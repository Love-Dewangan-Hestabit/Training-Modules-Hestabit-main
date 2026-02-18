# Week 7 (Day 1) - Local Rag System and Pipeline Architecture

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To build Local Ingestion and Chunking Pipeline

## High-Level Architecture

```
                           Documents
                               |
                               V
                        Text Extraction
                               |
                               V
                            Cleaning
                               |
                               V
                            Chunking
                               |
                               V
                           Embedding
                               |
                               V
                             Vector
                               |
                               V
                         Storage (FAISS)
                               |
                               V
                       Semantic Retrieval
```

This architecture enables meaning-based search instead of keyword-based search through Semantic Indexing.

## Ingestion Pipeline

### Step 1: Document Loading

Ingestion supports PDF, DOCX, TXT and CSV.
Firstly each file is converted into raw text

### Step 2: Text Cleaning

Removes newline characters and extra spaces to improve embedding quality.

### Step 3: Chunking Strategy

Documents are split into 500 token chunks with 100 token overlap using the tiktoken.

## Metadata Design

Each chunk stores the following metadata:

- source
- filetype
- chunkid
- charcount
- tokencount
- ingested_at

This enables traceability, evaluation, and filtering
capabilities.

## Embedding Model

Embedding Model Used: - all-MiniLM-L6-v2

I used this mode as this is Lightweight, Fast and Suitable for local development

Each chunk is converted into a numerical vector representation.

## Vector Database

For Vector Storage I used - FAISS
I used FAISS as it has high performance and local deployment

All embeddings are stored here
vectorstore/index.faiss
vectorstore/metadata.json

## Learning Outcomes

- Understanding RAG fundamentals and Architecture
- Importance of chunking strategy
- Role of embeddings in semantic search
- Importance of Overlapping while implementing Chunking
- Handling real-world PDF ingestion errors
