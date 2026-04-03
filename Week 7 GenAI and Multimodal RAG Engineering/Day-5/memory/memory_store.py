import json
import os
from datetime import datetime

MEMORY_FILE = "logs/CHAT-LOGS.json"
MAX_HISTORY = 5


class MemoryStore:
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump([], f)

    def load_memory(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def save_interaction(self, question, answer, metadata=None):
        history = self.load_memory()

        history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "question": question,
            "answer": answer,
            "metadata": metadata or {}
        })

        history = history[-MAX_HISTORY:]

        with open(MEMORY_FILE, "w") as f:
            json.dump(history, f, indent=2)

    def get_recent_context(self):
        history = self.load_memory()
        context = ""
        for item in history:
            context += f"\nUser: {item['question']}\nAssistant: {item['answer']}\n"
        return context