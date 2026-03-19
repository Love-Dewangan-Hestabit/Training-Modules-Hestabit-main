import os
from autogen_ext.models.openai import OpenAIChatCompletionClient


def get_model_client():
    api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("API key not found. Set GROQ_API_KEY or OPENAI_API_KEY")

    return OpenAIChatCompletionClient(
        model="llama-3.3-70b-versatile",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,  # ✅ FIXED warning
            "family": "llama3",
        }
    )