import torch
import time
import psutil
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from peft import PeftModel # type: ignore
import pynvml # type: ignore
from tqdm import tqdm

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def get_vram_usage():
    if not torch.cuda.is_available():
        return 0
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    return info.used / (1024 ** 3) 

def tokens_per_second(output_ids, elapsed):
    total_tokens = output_ids.shape[-1]
    return total_tokens / elapsed


def load_base_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype=torch.float16,
        device_map="auto"
    )
    return model, tokenizer


def load_finetuned_model(base_model_name, adapter_path):
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        dtype=torch.float16,
        device_map="auto"
    )
    model = PeftModel.from_pretrained(model, adapter_path)
    return model, tokenizer


def run_inference(model, tokenizer, prompt, stream=False):
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)

    if stream:
        streamer = TextStreamer(tokenizer)

    torch.cuda.empty_cache()
    start_vram = get_vram_usage()

    start = time.time()

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            use_cache=True,
            streamer=streamer if stream else None
        )

    end = time.time()
    end_vram = get_vram_usage()

    elapsed = end - start
    tps = tokens_per_second(output, elapsed)

    return {
        "latency": elapsed,
        "tokens_per_sec": tps,
        "vram_used_gb": end_vram - start_vram
    }


def run_batch_inference(model, tokenizer, prompts):
    inputs = tokenizer(prompts, return_tensors="pt", padding=True).to(DEVICE)

    start = time.time()
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=50)

    end = time.time()
    return (end - start)


def benchmark():

    base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    adapter_path = "adapter"

    prompt = "Explain machine learning in simple terms."

    results = []

    model, tokenizer = load_base_model(base_model_name)
    result = run_inference(model, tokenizer, prompt)
    result["model"] = "Base FP16"
    results.append(result)

  
    model, tokenizer = load_finetuned_model(base_model_name, adapter_path)
    result = run_inference(model, tokenizer, prompt)
    result["model"] = "Fine-tuned LoRA"
    results.append(result)

    df = pd.DataFrame(results)
    df.to_csv("benchmarks/results.csv", index=False)

    print("\nBenchmark Results:")
    print(df)


if __name__ == "__main__":
    benchmark()
