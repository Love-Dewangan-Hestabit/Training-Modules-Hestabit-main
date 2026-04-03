import os
from dotenv import load_dotenv
from autogen_ext.models.ollama import OllamaChatCompletionClient

load_dotenv()


def get_model_client():
    return OllamaChatCompletionClient(
        model="qwen:7b"

    )

