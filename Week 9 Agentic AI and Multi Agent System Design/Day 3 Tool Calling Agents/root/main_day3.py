import asyncio
import json
import re

from config import get_model_client
from tools.code_executor import CodeExecutorAgent
from tools.file_agent import FileAgent
from tools.db_agent import DBAgent
from autogen_agentchat.agents import AssistantAgent


class Orchestrator:
    def __init__(self):
        self.model_client = get_model_client()

        self.planner = AssistantAgent(
            name="planner",
            model_client=self.model_client,
            system_message="""
            You are a smart planner.
            
            At each step decide NEXT ACTION.
            
            Return ONLY JSON:
            {
              "action": "file | db | code | finish"
            }
            
            RULES:
            - Think step by step
            - Use previous outputs
            - You can reuse tools multiple times
            - When task is complete → action = "finish"
            - No explanation outside JSON
            """
        )

        self.file_agent = FileAgent(self.model_client)
        self.db_agent = DBAgent(self.model_client)
        self.code_agent = CodeExecutorAgent(self.model_client)

    async def run(self, query: str):

        print("\n[USER QUERY]:", query)

        context = f"User Query:\n{query}\n"

 
        agent_flow = ["planner"]

        step = 0
        max_steps = 10

        while step < max_steps:
            step += 1
            print(f"\n--- STEP {step} ---")

  
            plan_response = await self.planner.run(task=context)
            raw = plan_response.messages[-1].content

            print("\n[PLANNER RAW]\n", raw)

            try:
                decision = json.loads(re.sub(r"```json|```", "", raw).strip())
                action = decision.get("action", "finish")
            except:
                action = "finish"

            print("[Next Action]:", action)

  
            if action == "finish":
                agent_flow.append("finish")
                break


            elif action == "file":
                agent_flow.append("file_agent")
                result = await self.file_agent.execute(context)
                context += f"\nFILE OUTPUT\n{result}\n"

     
            elif action == "db":
                agent_flow.append("db_agent")
                result = await self.db_agent.execute(query, "data/sales.csv")
                context += f"\nDB OUTPUT\n{result}\n"

   
            elif action == "code":
                agent_flow.append("code_agent")
                result = await self.code_agent.execute(context)
                context += f"\nCODE OUTPUT\n{result}\n"

      
        print("\nAgent Workflow:\n")
        print(" -> ".join(agent_flow))



        final_agent = AssistantAgent(
            name="final_agent",
            model_client=self.model_client,
            system_message="""
            Only summarize given outputs.
            Do NOT hallucinate.
            """
        )

        final = await final_agent.run(
            task=f"""
            User Query:
            {query}
            
            Tool Outputs:
            {context}
            
            Provide final answer.
            """
        )

        return final.messages[-1].content



if __name__ == "__main__":

    async def main():
        orch = Orchestrator()

        print("\nDynamic Multi-Agent System Started\n")

        while True:
            query = input("Enter your query: ")

            if query.lower() in ["exit", "quit"]:
                break

            try:
                result = await orch.run(query)

                print("\nFinal Answer\n")
                
                print(result)
                print("\n")

            except Exception as e:
                print(f"\nError: {str(e)}\n")

    asyncio.run(main())