from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import config

model = None
tokenizer = None


def load_model():

    global model, tokenizer

    if model is None:

        print("Loading model on CPU...")

        tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)

        model = AutoModelForCausalLM.from_pretrained(
            config.MODEL_NAME,
            dtype=torch.float32
        )

        model.to(config.DEVICE)

        print("Model loaded successfully")

    return model, tokenizer