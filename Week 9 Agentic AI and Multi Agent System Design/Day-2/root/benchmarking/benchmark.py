import time
import statistics
import os
from datetime import datetime
import asyncio

from autogen_ext.models.ollama import OllamaChatCompletionClient

from orchestrator.planner import create_planner_agent
from agents.worker_agent import create_worker_agent
from agents.reflection_agent import create_reflection_agent
from agents.validator import create_validator_agent


RUNS = 3  # keep small for local models


# 🔹 Core pipeline (same as your main.py)
async def _run_pipeline(model_client, query):

    planner = create_planner_agent(model_client)
    worker = create_worker_agent(model_client)
    reflection = create_reflection_agent(model_client)
    validator = create_validator_agent(model_client)

    timings = {}

    # -------- Planner --------
    t1 = time.time()
    plan_result = await planner.run(task=query)
    t2 = time.time()
    timings["planner"] = t2 - t1

    tasks_text = plan_result.messages[-1].content

    tasks = [
        line.split(".", 1)[1].strip()
        for line in tasks_text.split("\n")
        if line.strip() and line[0].isdigit()
    ]

    # -------- Workers --------
    async def run_worker(task):
        result = await worker.run(task=task)
        return result.messages[-1].content

    t3 = time.time()
    worker_outputs = await asyncio.gather(
        *[run_worker(task) for task in tasks]
    )
    t4 = time.time()
    timings["workers"] = t4 - t3

    combined_results = "\n".join(worker_outputs)

    # -------- Reflection --------
    t5 = time.time()
    reflection_result = await reflection.run(task=combined_results)
    reflection_output = reflection_result.messages[-1].content
    t6 = time.time()
    timings["reflection"] = t6 - t5

    # -------- Validator --------
    t7 = time.time()
    final_result = await validator.run(task=reflection_output)
    final_output = final_result.messages[-1].content
    t8 = time.time()
    timings["validator"] = t8 - t7

    timings["total"] = t8 - t1

    return timings, final_output


# 🔹 Benchmark runner
async def run_benchmark(query, model_name):

    model_client = OllamaChatCompletionClient(model=model_name)

    all_timings = []
    outputs = []

    print(f"\n⚡ Running Benchmark for model: {model_name}\n")

    for i in range(RUNS):
        try:
            timings, output = await _run_pipeline(model_client, query)

            print(
                f"Run {i+1}: "
                f"Total={timings['total']:.2f}s | "
                f"P={timings['planner']:.2f}s | "
                f"W={timings['workers']:.2f}s | "
                f"R={timings['reflection']:.2f}s | "
                f"V={timings['validator']:.2f}s"
            )

            all_timings.append(timings)
            outputs.append(output)

        except Exception as e:
            print(f"❌ Error: {e}")

    if not all_timings:
        print("❌ Benchmark failed.")
        return

    report = _generate_report(all_timings, outputs, query, model_name)
    _save_report(report, model_name)

    await model_client.close()

    print("\n📄 Benchmark saved successfully!")


# 🔹 Report generator
def _generate_report(all_timings, outputs, query, model_name):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def avg(key):
        return round(statistics.mean([t[key] for t in all_timings]), 2)

    lines = []
    lines.append("DAY 2 AGENT BENCHMARK REPORT")
    lines.append("=" * 60)

    lines.append(f"Model: {model_name}")
    lines.append(f"Query: {query}")
    lines.append(f"Timestamp: {now}")
    lines.append(f"Runs: {len(all_timings)}\n")

    lines.append("PERFORMANCE")
    lines.append("-" * 60)
    lines.append(f"Total Avg: {avg('total')} sec")
    lines.append(f"Planner Avg: {avg('planner')} sec")
    lines.append(f"Workers Avg: {avg('workers')} sec")
    lines.append(f"Reflection Avg: {avg('reflection')} sec")
    lines.append(f"Validator Avg: {avg('validator')} sec\n")

    lines.append("FINAL OUTPUT SAMPLE")
    lines.append("-" * 60)
    lines.append(outputs[-1])

    lines.append("\n" + "=" * 60)

    return "\n".join(lines)


# 🔹 Save report
def _save_report(report, model_name):
    os.makedirs("benchmark", exist_ok=True)

    safe_model_name = model_name.replace(":", "_").replace("/", "_")

    path = f"benchmarking/benchmark_{safe_model_name}.txt"

    with open(path, "w") as f:
        f.write(report)

    print(f"\n📄 Saved -> {path}")


# 🔹 Entry point
if __name__ == "__main__":
    query = input("Enter benchmark query: ")
    model = input("Enter model (e.g. mistral, phi3, qwen:7b): ")

    asyncio.run(run_benchmark(query, model))