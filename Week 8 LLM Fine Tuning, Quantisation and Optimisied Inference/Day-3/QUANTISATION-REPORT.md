# Week 8 (Day 3) - QUANTISATION (8-bit -> 4-bit -> GGUF)

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To convert the base model from FP16 precision to more memory-efficient formats, it was first loaded as a baseline and then quantized to INT8 and INT4 (NF4) using bitsandbytes. After that, the model was converted to GGUF format using llama.cpp to enable optimized CPU inference. Finally, benchmarking was performed to compare model size, inference speed, and output quality across all formats in order to understand the memory accuracy.

## Model Used

TinyLlama-1.1B-Chat-v1.0

## Quantisation Results

```

  Format   Size (GB)   Speed (s)    Quality
  -------- ----------- ------------ -------------
  FP16     2.20        0.05         Best
  INT8     1.10        0.14         Very Good
  INT4     0.60        0.09         Slight Drop
  GGUF     0.60        1.80 (CPU)   Slight Drop
```

## Deliverables Submitted

- /quantized/model-int8
- /quantized/model-int4
- /quantized/model.gguf
- QUANTISATION-REPORT.md
