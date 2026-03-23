import logging
from groq import Groq, RateLimitError as GroqRateLimitError
from config import (
    GROQ_API_KEY, GROQ_MODEL,
    GEMINI_API_KEY, GEMINI_MODEL_PRIMARY, GEMINI_MODEL_FALLBACK
)

# ── Clients ────────────────────────────────────────────────────────────────────
groq_client = Groq(api_key=GROQ_API_KEY)

gemini_client = None
if GEMINI_API_KEY:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_client = genai
else:
    logging.warning("GEMINI_API_KEY not set — Gemini fallback is disabled.")

logger = logging.getLogger(__name__)

# ── System Prompt ──────────────────────────────────────────────────────────────
def get_system_prompt(context: str) -> str:
    """Generates the strict instructional prompt with the provided context."""
    return f"""
    You are a polite and professional AI assistant for Ayush.
    
    RULES:
    1. You may engage in brief general pleasantries (like "Hello", "I am doing well"). But DO NOT ask the user open-ended questions like "How are you?" or "How's your day?". Just answer the greeting naturally and ask how you can help.
    2. For ANY question requiring facts, details, or knowledge, you MUST answer ONLY based on the RELEVANT RESUME DATA below.
    3. If asked a question that cannot be answered using the RELEVANT RESUME DATA below, you must respond EXACTLY with:
       "I do not have information about that in my current knowledge base."
    4. DO NOT use external knowledge. DO NOT guess or hallucinate details.
    
    === RELEVANT RESUME DATA ===
    {context}
    ===================
    """

# ── Gemini Helper ──────────────────────────────────────────────────────────────
def _call_gemini(model_name: str, system_prompt: str, user_message: str) -> str:
    """Call a Gemini model with the given prompts."""
    model = gemini_client.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt,
    )
    response = model.generate_content(
        user_message,
        generation_config={"temperature": 0.5, "max_output_tokens": 512},
    )
    return response.text

# ── Main Entry Point with Fallback Chain ───────────────────────────────────────
def generate_chat_response(system_prompt: str, user_message: str) -> str:
    """
    Attempts to generate a response using a fallback chain:
      1. Groq  (Llama 3.3 70B)
      2. Gemini 2.0 Flash
      3. Gemini 1.5 Flash
    Falls back to the next model only on rate-limit (429) errors.
    """

    # ── 1. Try Groq ────────────────────────────────────────────────────────────
    try:
        logger.info("Calling Groq (%s)…", GROQ_MODEL)
        response = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_message},
            ],
            temperature=0.5,
            max_tokens=512,
        )
        return response.choices[0].message.content

    except GroqRateLimitError:
        logger.warning("Groq rate limit hit — falling back to Gemini 2.0 Flash.")
    except Exception as e:
        # Re-raise non-rate-limit Groq errors immediately
        raise RuntimeError(f"Groq error: {e}") from e

    # ── 2. Try Gemini 2.0 Flash ────────────────────────────────────────────────
    if gemini_client:
        try:
            logger.info("Calling Gemini (%s)…", GEMINI_MODEL_PRIMARY)
            return _call_gemini(GEMINI_MODEL_PRIMARY, system_prompt, user_message)
        except Exception as e:
            err = str(e)
            if "429" in err or "quota" in err.lower() or "rate" in err.lower():
                logger.warning("Gemini 2.0 Flash rate limit hit — falling back to Gemini 1.5 Flash.")
            else:
                raise RuntimeError(f"Gemini 2.0 Flash error: {e}") from e

        # ── 3. Try Gemini 1.5 Flash ────────────────────────────────────────────
        try:
            logger.info("Calling Gemini (%s)…", GEMINI_MODEL_FALLBACK)
            return _call_gemini(GEMINI_MODEL_FALLBACK, system_prompt, user_message)
        except Exception as e:
            raise RuntimeError(f"All models exhausted. Last error (Gemini 1.5 Flash): {e}") from e

    raise RuntimeError(
        "Groq rate limit reached and no GEMINI_API_KEY is configured. "
        "Add GEMINI_API_KEY to your .env file to enable fallback."
    )

