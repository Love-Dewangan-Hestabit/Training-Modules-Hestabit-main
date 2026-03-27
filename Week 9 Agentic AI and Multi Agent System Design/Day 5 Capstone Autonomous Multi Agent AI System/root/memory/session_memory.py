
from datetime import datetime


class SessionMemory:
    def __init__(self, max_messages: int = 20):
        self.messages: list[dict] = []
        self.max_messages = max_messages

    def add(self, role: str, content: str) -> None:
        """Add a message to the session buffer."""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        })
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_context(self) -> list[dict]:
        """Return raw message list (for prompt injection)."""
        return self.messages

    def get_formatted(self) -> str:
        """Return a human-readable string of the session history."""
        if not self.messages:
            return "No session history yet."
        lines = []
        for msg in self.messages:
            role = msg["role"].upper()
            lines.append(f"[{role}] {msg['content']}")
        return "\n".join(lines)

    def size(self) -> int:
        return len(self.messages)

    def clear(self) -> None:
        self.messages = []
