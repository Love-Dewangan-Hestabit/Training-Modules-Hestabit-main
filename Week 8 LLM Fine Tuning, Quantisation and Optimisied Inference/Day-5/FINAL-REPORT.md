# Week 8 (Day 5) - Capstone: Build and Deploy Local LLM API

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To build a local LLM microservice using FastAPI that exposes model inference through REST APIs. The system provides endpoints for text generation (/generate) and chat interaction (/chat) using a quantised language model.

The implementation includes model caching, configurable generation parameters (temperature, top-k, top-p), request logging with request IDs, and infinite chat history. The project is structured for deployment readiness and designed to support future extensions such as RAG and AI agents.

## Technologies Used

The project uses the following technologies:

- **Python**
- **FastAPI** - API framework
- **Uvicorn** - ASGI server
- **Transformers (Hugging Face)** - Model loading and inference
- **PyTorch** - Deep learning framework

Model Used:

**TinyLlama/TinyLlama-1.1B-Chat-v1.0**

This lightweight model allows experimentation with LLM deployment on CPU
hardware.

## System Architecture

The architecture of the system follows a simple microservice structure:

```
                            Client Request
                                  |
                                  V
                            FastAPI Server
                                  |
                                  V
                             Model Loader
                                  |
                                  V
                      Language Model (TinyLlama)
                                  |
                                  V
                         Generated Response
```

### Components

1.  **FastAPI Server**
    - Handles incoming API requests
    - Validates request payloads
    - Routes requests to the model
2.  **Model Loader**
    - Loads the model once during startup
    - Caches the model in memory
    - Prevents repeated model loading
3.  **Configuration Module**
    - Stores generation parameters
    - Maintains model configuration settings

## API Endpoints

### 1. `/generate`

This endpoint generates text based on a prompt.

Example Request:

    POST /generate
    {
     "prompt": "Explain machine learning",
     "temperature": 0.7,
     "top_k": 50,
     "top_p": 0.9
    }

### 2. `/chat`

This endpoint supports conversational interaction by maintaining chat
history.

Example Request:

    POST /chat
    {
     "message": "What is deep learning?"
    }

The chat endpoint stores previous messages to maintain conversation
context.

## Key Features

- **Local LLM deployment**
- **FastAPI microservice architecture**
- **Configurable generation parameters**
  - Temperature
  - Top-k sampling
  - Top-p sampling
- **Request ID logging**
- **Docker-ready structure**

## Deployment

The application can be deployed locally using:

    uvicorn deploy.app:app --reload

The server will run at:

    http://127.0.0.1:8000

API documentation is available at:

    http://127.0.0.1:8000/docs

FastAPI automatically generates interactive Swagger documentation.

## Docker Support

The project includes a Dockerfile to enable containerized deployment.

Build the container:

    docker build -t llm-api .

Run the container:

    docker run -p 8000:8000 llm-api

## Challenges Faced

1.  Handling model loading efficiently
2.  Ensuring compatibility with CPU-only environments
3.  Managing chat history for conversational interactions
4.  Configuring API parameters for flexible generation

These challenges were addressed through modular code design and
configuration-based control.
