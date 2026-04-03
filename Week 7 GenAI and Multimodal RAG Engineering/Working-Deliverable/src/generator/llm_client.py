import os
import yaml
from pathlib import Path
from groq import Groq


class LLMClient:
    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config" / "model.yaml"

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        api_key = os.getenv(config["api_key_env"])
        if not api_key:
            raise ValueError("GROQ_API_KEY not found.")

        self.client = Groq(api_key=api_key)
        self.model_name = config["model_name"]

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a precise AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )

        return response.choices[0].message.content.strip()