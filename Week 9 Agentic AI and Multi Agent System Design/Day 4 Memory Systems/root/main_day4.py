import asyncio
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

from transformers import logging
logging.set_verbosity_error()


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
        print("\n" + "=" * 60)
        print("Memory Search")
        print("=" * 60)

        print(f"FAISS Vectors : {self.vector.index.ntotal}")
        print(f"Metadata Size : {len(self.vector.metadata)}")


        similar_memories = self.vector.search(user_input, k=5)

        print("\n" + "-" * 60)
        print("Relevant Memories")
        print("-" * 60)

        if not similar_memories:
            print("No relevant memories found.")
        else:
            for i, m in enumerate(similar_memories, 1):
                print(f"{i}. {m}")

        memory_context = "\n".join(similar_memories) if similar_memories else "None"
        session_context = self.session.get_context()

        prompt = f"""Relevant Past Memory:
                  {memory_context}
                  
                  Current Conversation:
                  {session_context}
                  
                  User Query:
                  {user_input}
                  """

        
        agent_task = asyncio.create_task(self.agent.run(task=prompt))

        
        response = await agent_task
        agent_reply = response.messages[-1].content

       
        self.session.add("user", user_input)
        self.session.add("assistant", agent_reply)

       
        summary_task = asyncio.create_task(
            self.summarizer.summarize(user_input, agent_reply)
        )

        summary = await summary_task

        print("\n" + "-" * 60)
        print("SUMMARY STORED")
        print("-" * 60)
        print(summary)

        
        self.long_term.store(user_input, agent_reply, summary)
        self.vector.add(summary, summary)

        return agent_reply


async def main():
    print("\nInitializing system...")

    orchestrator = MemoryOrchestrator()

    print("System ready.")
    print("\n" + "=" * 60)
    print("Memory-Enhanced Agent Chat")
    print("=" * 60)

    while True:
        user_input = input("\nChat > ")

        if user_input.lower() in ["exit", "quit"]:
            break

        reply = await orchestrator.handle(user_input)

        print("\n" + "-" * 60)
        print("Agent Response")
        print("-" * 60)
        print(reply)


if __name__ == "__main__":
    asyncio.run(main())