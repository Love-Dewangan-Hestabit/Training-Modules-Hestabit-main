import torch
import time
import pandas as pd
import psutil
import os
import pynvml
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from llama_cpp import Llama
from difflib import SequenceMatcher

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BASE_PATH = "/content/drive/MyDrive"

def get_peak_vram():
    if not torch.cuda.is_available():
        return 0
    return torch.cuda.max_memory_allocated() / (1024 ** 3)

def compute_accuracy(generated, reference):
    return SequenceMatcher(None, generated, reference).ratio()

def tokens_per_second(tokens, latency):
    return tokens / latency

def load_base_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
        device_map="auto" if DEVICE == "cuda" else None
    )
    if DEVICE == "cuda":
        model.to(DEVICE)
    return model, tokenizer

def load_lora_model(base_model):
    adapter_path = f"{BASE_PATH}/adapter"
    if not os.path.exists(adapter_path):
        raise ValueError(f"Adapter folder not found: {adapter_path}")
    model = PeftModel.from_pretrained(base_model, adapter_path)
    return model

def run_transformer(model, tokenizer, prompt, reference):
    inputs = tokenizer(prompt, return_tensors="pt")
    if DEVICE == "cuda":
        inputs = inputs.to(DEVICE)
    if DEVICE == "cuda":
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()

    start = time.time()

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=100
        )

    end = time.time()

    latency = end - start
    generated = tokenizer.decode(output[0], skip_special_tokens=True)
    tokens = len(output[0])
    accuracy = compute_accuracy(generated, reference)
    vram = get_peak_vram()

    return {
        "latency": latency,
        "tokens_per_sec": tokens_per_second(tokens, latency),
        "vram_used_gb": vram,
        "accuracy": accuracy
    }

def load_quantized_model():
    model_path = f"{BASE_PATH}/quantized/model.gguf"
    if not os.path.exists(model_path):
        raise ValueError(f"GGUF model not found: {model_path}")
    llm = Llama(
        model_path=model_path,
        n_threads=psutil.cpu_count(),
        n_ctx=2048
    )
    return llm

def run_quantized(llm, prompt, reference):
    start = time.time()
    output = llm(prompt, max_tokens=100)
    end = time.time()

    latency = end - start
    text = output["choices"][0]["text"]
    tokens = len(text.split())
    accuracy = compute_accuracy(text, reference)

    return {
        "latency": latency,
        "tokens_per_sec": tokens_per_second(tokens, latency),
        "vram_used_gb": 0,
        "accuracy": accuracy
    }

def benchmark():
    base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    prompt = "Explain machine learning in simple terms."

    reference_answer = """
Machine learning is a type of artificial intelligence where computers learn patterns
from data and make predictions or decisions without being explicitly programmed.
"""

    results = []

    print("\nRunning Base Model Benchmark...\n")

    base_model, tokenizer = load_base_model(base_model_name)

    result = run_transformer(base_model, tokenizer, prompt, reference_answer)
    result["model"] = "Base FP16"
    results.append(result)

    del base_model
    torch.cuda.empty_cache()

    print("\nRunning LoRA Model Benchmark...\n")

    base_model, tokenizer = load_base_model(base_model_name)
    lora_model = load_lora_model(base_model)

    result = run_transformer(lora_model, tokenizer, prompt, reference_answer)
    result["model"] = "Fine-tuned LoRA"
    results.append(result)

    del base_model
    del lora_model
    torch.cuda.empty_cache()

    print("\nRunning Quantized GGUF Benchmark...\n")

    llm = load_quantized_model()

    result = run_quantized(llm, prompt, reference_answer)
    result["model"] = "Quantized GGUF"
    results.append(result)

    df = pd.DataFrame(results)

    save_path = f"{BASE_PATH}/benchmarks/results.csv"

    df.to_csv(save_path, index=False)

    print("\nBenchmark Results\n")
    print(df)
    print(f"\nResults saved to: {save_path}")

if __name__ == "__main__":
    benchmark()