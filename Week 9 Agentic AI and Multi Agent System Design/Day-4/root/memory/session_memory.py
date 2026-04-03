class SessionMemory:
    def __init__(self, max_messages=10):
        self.messages = []
        self.max_messages = max_messages

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_context(self):
        return self.messages

    def clear(self):
        self.messages = []
