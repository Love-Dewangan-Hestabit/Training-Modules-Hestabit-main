# Week 8 (Day 2) - Parameter Efficient Fine Tuning (LoRA/QLora)

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To fine tune modal using QLoRA

## QLoRA Training Report

### Base Model

TinyLlama/TinyLlama-1.1B-Chat-v1.0

### Fine-Tuning Method

QLoRA (Quantized Low-Rank Adaptation)

## Training Configuration

- Rank (r): 16
- LoRA Alpha: 32
- LoRA Dropout: 0.05
- Learning Rate: 2e-4
- Batch Size: 4
- Epochs: 3
- Optimizer: paged_adamw_8bit
- Precision: FP16
- Quantization: 4-bit (NF4)
- Gradient Checkpointing: Enabled

## Training Results

Epoch-wise Performance:

Epoch 1: - Training Loss: 0.325061 - Validation Loss: 0.290985

Epoch 2: - Training Loss: 0.308284 - Validation Loss: 0.279865

Epoch 3: - Training Loss: 0.288531 - Validation Loss: 0.274536

Final Metrics:

- Global Steps: 570
- Final Training Loss: 0.358517
- Total Epochs Completed: 3
- Train Runtime: 726 seconds
- Train Samples per Second: 3.136
- Train Steps per Second: 0.785

## Observations

- Validation loss consistently decreased across epochs.
- Model successfully adapted to the domain dataset.
- Only \~1% of parameters were trainable (LoRA adapters).
- Training was memory-efficient due to 4-bit quantization.
