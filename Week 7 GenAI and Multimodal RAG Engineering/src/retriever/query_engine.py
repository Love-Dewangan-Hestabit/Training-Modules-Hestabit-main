import faiss
import json
import numpy as np
from embeddings.embedder import Embedder

INDEX_PATH = "vectorstore/index.faiss"
METADATA_PATH = "vectorstore/metadata.json"

class QueryEngine:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)

        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        self.embedder = Embedder()

    def query(self, question, top_k=3):
        query_embedding = self.embedder.embed([question])

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results


if __name__ == "__main__":
    engine = QueryEngine()
    question = input("Ask your question: ")
    results = engine.query(question)

    for i, result in enumerate(results):
        print(f"\nResult {i+1}")
        print(result["text"])
        print("Source:", result["metadata"]["source"])
