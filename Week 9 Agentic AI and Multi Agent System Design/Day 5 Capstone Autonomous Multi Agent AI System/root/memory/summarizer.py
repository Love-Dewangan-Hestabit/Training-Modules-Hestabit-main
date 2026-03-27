
import json
import re

from autogen_agentchat.agents import AssistantAgent


class MemorySummarizer:
    def __init__(self, model_client):
        self.agent = AssistantAgent(
            name="memory_summarizer",
            model_client=model_client,
            system_message="""
You are a Memory Summarizer for an AI multi-agent system.

Given a user task and the agent's response, produce:
1. A concise factual summary (max 2 sentences) capturing the key intent and outcome.
2. An importance score from 1-10.

IMPORTANCE SCORING GUIDE:
- 8-10: User preferences, names, system correction rules, and core project architecture decisions (e.g., "My name is Love", "Always use Python 3.12").
- 5-7:  High-level summaries of completed tasks or key insights (e.g., "Successfully planned the MedAI startup", "Analyzed CSV and found 3 key metrics").
- 1-4:  Raw code execution logs, intermediate task steps, large data outputs, tool usage details, and trivial small talk.

Return ONLY this raw JSON (no markdown, no explanation):
{"summary": "...", "importance": 7}
""",
        )

    async def summarize(self, user_task: str, agent_response: str) -> dict:
        """
        Returns {"summary": str, "importance": int}.
        Falls back to importance=5 if parsing fails.
        """
        prompt = f"User Task: {user_task}\nAgent Response: {agent_response[:1500]}"

        try:
            response = await self.agent.run(task=prompt)
            raw = response.messages[-1].content.strip()

            cleaned = re.sub(r"```json\s*|```\s*", "", raw).strip()
            data = json.loads(cleaned)

            return {
                "summary": str(data.get("summary", user_task[:200])),
                "importance": int(data.get("importance", 5)),
            }
        except Exception:
        
            return {
                "summary": f"User asked: {user_task[:150]}",
                "importance": 5,
            }
