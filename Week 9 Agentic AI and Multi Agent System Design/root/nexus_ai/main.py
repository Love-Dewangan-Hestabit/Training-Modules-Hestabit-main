import asyncio
from orchestrator.nexus_orchestrator import NexusOrchestrator


async def main():

    nexus = NexusOrchestrator()

    while True:
        task = input("\nEnter Task: ")

        result = await nexus.run(task)

        print("\nFINAL RESULT:\n")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())