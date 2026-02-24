# Week 7 (Day 5) - Advanced Rag, Memory and Evaluation

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To Build a complete system with endpoints for Text/Document Retrieval, Image Retrieval and SQL question and answering. Also the system should include Memory for the last 5 message, Hallucination Detection, Debugging Traces and Streamlit UI.

## Overview

This project implements a production-ready Advanced Multimodal RAG
System with:

- Text RAG (Hybrid Retrieval + Reranking)
- SQL RAG (Dynamic DB / CSV / Excel Upload)
- Image RAG (CLIP + OCR + Hybrid Search)
- Conversational Memory (Last 5 Messages)
- Refinement Loop
- Hallucination Detection
- Faithfulness Scoring
- Confidence Score
- Debug Traces
- Streamlit UI
- FastAPI Backend

## Environment Setup

## Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

## Install Dependencies

```
pip install streamlit
pip install fastapi uvicorn
pip install sentence-transformers
pip install faiss-cpu
pip install rank-bm25
pip install tiktoken
pip install tabulate
pip install pypdf python-docx pandas
pip install pillow pytesseract
pip install transformers torch
pip install sqlparse
pip install google-generativeai
pip install openpyxl
pip install pypandoc
```

## Environment Variables

Set Gemini API key (if using Gemini):

```
export GOOGLE_API_KEY=your_api_key_here
```

## Running the Application

### Streamlit UI

From project root:

```
streamlit run streamlit_app.py
```

### FastAPI Backend

```
uvicorn src.deployment.app:app --reload
```

## SQL RAG Usage

Supported uploads:

- `.csv`
- `.xlsx`

```
Flow:
                         Upload file
                              |
                              V
               Tables auto-created (for CSV/XLSX)
                              |
                              V
                 Ask natural language question
                              |
                              V
                        SQL generated
                              |
                              V
                      Results Displayed
```

## Evaluation & Scoring

Text RAG includes:

- Refinement loop
- Hallucination detection
- Faithfulness score (0-1)
- Confidence score
