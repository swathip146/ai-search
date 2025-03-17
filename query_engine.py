from vector_store import VectorStore

class QueryEngine:
    """Handles search queries against the vector database."""

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def process_query(self, query):
        """Search for relevant content."""
        results = self.vector_store.search(query)
        print(f"Results: {results}")
        return [doc.page_content for doc in results]
