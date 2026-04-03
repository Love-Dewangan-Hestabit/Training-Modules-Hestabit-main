import json
import faiss
import numpy as np
from embeddings.embedder import Embedder

CHUNKS_PATH = "data/chunks/chunks.json"
INDEX_PATH = "vectorstore/index.faiss"
METADATA_PATH = "vectorstore/metadata.json"

def build_index():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [chunk["text"] for chunk in chunks]

    embedder = Embedder()
    embeddings = embedder.embed(texts)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f)

    print("FAISS index built and saved.")


if __name__ == "__main__":
    build_index()
