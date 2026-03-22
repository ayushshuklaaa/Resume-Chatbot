from fastapi import FastAPI
from routes import router

app = FastAPI(title="Resume Chatbot API")

# Include all modular endpoints from routes.py
app.include_router(router)
