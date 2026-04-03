"""
NEXUS AI — Entry Point
Run: python main.py
"""

import asyncio
import os
import sys
from dotenv import load_dotenv

load_dotenv()

from orchestrator.orchestrator import NexusOrchestrator


BANNER = """
--------------------------------------------------------
|                  N E X U S   A I                     |
|      Autonomous Multi-Agent Intelligence System      |
|  Type 'exit' or 'quit' to stop  |  Ctrl+C to abort   |
--------------------------------------------------------
"""

async def main():
    print(BANNER)

    try:
        orchestrator = NexusOrchestrator()
    except EnvironmentError as e:
        print(f"\n[ERROR] Setup error: {e}")
        sys.exit(1)

    vec_count = orchestrator.vector_store.count()
    lt_count  = orchestrator.long_term.count()
    print(f"\n[MEMORY] Memory Status:")
    print(f"   Vector store entries : {vec_count}")
    print(f"   Long-term memories   : {lt_count}")
    print("\n[READY] NEXUS AI READY — Awaiting your task...\n")

    while True:
        try:
            user_input = input("YOU: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit", "bye"}:
                print("\n[EXIT] Goodbye! NEXUS AI shutting down.")
                break

            result = await orchestrator.run(user_input)

            print("\n" + "═" * 60)
            print("[FINAL] NEXUS AI FINAL RESPONSE:")
            print("═" * 60)
            print(f"[TASK] Task: {user_input}")
            print("─" * 60)
            print(result)
            print("─" * 60)
            print(f"[STATS] Memory: {orchestrator.vector_store.count()} vectors | "
                  f"{orchestrator.long_term.count()} long-term | "
                  f"{orchestrator.session_memory.size()} session msgs")
            print("═" * 60 + "\n")

        except KeyboardInterrupt:
            print("\n\n[WARN] Interrupted. Exiting NEXUS AI.")
            break

        except ValueError as e:
            print(f"\n[ERROR] Planning error: {e}")
            print("Please rephrase your task and try again.\n")

        except Exception as e:
            print(f"\n[ERROR] Unexpected error: {e}")
            print("Check logs/nexus.log for details.\n")


if __name__ == "__main__":
    asyncio.run(main())