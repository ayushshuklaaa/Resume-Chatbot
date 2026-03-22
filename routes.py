from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from document_processor import process_and_store_document
from database import get_db_collection
from llm import get_system_prompt, generate_chat_response

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    message: str

@router.get("/", response_class=HTMLResponse)
async def get_ui(request: Request):
    """Serves the main frontend UI from the templates folder."""
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Handles user chat by querying the relevant text chunks from the vector DB,
    formatting the system context prompt, and calling Groq LLM to answer.
    """
    user_message = request.message.strip()
    if not user_message:
        return JSONResponse({"error": "Message cannot be empty"}, status_code=400)

    try:
        collection = get_db_collection()
        if collection:
            results = collection.query(
                query_texts=[user_message],
                n_results=15
            )
            context = "\n\n".join(results["documents"][0])
        else:
            context = ""
            
        system_prompt = get_system_prompt(context)
        response_text = generate_chat_response(system_prompt, user_message)
        
        return {"reply": response_text}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Receives file bytes, defers processing to document_processor, and saves chunks."""
    collection = get_db_collection()
    if not collection:
        return JSONResponse({"error": "Database not initialized"}, status_code=500)

    try:
        file_bytes = await file.read()
        num_chunks = process_and_store_document(file.filename, file_bytes)
        return {"message": f"Successfully processed '{file.filename}' into {num_chunks} chunks."}
    except ValueError as ve:
        return JSONResponse({"error": str(ve)}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
