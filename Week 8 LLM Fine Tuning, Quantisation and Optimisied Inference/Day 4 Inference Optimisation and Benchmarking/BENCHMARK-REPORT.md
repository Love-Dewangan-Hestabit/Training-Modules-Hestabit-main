# Week 8 (Day 4) - Inference Optimisation and Benchmarking

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To benchmark and optimise inference performance of LLM under Base Model, Fine-tuned model and Quantised model.

## Environment Setup

- Platform: Google Colab
- GPU: Nvidia T4
- Frameworks:
  - PyTorch
  - HuggingFace Transformers
  - LoRA
  - bitsandbytes
  - llama.cpp
- Precision:
  - FP16 (baseline)
  - LoRA (FP16 + adapter)
  - GGUF (4-bit quantised)

## Models Evaluated

### Base Model (FP16)

- Model: TinyLlama-1.1B-Chat
- Precision: FP16
- KV caching enabled (use_cache=True)

Purpose: To establish a baseline for latency, VRAM usage, and output
quality.

### Fine-Tuned Model

- Base model: TinyLlama
- Adapter: Custom LoRA fine-tuned adapter
- Precision: FP16 (base) + LoRA weights

Purpose: To evaluate whether fine-tuning impacts:

- Inference speed
- Memory usage
- Task-specific accuracy

### Quantised Model

- Converted to GGUF format
- 4-bit quantisation
- Inference via llama.cpp (CPU execution)

Purpose: To evaluate:

- Memory reduction
- CPU-based inference performance
- Trade-offs in speed and quality

## Metrics Measured

### Latency

Total time taken to generate output for a given prompt.

### Tokens Per Second

Tokens/sec = total_generated_tokens / latency

Higher values indicate faster inference.

### VRAM Usage

Measured before and after generation using NVML.

### Accuracy

Measured qualitatively based on:

- Coherence
- Relevance
- Instruction-following ability

## Benchmark Observations

### Base FP16

- Fast GPU inference
- High throughput
- High VRAM usage
- Stable quality

### Fine-tuned LoRA

- Minimal increase in latency
- Slight VRAM increase
- Improved task-specific responses

### Quantised GGUF

- Very low memory usage
- Higher latency on CPU
- Slight reduction in richness of output
