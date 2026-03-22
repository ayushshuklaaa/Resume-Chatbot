# 💼 Resume AI Assistant

An intelligent, context-aware AI chatbot that answers questions based strictly on a provided knowledge base (like a resume or portfolio). Powered by **FastAPI**, **ChromaDB** (Vector Database), and **Groq** (LLaMA 3).

## ✨ Features
- **Strict Context Answering:** The AI is strictly prompted to answer **only** from the provided documents. If it doesn't know the answer, it politely declines rather than hallucinating.
- **Dynamic Knowledge Base:** Upload `.txt` or `.docx` files directly through the UI. The backend automatically extracts the text, chunks it, and ingests it into the ChromaDB vector store.
- **FastAPI Backend:** Fully modular, asynchronous, and high-performance backend routing.
- **RAG Pipeline:** Utilizes Retrieval-Augmented Generation (RAG) by performing semantic similarity searches across the embedded document chunks before generating a response.
- **Modern UI:** Clean, responsive, and lightweight HTML/CSS frontend.

---

## 🛠️ Project Structure
```text
Chatbot/
├── main.py                  # The main FastAPI server entry point
├── config.py                # Environment variables and API keys
├── database.py              # ChromaDB vector store connection
├── llm.py                   # Groq API client and System Prompts
├── document_processor.py    # File extraction (.txt/.docx) and text chunking
├── routes.py                # API endpoints (/chat, /upload)
├── templates/
│   └── index.html           # The Chatbot Frontend UI
├── resume_data.py           # The base source-of-truth knowledge chunks
├── requirements.txt         # Python dependencies
└── .env                     # Your private environment variables
```

---

## 🚀 Setup & Installation

### 1. Clone the repository
Make sure you have Python 3.10+ installed.

### 2. Install Dependencies
Run the following command to install required libraries (FastAPI, ChromaDB, Groq, etc.):
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a file named `.env` in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```
*(You can get a free API key at [console.groq.com](https://console.groq.com/keys))*

### 4. Run the Server
Start the Uvicorn ASGI server:
```bash
python -m uvicorn main:app --reload --port 5000
```

### 5. Access the App
Open your browser and navigate to:
**[http://localhost:5000](http://localhost:5000)**

---

## 🧠 How It Works
1. **Embedding:** When you upload a file, the `document_processor.py` splits the text into ~800-character chunks and adds them to the local `chroma_db` folder.
2. **Retrieval (RAG):** When you ask a question, ChromaDB fetches the top 15 most semantically relevant chunks from the database.
3. **Generation:** The retrieved chunks are passed as context to the LLaMA 3 model via Groq, which reads them and outputs a natural, strictly fact-based answer.
