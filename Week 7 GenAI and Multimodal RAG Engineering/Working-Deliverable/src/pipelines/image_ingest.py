import os
import json
import faiss
import pytesseract
import numpy as np
from PIL import Image
from tqdm import tqdm
from transformers import BlipProcessor, BlipForConditionalGeneration
from embeddings.clip_embedder import CLIPEmbedder
from pdf2image import convert_from_path


IMAGE_FOLDER = "data/images"
INDEX_PATH = "vectorstore/image_index.faiss"
METADATA_PATH = "vectorstore/image_metadata.json"


class ImageIngestor:
    def __init__(self):
        self.embedder = CLIPEmbedder()
        self.blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.blip_model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        self.embeddings = []
        self.metadata = []

    def extract_ocr(self, image_path):
        image = Image.open(image_path)
        return pytesseract.image_to_string(image)

    def generate_caption(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.blip_processor(images=image, return_tensors="pt")
        output = self.blip_model.generate(**inputs)
        caption = self.blip_processor.decode(output[0], skip_special_tokens=True)
        return caption

    def process_pdf(self, pdf_path):
        images = convert_from_path(pdf_path)
        paths = []

        for i, img in enumerate(images):
            path = pdf_path.replace(".pdf", f"_page_{i}.jpg")
            img.save(path)
            paths.append(path)

        return paths

    def ingest(self):
        files = os.listdir(IMAGE_FOLDER)

        for file in tqdm(files):
            path = os.path.join(IMAGE_FOLDER, file)

            if file.endswith(".pdf"):
                paths = self.process_pdf(path)
            else:
                paths = [path]

            for img_path in paths:
                embedding = self.embedder.embed_image(img_path)

                ocr_text = self.extract_ocr(img_path)
                caption = self.generate_caption(img_path)

                self.embeddings.append(embedding[0])

                self.metadata.append({
                    "image_path": img_path,
                    "ocr_text": ocr_text,
                    "caption": caption
                })

        self.build_index()

    def build_index(self):
        embeddings = np.array(self.embeddings).astype("float32")
        dimension = embeddings.shape[1]

        index = faiss.IndexFlatIP(dimension)
        index.add(embeddings)

        faiss.write_index(index, INDEX_PATH)

        with open(METADATA_PATH, "w") as f:
            json.dump(self.metadata, f, indent=2)

        print("Image index built successfully.")


if __name__ == "__main__":
    ingestor = ImageIngestor()
    ingestor.ingest()