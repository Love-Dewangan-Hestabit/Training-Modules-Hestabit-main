from autogen_agentchat.agents import AssistantAgent


class MemorySummarizer:
    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="memory_summarizer",
            model_client=model_client,
            system_message="""
            Summarize the conversation into a concise factual memory.
            
            Focus on:
            - User's intent
            - Key facts
            - Preferences
            
            Return only summary.
            """
        )

    async def summarize(self, user_input, agent_response):
        prompt = f"""
                  User: {user_input}
                  Agent: {agent_response}
                  """
        response = await self.agent.run(task=prompt)
        return response.messages[-1].content.strip()