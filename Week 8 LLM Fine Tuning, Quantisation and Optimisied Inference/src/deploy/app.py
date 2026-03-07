from fastapi import FastAPI
from pydantic import BaseModel
import uuid

import config
from model_loader import load_model

app = FastAPI(title="Local LLM API")

model, tokenizer = load_model()

chat_history = []


class GenerateRequest(BaseModel):

    prompt: str
    max_tokens: int = config.MAX_NEW_TOKENS
    temperature: float = config.TEMPERATURE
    top_k: int = config.TOP_K
    top_p: float = config.TOP_P


class ChatRequest(BaseModel):

    message: str
    temperature: float = config.TEMPERATURE
    top_k: int = config.TOP_K
    top_p: float = config.TOP_P


@app.post("/generate")

def generate(req: GenerateRequest):

    request_id = str(uuid.uuid4())

    print("Request ID:", request_id)

    inputs = tokenizer(req.prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=req.max_tokens,
        temperature=req.temperature,
        top_k=req.top_k,
        top_p=req.top_p,
        do_sample=True
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "request_id": request_id,
        "response": text
    }


@app.post("/chat")

def chat(req: ChatRequest):

    request_id = str(uuid.uuid4())

    chat_history.append(f"User: {req.message}")

    prompt = "\n".join(chat_history) + "\nAssistant:"

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=req.temperature,
        top_k=req.top_k,
        top_p=req.top_p,
        do_sample=True
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    reply = text.split("Assistant:")[-1]

    chat_history.append(f"Assistant: {reply}")

    return {
        "request_id": request_id,
        "response": reply
    }