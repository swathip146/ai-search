from document_loader import DocumentLoader
from vector_store import VectorStore
import uvicorn
from api import app, initialize_query_engine

PDF_PATH = "resources/Grokking-the-system-design-interviewpdf-5-pdf-free (1).pdf"

if __name__ == "__main__":
    print("🚀 In Main of AI Search Engine")
    # Load and process the document
    loader = DocumentLoader()
    text = loader.extract_text(PDF_PATH)
    print(f"🚀 Text extracted from PDF size: {len(text)}")
    print(text[:500])

    # Create vector database
    vector_store = VectorStore()
    vector_store.create_vector_store(text)

    # ✅ Pass it to API before running the server
    initialize_query_engine(vector_store)

    # Run FastAPI server
    print("🚀 AI Search API running at: http://127.0.0.1:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
