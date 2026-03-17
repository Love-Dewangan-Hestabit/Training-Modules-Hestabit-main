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


class ChatRequest(BaseModel):
    message: str


@app.post("/generate")
def generate(req: GenerateRequest):

    request_id = str(uuid.uuid4())

    print("Request ID:", request_id)

    prompt = f"User: {req.prompt}\nAssistant:"

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=config.MAX_NEW_TOKENS,
        temperature=config.TEMPERATURE,
        top_k=config.TOP_K,
        top_p=config.TOP_P,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id
    )

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

    text = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    stop_phrases = ["User:", "\nUser:"]

    for stop in stop_phrases:
        if stop in text:
            text = text.split(stop)[0]

    return {
        "request_id": request_id,
        "response": text.strip()
    }


@app.post("/chat")
def chat(req: ChatRequest):

    request_id = str(uuid.uuid4())

    chat_history.append(f"User: {req.message}")

    prompt = (
        "Give clear, detailed, and complete answers.\n\n"
        + "\n".join(chat_history)
        + "\nAssistant:"
   )

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=config.MAX_NEW_TOKENS,
        temperature=config.TEMPERATURE,
        top_k=config.TOP_K,
        top_p=config.TOP_P,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id
    )

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

    text = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    stop_phrases = ["User:", "\nUser:"]
    for stop in stop_phrases:
        if stop in text:
            text = text.split(stop)[0]

    reply = text.strip()

    chat_history.append(f"Assistant: {reply}")

    return {
        "request_id": request_id,
        "response": reply
    }