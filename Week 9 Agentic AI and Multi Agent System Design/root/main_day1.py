import asyncio

from autogen_ext.models.ollama import OllamaChatCompletionClient

from agents.research_agent import create_research_agent
from agents.summarizer_agent import create_summarizer_agent
from agents.answer_agent import create_answer_agent


async def main():

    model_client = OllamaChatCompletionClient(
        model="mistral"
    )

    research_agent = create_research_agent(model_client)
    summarizer_agent = create_summarizer_agent(model_client)
    answer_agent = create_answer_agent(model_client)

    print("Type 'exit' to stop\n")

    while True:

        query = input("\nAsk a question: ")

        if query.lower() == "exit":
            break

        print("\nResearch Agent Output:\n")

        research_result = await research_agent.run(task=query)
        research_text = research_result.messages[-1].content
        print(research_text)

        print("\nSummarizer Agent Output:\n")

        summary_result = await summarizer_agent.run(task=research_text)
        summary_text = summary_result.messages[-1].content
        print(summary_text)

        print("\nAnswer Agent Output:\n")

        final_result = await answer_agent.run(task=summary_text)
        final_text = final_result.messages[-1].content
        print(final_text)

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())