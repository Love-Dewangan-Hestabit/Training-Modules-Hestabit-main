import time
import statistics
import os
from datetime import datetime

from agents.research_agent import create_research_agent
from agents.summarizer_agent import create_summarizer_agent
from agents.answer_agent import create_answer_agent


RUNS = 3   # keep small for real-time



async def _run_pipeline(model_client, query):
    research_agent = create_research_agent(model_client)
    summarizer_agent = create_summarizer_agent(model_client)
    answer_agent = create_answer_agent(model_client)

    timings = {}

    # Research
    t1 = time.time()
    r = await research_agent.run(task=query)
    t2 = time.time()
    timings["research"] = t2 - t1

    # Summarizer
    t3 = time.time()
    s = await summarizer_agent.run(task=r.messages[-1].content)
    t4 = time.time()
    timings["summary"] = t4 - t3

    # Answer
    t5 = time.time()
    a = await answer_agent.run(task=s.messages[-1].content)
    t6 = time.time()
    timings["answer"] = t6 - t5

    timings["total"] = t6 - t1

    return timings, a.messages[-1].content


async def run_benchmark_for_query(model_client, query, model_name):
    all_timings = []
    outputs = []

    print("\n⚡ Running Benchmark for this query...\n")

    for i in range(RUNS):
        try:
            timings, output = await _run_pipeline(model_client, query)

            print(
                f"Run {i+1}: "
                f"Total={timings['total']:.2f}s | "
                f"R={timings['research']:.2f}s | "
                f"S={timings['summary']:.2f}s | "
                f"A={timings['answer']:.2f}s"
            )

            all_timings.append(timings)
            outputs.append(output)

        except Exception as e:
            print(f"❌ Benchmark error: {e}")

    if not all_timings:
        print("❌ Benchmark failed.")
        return

    report = _generate_report(all_timings, outputs, query, model_name)

    _save_report(report, model_name)

    print("\n📄 Benchmark saved successfully!")



def _generate_report(all_timings, outputs, query, model_name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def avg(key):
        return round(statistics.mean([t[key] for t in all_timings]), 2)

    lines = []
    lines.append("AGENT BENCHMARK REPORT")
    lines.append("=" * 60)

    lines.append(f"Model: {model_name}")
    lines.append(f"Query: {query}")
    lines.append(f"Timestamp: {now}")
    lines.append(f"Runs: {len(all_timings)}\n")

    lines.append("PERFORMANCE")
    lines.append("-" * 60)
    lines.append(f"Total Avg: {avg('total')} sec")
    lines.append(f"Research Avg: {avg('research')} sec")
    lines.append(f"Summary Avg: {avg('summary')} sec")
    lines.append(f"Answer Avg: {avg('answer')} sec\n")

    lines.append("SAMPLE OUTPUT")
    lines.append("-" * 60)
    lines.append(outputs[-1])

    lines.append("\n" + "=" * 60)

    return "\n".join(lines)



def _save_report(report, model_name):
    os.makedirs("benchmark", exist_ok=True)

    safe_model_name = model_name.replace(" ", "_").replace("/", "_")

    path = f"benchmark/benchmark_{safe_model_name}.txt"

    with open(path, "w") as f:
        f.write(report)

    print(f"\n📄 Benchmark saved -> {path}")