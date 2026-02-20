import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import numpy as np


class CLIPEmbedder:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        ).to(self.device)

        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

        self.model.eval()

    def embed_image(self, image_path):
        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        pixel_values = inputs["pixel_values"].to(self.device)

        with torch.no_grad():
            vision_outputs = self.model.vision_model(
                pixel_values=pixel_values
            )

            pooled_output = vision_outputs.pooler_output

            image_features = self.model.visual_projection(
                pooled_output
            )

        image_features = torch.nn.functional.normalize(
            image_features,
            p=2,
            dim=-1
        )

        return image_features.cpu().numpy()

    def embed_text(self, text):
        inputs = self.processor(
            text=[text],
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        input_ids = inputs["input_ids"].to(self.device)
        attention_mask = inputs["attention_mask"].to(self.device)

        with torch.no_grad():
            text_outputs = self.model.text_model(
                input_ids=input_ids,
                attention_mask=attention_mask
            )

            pooled_output = text_outputs.pooler_output

            text_features = self.model.text_projection(
                pooled_output
            )

        text_features = torch.nn.functional.normalize(
            text_features,
            p=2,
            dim=-1
        )

        return text_features.cpu().numpy()