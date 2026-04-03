
import os
import pickle

import faiss
import numpy as np

os.environ["TOKENIZERS_PARALLELISM"] = "false"
import transformers
transformers.logging.set_verbosity_error()

from sentence_transformers import SentenceTransformer

class VectorStore:
    MODEL_NAME = "all-MiniLM-L6-v2"
    DIMENSION = 384  

    def __init__(
        self,
        index_path: str = "memory/faiss.index",
        meta_path: str = "memory/meta.pkl",
    ):
        os.makedirs(os.path.dirname(index_path), exist_ok=True)

        self.index_path = index_path
        self.meta_path = meta_path
        self.model = SentenceTransformer(self.MODEL_NAME)

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.index = faiss.read_index(index_path)
            with open(meta_path, "rb") as f:
                self.metadata: list[dict] = pickle.load(f)

            if self.index.ntotal != len(self.metadata):
                print("[VECTOR STORE] Index/metadata mismatch — resetting.")
                self.index = faiss.IndexFlatL2(self.DIMENSION)
                self.metadata = []
        else:
            self.index = faiss.IndexFlatL2(self.DIMENSION)
            self.metadata = []

    def add(self, text: str, meta: dict) -> None:
        """Embed `text` and store alongside `meta` dict."""
        embedding = self.model.encode([text])
        self.index.add(np.array(embedding).astype("float32"))
        self.metadata.append(meta)

        assert self.index.ntotal == len(self.metadata), \
            "FAISS index and metadata are out of sync!"

        self._save()

    def search(self, query: str, k: int = 3) -> list[dict]:
        """Return up to `k` metadata dicts most similar to `query`."""
        if not self.metadata:
            return []

        embedding = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(embedding).astype("float32"), min(k, len(self.metadata))
        )

        results = []
        for i in indices[0]:
            if 0 <= i < len(self.metadata):
                results.append(self.metadata[i])
        return results

    def _save(self) -> None:
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def count(self) -> int:
        return self.index.ntotal
