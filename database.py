import chromadb
from config import CHROMA_DB_DIR, COLLECTION_NAME

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

def get_db_collection():
    """Lazily gets or creates the collection to prevent crashes if it gets deleted."""
    try:
        return chroma_client.get_or_create_collection(name=COLLECTION_NAME)
    except Exception as e:
        print(f"Warning: Collection could not be loaded. {e}")
        return None
