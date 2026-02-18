import os
import json
import pandas as pd
from pypdf import PdfReader
from docx import Document
import tiktoken
from datetime import datetime, timezone


RAW_DATA_PATH = "src/data/raw/"
CHUNKS_PATH = "src/data/chunks/chunks.json"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100



def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text


def load_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()


def clean_text(text):
    return text.replace("\n", " ").strip()


def chunk_text(text, source, file_type):
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)

    chunks = []
    chunk_id = 0

    for i in range(0, len(tokens), CHUNK_SIZE - CHUNK_OVERLAP):
        chunk_tokens = tokens[i:i + CHUNK_SIZE]
        chunk_text = tokenizer.decode(chunk_tokens)

        chunks.append({
            "text": chunk_text,
            "metadata": {
                "source": source,
                "file_type": file_type,
                "chunk_id": chunk_id,
                "char_count": len(chunk_text),
                "token_count": len(chunk_tokens),
                "ingested_at": datetime.now(timezone.utc).isoformat()

            }
        })

        chunk_id += 1

    return chunks


def ingest_documents():
    all_chunks = []

    for filename in os.listdir(RAW_DATA_PATH):
        file_path = os.path.join(RAW_DATA_PATH, filename)

        if filename.endswith(".pdf"):
            text = load_pdf(file_path)
            file_type = "pdf"

        elif filename.endswith(".docx"):
            text = load_docx(file_path)
            file_type = "docx"

        elif filename.endswith(".txt"):
            text = load_txt(file_path)
            file_type = "txt"

        elif filename.endswith(".csv"):
            text = load_csv(file_path)
            file_type = "csv"

        else:
            continue

        cleaned = clean_text(text)
        chunks = chunk_text(cleaned, filename, file_type)
        all_chunks.extend(chunks)

    os.makedirs("data/chunks", exist_ok=True)

    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    print(f"Ingestion complete. {len(all_chunks)} chunks created.")


if __name__ == "__main__":
    ingest_documents()
