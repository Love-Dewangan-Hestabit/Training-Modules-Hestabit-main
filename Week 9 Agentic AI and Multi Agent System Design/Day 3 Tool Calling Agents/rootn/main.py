import asyncio
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.messages import TextMessage

from config import get_model_client
from agents.planner_agent import get_planner_agent
from agents.file_agent import get_file_agent
from agents.db_agent import get_db_agent
from agents.code_agent import get_code_agent


async def main():
    model = get_model_client()

    planner    = get_planner_agent(model)
    file_agent = get_file_agent(model)
    db_agent   = get_db_agent(model)
    code_agent = get_code_agent(model)

    # Stop when TERMINATE is said OR after 10 messages (safety net)
    stop_condition = TextMentionTermination("TERMINATE") | MaxMessageTermination(10)

    team = SelectorGroupChat(
        participants=[planner, file_agent, db_agent, code_agent],
        model_client=model,
        termination_condition=stop_condition,
    )

    print("Multi-Agent System Ready!\n")

    while True:
        task = input("You: ").strip()
        if task.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        if not task:
            continue

        try:
            async for message in team.run_stream(task=task):
                if isinstance(message, TextMessage):
                    print(f"\n[{message.source}]: {message.content}\n")

        except RuntimeError as e:
            # Catch tool call failures gracefully without crashing
            print(f"\n[System Error]: {e}")
            print("[System]: The agent encountered a tool call error. Please try rephrasing your request.\n")

        except Exception as e:
            print(f"\n[Unexpected Error]: {e}\n")

        finally:
            # Always reset team state between tasks
            await team.reset()


asyncio.run(main())