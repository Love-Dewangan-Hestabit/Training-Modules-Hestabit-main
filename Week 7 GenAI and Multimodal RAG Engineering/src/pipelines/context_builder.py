import tiktoken

MAX_TOKENS = 1500

class ContextBuilder:
    def __init__(self):
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def build_context(self, documents):
        context = ""
        total_tokens = 0

        for i, doc in enumerate(documents):
            text = doc["text"]
            metadata = doc["metadata"]

            chunk_text = f"""
Source {i+1}:
File: {metadata.get('source')}
Chunk ID: {metadata.get('chunk_id')}
-----------------------------------
{text}
"""

            tokens = len(self.tokenizer.encode(chunk_text))

            if total_tokens + tokens > MAX_TOKENS:
                break

            context += chunk_text
            total_tokens += tokens

        return context
