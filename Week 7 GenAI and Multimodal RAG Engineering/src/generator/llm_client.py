import os
import yaml
from pathlib import Path
from google import genai


class LLMClient:
    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config" / "model.yaml"

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        api_key = os.getenv(config["api_key_env"])
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found. Please set environment variable.")

        self.client = genai.Client(api_key=api_key)
        self.model_name = config["model_name"]

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config={"temperature": 0.1}
        )

        return response.text.strip()