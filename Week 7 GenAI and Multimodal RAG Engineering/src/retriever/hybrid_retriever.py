import json
import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from src.embeddings.embedder import Embedder

INDEX_PATH = "src/vectorstore/index.faiss"
METADATA_PATH = "src/vectorstore/metadata.json"

class HybridRetriever:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)

        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        self.embedder = Embedder()
       
        self.corpus = [doc["text"].split() for doc in self.metadata]
        self.bm25 = BM25Okapi(self.corpus)

    def apply_filters(self, docs, filters):
        if not filters:
            return docs

        filtered = []
        for doc in docs:
            metadata = doc["metadata"]
            match = True
            for key, value in filters.items():
                if metadata.get(key) != value:
                    match = False
                    break
            if match:
                filtered.append(doc)

        return filtered

    def deduplicate(self, docs):
        seen = set()
        unique_docs = []

        for doc in docs:
            text_hash = hash(doc["text"])
            if text_hash not in seen:
                seen.add(text_hash)
                unique_docs.append(doc)

        return unique_docs

    def search(self, query, top_k=5, filters=None):

        query_embedding = self.embedder.embed([query])
        distances, indices = self.index.search(query_embedding, 15)

        semantic_results = []
        for idx, dist in zip(indices[0], distances[0]):
            doc = self.metadata[idx]
            doc["semantic_score"] = float(1 / (1 + dist))
            semantic_results.append(doc)

        tokenized_query = query.split()
        bm25_scores = self.bm25.get_scores(tokenized_query)

        bm25_results = []
        top_bm25_idx = np.argsort(bm25_scores)[-15:]

        for idx in top_bm25_idx:
            doc = self.metadata[idx]
            doc["bm25_score"] = float(bm25_scores[idx])
            bm25_results.append(doc)

        combined = semantic_results + bm25_results

        for doc in combined:
            semantic_score = doc.get("semantic_score", 0)
            bm25_score = doc.get("bm25_score", 0)
            doc["hybrid_score"] = 0.6 * semantic_score + 0.4 * bm25_score

        combined = sorted(combined, key=lambda x: x["hybrid_score"], reverse=True)

        combined = self.deduplicate(combined)

        combined = self.apply_filters(combined, filters)

        return combined[:20]
