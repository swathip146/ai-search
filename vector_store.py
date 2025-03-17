from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from config import OPENAI_API_KEY

class VectorStore:
    """Handles storing and retrieving vectorized documents."""

    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.vector_db = None  # FAISS index

    def create_vector_store(self, text):
        """Converts text to embeddings and stores in FAISS."""
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_text(text)
        documents = [Document(page_content=chunk) for chunk in chunks]
        self.vector_db = FAISS.from_documents(documents, self.embeddings)
        print(f"🚀 Vector store created with {len(documents)} chunks.")

    def search(self, query, top_k=3):
        """Searches for the most relevant documents."""
        if not self.vector_db:
            return ["Vector store is empty."]
        return self.vector_db.similarity_search(query, k=top_k)
