import asyncio

from config import get_model_client

from memory.session_memory import SessionMemory
from memory.long_term_store import LongTermMemory
from memory.vector_store import VectorStore
from memory.summarizer import MemorySummarizer

from autogen_agentchat.agents import AssistantAgent


class MemoryOrchestrator:
    def __init__(self):
        self.model_client = get_model_client()

        self.session = SessionMemory()
        self.long_term = LongTermMemory()
        self.vector = VectorStore()
        self.summarizer = MemorySummarizer(self.model_client)

        self.agent = AssistantAgent(
            name="main_agent",
            model_client=self.model_client,
            system_message="""
You are a helpful AI assistant with memory.

Use provided memory if relevant.
If no memory available, answer normally.
"""
        )

    async def handle(self, user_input):
        print("\n🔍 Searching memory...")

        # 🔥 DEBUG INFO
        print(f"FAISS vectors: {self.vector.index.ntotal}")
        print(f"Metadata size: {len(self.vector.metadata)}")

        # 1. VECTOR SEARCH
        similar_memories = self.vector.search(user_input, k=5)

        print("\n📌 Similar Memories Found:")
        for m in similar_memories:
            print("-", m)

        memory_context = "\n".join(similar_memories) if similar_memories else "None"

        # 2. SESSION CONTEXT
        session_context = self.session.get_context()

        # 3. BUILD PROMPT
        prompt = f"""
Relevant Past Memory:
{memory_context}

Current Conversation:
{session_context}

User Query:
{user_input}
"""

        # 4. GENERATE RESPONSE
        response = await self.agent.run(task=prompt)
        agent_reply = response.messages[-1].content

        # 5. UPDATE SESSION
        self.session.add("user", user_input)
        self.session.add("assistant", agent_reply)

        # 6. SUMMARIZE
        summary = await self.summarizer.summarize(user_input, agent_reply)

        print("\n🧠 Summary:", summary)

        # 7. STORE LONG-TERM
        self.long_term.store(user_input, agent_reply, summary)

        # 8. STORE VECTOR
        self.vector.add(summary, summary)

        return agent_reply


async def main():
    orchestrator = MemoryOrchestrator()

    while True:
        user_input = input("\n🧑 You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        reply = await orchestrator.handle(user_input)
        print(f"\n🤖 Agent: {reply}")


if __name__ == "__main__":
    asyncio.run(main())