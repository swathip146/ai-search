from fastapi import FastAPI
from query_engine import QueryEngine

app = FastAPI()
query_engine = None

@app.get("/search/")
def search(query: str):
    """API to search the vector database."""
    if query_engine is None:
        return {"error": "Query engine not initialized."}
    results = query_engine.process_query(query)
    return {"query": query, "results": results}

# New function to set the vector store instance
def initialize_query_engine(vector_store):
    """Initialize the QueryEngine with a shared VectorStore instance."""
    global query_engine
    query_engine = QueryEngine(vector_store)
