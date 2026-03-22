import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# App Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env file.")

# LLM Configuration
GROQ_MODEL = "llama-3.3-70b-versatile"

# Database Configuration
CHROMA_DB_DIR = "./chroma_db"
COLLECTION_NAME = "resume_collection"
