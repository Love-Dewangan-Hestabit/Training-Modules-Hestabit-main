import json
import logging
import re

from config import get_model_client

# existing agents
from agents.research_agent import create_research_agent
from agents.summarizer_agent import create_summarizer_agent
from agents.answer_agent import create_answer_agent
from agents.reflection_agent import create_reflection_agent
from agents.validator import create_validator_agent

# new agents
from agents.planner_agent import create_planner_agent
from agents.analyst_agent import create_analyst_agent
from agents.critic_agent import create_critic_agent
from agents.optimizer_agent import create_optimizer_agent
from agents.reporter_agent import create_reporter_agent

from tools.code_executor import CodeExecutorAgent

from memory.session_memory import SessionMemory
from memory.long_term_store import LongTermMemory


logging.basicConfig(
    filename="logs/nexus.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


class NexusOrchestrator:

    def __init__(self):

        self.model_client = get_model_client()

        # Memory
        self.session_memory = SessionMemory()
        self.long_memory = LongTermMemory()

        # Agents
        self.planner = create_planner_agent(self.model_client)

        self.agents = {
            "research_agent": create_research_agent(self.model_client),
            "summarizer_agent": create_summarizer_agent(self.model_client),
            "answer_agent": create_answer_agent(self.model_client),
            "reflection_agent": create_reflection_agent(self.model_client),
            "validator_agent": create_validator_agent(self.model_client),
            "analyst_agent": create_analyst_agent(self.model_client),
            "critic_agent": create_critic_agent(self.model_client),
            "optimizer_agent": create_optimizer_agent(self.model_client),
            "reporter_agent": create_reporter_agent(self.model_client),
        }

        self.code_executor = CodeExecutorAgent(self.model_client)

    async def run(self, user_input):

        print("\nUSER:", user_input)

        # STEP 1: PLANNING
        plan_response = await self.planner.run(task=user_input)
        raw_output = plan_response.messages[-1].content

        print("\n[PLANNER RAW OUTPUT]\n", raw_output)
        
        # Extract JSON safely
        match = re.search(r"\{.*\}", raw_output, re.        DOTALL)
        
        if not match:
            raise ValueError("Planner did not return         JSON")
        
        plan = json.loads(match.group())
        results = []

        # STEP 2: EXECUTION LOOP
        for step in plan["steps"]:

            agent_name = step["agent"]
            task = step["task"]

            print(f"\n[{agent_name.upper()}] → {task}")

            try:
                if agent_name == "code_agent":
                    output = await self.code_executor.execute(task)
                else:
                    agent = self.agents[agent_name]
                    response = await agent.run(task=task)
                    output = response.messages[-1].content

                print("OUTPUT:", output)

                # Logging
                logging.info(f"{agent_name}: {output}")

                # Memory
                self.session_memory.add(output)
                self.long_memory.store(output)

                results.append(output)

            except Exception as e:
                logging.error(f"ERROR in {agent_name}: {str(e)}")
                results.append(f"Error: {str(e)}")

        # STEP 3: SELF-REFLECTION
        critic = await self.agents["critic_agent"].run(task=str(results))
        optimized = await self.agents["optimizer_agent"].run(
            task=critic.messages[-1].content
        )

        # STEP 4: VALIDATION
        validated = await self.agents["validator_agent"].run(
            task=optimized.messages[-1].content
        )

        # STEP 5: REPORTING
        final = await self.agents["reporter_agent"].run(
            task=validated.messages[-1].content
        )

        return final.messages[-1].content