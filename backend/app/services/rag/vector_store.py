import faiss
import numpy as np
from app.services.rag.embeddings import EmbeddingService

class VectorStore:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.index = faiss.IndexFlatL2(384)
        self.documents = []

    def add_documents(self, docs):
        embeddings = self.embedding_service.embed(docs)
        self.index.add(np.array(embeddings).astype("float32"))
        self.documents.extend(docs)

    def search(self, query, k=3):
        query_embedding = self.embedding_service.embed([query])
        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"), k
        )
        return [self.documents[i] for i in indices[0] if i != -1]
