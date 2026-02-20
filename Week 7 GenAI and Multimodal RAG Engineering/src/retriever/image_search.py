import faiss
import json
import numpy as np
from rank_bm25 import BM25Okapi
from src.embeddings.clip_embedder import CLIPEmbedder


INDEX_PATH = "src/vectorstore/image_index.faiss"
METADATA_PATH = "src/vectorstore/image_metadata.json"


class HybridImageSearch:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)
        self.embedder = CLIPEmbedder()

        with open(METADATA_PATH, "r") as f:
            self.metadata = json.load(f)

        self.corpus = [
            doc["ocr_text"].lower().split()
            for doc in self.metadata
        ]
        self.bm25 = BM25Okapi(self.corpus)

    def deduplicate(self, results):
        seen = set()
        unique = []

        for doc in results:
            path = doc["image_path"]
            if path not in seen:
                seen.add(path)
                unique.append(doc)

        return unique

    def save_results(self, results, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for i, res in enumerate(results):
                f.write(f"Result {i+1}\n")
                f.write(f"Image: {res['image_path']}\n")
                f.write(f"Caption: {res['caption']}\n")
                f.write(f"OCR Text:\n{res['ocr_text']}\n")
                f.write("-" * 60 + "\n")

    def text_to_image(self, query, top_k=5):

        query_embedding = self.embedder.embed_text(query)
        clip_scores, indices = self.index.search(
            query_embedding.astype("float32"), len(self.metadata)
        )

        clip_scores = clip_scores[0]
        indices = indices[0]

        tokenized_query = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)

        results = []

        for rank, idx in enumerate(indices):
            doc = self.metadata[idx]

            clip_score = float(clip_scores[rank])
            ocr_score = float(bm25_scores[idx])

            ocr_score = ocr_score / (max(bm25_scores) + 1e-6)

            hybrid_score = 0.6 * clip_score + 0.4 * ocr_score

            doc_copy = doc.copy()
            doc_copy["hybrid_score"] = hybrid_score

            results.append(doc_copy)

        results = sorted(
            results,
            key=lambda x: x["hybrid_score"],
            reverse=True
        )

        results = self.deduplicate(results)

        final = results[:top_k]

        self.save_results(final, "text_to_image_results.txt")

        return final


if __name__ == "__main__":
    search = HybridImageSearch()

    mode = input("Mode (text/image): ")

    if mode == "text":
        query = input("Enter query: ")
        search.text_to_image(query)