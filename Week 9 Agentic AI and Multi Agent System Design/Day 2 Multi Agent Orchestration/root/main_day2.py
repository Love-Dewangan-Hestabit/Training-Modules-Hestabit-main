import asyncio
import os

from autogen_ext.models.openai import OpenAIChatCompletionClient

from orchestrator.planner import create_planner_agent
from agents.worker_agent import create_worker_agent
from agents.reflection_agent import create_reflection_agent
from agents.validator import create_validator_agent


async def main():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not set")

    model_client = OpenAIChatCompletionClient(
        model="llama-3.3-70b-versatile",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",

     
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": "llama3",
        }
    )

    print("Using GROQ")
    print("Endpoint:", "https://api.groq.com/openai/v1")

   
    planner = create_planner_agent(model_client)
    worker = create_worker_agent(model_client)
    reflection = create_reflection_agent(model_client)
    validator = create_validator_agent(model_client)

    while True:
        query = input("\nAsk a question (type 'exit' to quit): ")
    
       
        if query.lower().strip() in ["exit", "quit"]:
            break
    
        print("\n[PLANNER OUTPUT]\n")
    
        
        plan_result = await planner.run(task=query)
        tasks_text = plan_result.messages[-1].content
        print(tasks_text)
    
        
        tasks = [
            line.split(".", 1)[1].strip()
            for line in tasks_text.split("\n")
            if line.strip() and line[0].isdigit()
        ]
    
        print("\n[EXECUTION TREE]\n")
        print("Planner")
        for i, task in enumerate(tasks):
            print(f"- Worker {i+1} -> {task}")
    
        print("\n[WORKER OUTPUTS]")
    
       
        async def run_worker(task):
            result = await worker.run(task=task)
            return result.messages[-1].content
    
        worker_outputs = await asyncio.gather(
            *[run_worker(task) for task in tasks]
        )
    
        for i, output in enumerate(worker_outputs):
            print(f"\nWorker {i+1} Output:\n{output}")
    
        
        combined_results = "\n".join(worker_outputs)
    
        print("\n[REFLECTION AGENT]\n")
    
      
        reflection_result = await reflection.run(task=combined_results)
        reflection_output = reflection_result.messages[-1].content
        print(reflection_output)
    
        print("\n[VALIDATOR AGENT]\n")
    
        final_result = await validator.run(task=reflection_output)
        final_answer = final_result.messages[-1].content
    
      
        if final_answer.strip() == reflection_output.strip():
            print("Validator made No changes")
        else:
            print("Validator Improved the answer")
    
        print("\n[VALIDATOR OUTPUT]\n")
        print(final_answer)
    
        print("\n[FINAL ANSWER]\n")
        print(final_answer)

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())