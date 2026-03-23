import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# App Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env file.")

# Gemini API Key (optional — used as fallback when Groq hits rate limits)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Configuration — Fallback chain order:
# 1. Groq (Llama 3.3 70B)  →  2. Gemini 2.0 Flash  →  3. Gemini 1.5 Flash
GROQ_MODEL = "llama-3.3-70b-versatile"
GEMINI_MODEL_PRIMARY = "gemini-2.0-flash"
GEMINI_MODEL_FALLBACK = "gemini-1.5-flash"

# Database Configuration
CHROMA_DB_DIR = "./chroma_db"
COLLECTION_NAME = "resume_collection"
