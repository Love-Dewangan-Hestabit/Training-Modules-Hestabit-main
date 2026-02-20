# Week 7 (Day 3) - Image Rag (Multimodal Rag)

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To build an Image RAG pipeline where the system generated OCR Text, CLIP embeddings, Captions through BLIP.

## Architecture Flow

### Ingestion Pipeline

- OCR through pytesseract
- Image Captioning through BLIP
- Image Embedding through CLIP
- Store Embedding in FAISS

### Retrieval Pipeline

```
                    User Query (Text or Image)
                               |
                               V
                    Convert to CLIP Embedding
                               |
                               V
                    Search FAISS Vector Index
                               |
                               V
                    Compute OCR BM25 Score
                               |
                               V
                Hybrid Scoring (0.6 CLIP + 0.4 OCR)
                               |
                               V
                          Rank Results
                               |
                               V
                  Return Image + Caption + OCR
```

## Components

### CLIP(Contrastive Language Image Pretraining)

I have used CLIP for embedding Image and Text into vectors as it maps both into same embedding space

### BLIP(Bootstrapping Language Image Pretraining)

It generates caption of the image in natural language, which helps in improving the explainability.

### OCR(Optical Character Recognition)

I have used OCR for extracting text inside images, which are crucial in analyzing diagrams and charts.

### FAISS (Vector Database)

I used FAISS for storing the image embeddings, this also perform search through nearest neighbor detection.

## Hybrid Ranking Formula

Hybrid Score = 0.6 × CLIP Similarity - 0.4 × OCR BM25 Score

This ensures:

- Visual similarity matters
- Keyword match matters
- Diagrams rank correctly
- Natural images still work

## Supported Query Modes

### Text → Image

### Image → Image

### Image → Text

## Why Multimodal RAG?

Traditional RAG handles only text.

Here I have used Multimodal RAGs to understand images, extract embedded text inside image.

## Output files

text_to_image_results.txt
image_to_image_results.txt
image_to_text_results.txt
