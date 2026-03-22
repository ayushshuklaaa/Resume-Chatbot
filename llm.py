from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

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

def generate_chat_response(system_prompt: str, user_message: str) -> str:
    """Calls the Groq API to generate a response."""
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.5,   # Balanced: not too creative, not too rigid
        max_tokens=512,     # Keep replies concise
    )
    return response.choices[0].message.content
