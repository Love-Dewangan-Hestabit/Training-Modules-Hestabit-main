# Week 8 (Day 5) — Build & Deploy Local LLM API

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Overview

This project implements a **Local Large Language Model (LLM) API** using FastAPI.
The API exposes model inference through REST endpoints for **text generation** and **chat interaction**.

The system is designed as a lightweight **LLM microservice** that can run locally on CPU and is structured for future integration with **RAG pipelines and AI agents**.

## Features

- Local LLM inference API
- `/generate` endpoint for text generation
- `/chat` endpoint for conversational interaction
- Configurable generation parameters (temperature, top-k, top-p)
- Model caching (model loads once at startup)
- Request ID logging
- Deployment-ready project structure
- Docker support

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Transformers (Hugging Face)
- PyTorch

Model Used:
TinyLlama/TinyLlama-1.1B-Chat-v1.0

## Running the API

cd deploy

uvicorn app:app --reload

Server runs at:
http://127.0.0.1:8000

API Docs:
http://127.0.0.1:8000/docs

## Docker Deployment

docker build -t llm-api .

docker run -p 8000:8000 llm-api
