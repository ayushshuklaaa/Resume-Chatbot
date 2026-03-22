import os
import uuid
from docx import Document
from database import get_db_collection

def extract_text_from_txt(file_bytes: bytes) -> str:
    """Decode text file bytes."""
    for encoding in ['utf-8', 'latin-1', 'windows-1252']:
        try:
            return file_bytes.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise Exception("Could not decode .txt file. Unknown encoding.")

def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract text from a DOCX file using a temporary save."""
    temp_path = f"temp_{uuid.uuid4().hex}.docx"
    try:
        with open(temp_path, "wb") as f:
            f.write(file_bytes)
        
        doc = Document(temp_path)
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text.strip())
        return "\n".join(full_text)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

def chunk_text(text: str, chunk_size: int = 800) -> list[str]:
    """Splits text into chunks of `chunk_size` characters by paragraph."""
    paragraphs = text.split('\n')
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if not para.strip():
            continue
            
        if len(current_chunk) + len(para) <= chunk_size:
            current_chunk += para + "\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n"
            
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def process_and_store_document(filename: str, file_bytes: bytes) -> int:
    """
    Extracts text, splits it into chunks, and adds it to the active ChromaDB collection.
    Returns the number of chunks added.
    """
    if filename.endswith(".txt"):
        text = extract_text_from_txt(file_bytes)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file format. Only .txt and .docx are allowed.")

    if not text.strip():
        raise ValueError("The uploaded file is empty or contains no readable text.")

    chunks = chunk_text(text)
    
    collection = get_db_collection()
    if not collection:
        raise Exception("Database not initialized")

    base_id = uuid.uuid4().hex
    ids = [f"upload_{base_id}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": filename} for _ in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=metadatas
    )
    
    return len(chunks)
