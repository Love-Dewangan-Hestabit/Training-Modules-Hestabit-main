import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import os


class VectorStore:
    def __init__(
        self,
        index_path="memory/faiss.index",
        meta_path="memory/meta.pkl"
    ):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.index_path = index_path
        self.meta_path = meta_path
        self.dimension = 384

        # Load or initialize
        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.index = faiss.read_index(index_path)

            with open(meta_path, "rb") as f:
                self.metadata = pickle.load(f)

            # 🔥 SYNC CHECK
            if self.index.ntotal != len(self.metadata):
                print("⚠️ FAISS index and metadata mismatch. Resetting...")
                self.index = faiss.IndexFlatL2(self.dimension)
                self.metadata = []

        else:
            self.index = faiss.IndexFlatL2(self.dimension)
            self.metadata = []

    def add(self, text, meta):
        embedding = self.model.encode([text])

        self.index.add(np.array(embedding).astype("float32"))
        self.metadata.append(meta)

        # 🔥 HARD CHECK
        assert self.index.ntotal == len(self.metadata), \
            "FAISS and metadata out of sync!"

        self._save()

    def search(self, query, k=3):
        # 🔥 EMPTY CHECK
        if len(self.metadata) == 0:
            return []

        embedding = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(embedding).astype("float32"), k
        )

        results = []

        for i in indices[0]:
            if 0 <= i < len(self.metadata):
                results.append(self.metadata[i])

        return results

    def _save(self):
        faiss.write_index(self.index, self.index_path)

        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)