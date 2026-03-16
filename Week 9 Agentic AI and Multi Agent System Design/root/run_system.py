import asyncio

from autogen_ext.models.ollama import OllamaChatCompletionClient

from orchestrator.planner import create_planner_agent
from agents.worker_agent import create_worker_agent
from agents.reflection_agent import create_reflection_agent
from agents.validator import create_validator_agent


async def main():

    model_client = OllamaChatCompletionClient(
        model="mistral"
    )

    planner = create_planner_agent(model_client)
    worker = create_worker_agent(model_client)
    reflection = create_reflection_agent(model_client)
    validator = create_validator_agent(model_client)

    query = input("Ask a question: ")

    print("\n--- PLANNER OUTPUT ---\n")

    plan_result = await planner.run(task=query)

    tasks_text = plan_result.messages[-1].content
    print(tasks_text)

    tasks = [line for line in tasks_text.split("\n") if line.strip()]

    print("\n--- EXECUTION TREE ---")
    print("Planner")
    for i, task in enumerate(tasks):
        print(f"  ├─ Worker {i+1} → {task}")

    print("\n--- WORKER OUTPUTS ---\n")

    async def run_worker(task):
        result = await worker.run(task=task)
        return result.messages[-1].content

    worker_outputs = await asyncio.gather(
        *[run_worker(task) for task in tasks]
    )

    for i, output in enumerate(worker_outputs):
        print(f"\nWorker {i+1} Result:\n{output}")

    combined_results = "\n".join(worker_outputs)

    print("\n--- REFLECTION AGENT ---\n")

    reflection_result = await reflection.run(task=combined_results)
    reflection_output = reflection_result.messages[-1].content
    print(reflection_output)

    print("\n--- VALIDATOR AGENT ---\n")

    final_result = await validator.run(task=reflection_output)
    final_answer = final_result.messages[-1].content

    print("\n--- FINAL ANSWER ---\n")
    print(final_answer)

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())