# Week 9 (Day 5) - Capstone: Autonomous Multi-Agent AI System

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## NEXUS AI - Autonomous Multi-Agent Capstone

**NEXUS AI** is a cutting-edge, autonomous multi-agent system designed to handle complex, multi-step tasks through intelligent planning, reasoning, and tool execution. Built on the **AutoGen AgentChat** framework, it features a sophisticated pipeline of specialized agents and integrated memory systems.

## Key Features

- **Autonomous Orchestration**: A central `NexusOrchestrator` manages the entire lifecycle of a task.
- **Dynamic Planning**: Automatically decomposes complex queries into actionable steps.
- **Multi-Agent Pipeline**:
  - **Research Agent**: Gathers initial information.
  - **Analyst Agent**: Generates core content and reasoning.
  - **Critic Agent**: Identifies flaws and potential improvements.
  - **Optimizer Agent**: Refines clarity and flow.
  - **Validator Agent**: Ensures technical correctness and safety.
  - **Reporter Agent**: Formats the final output for the user.
- **Integrated Tool Suite**:
  - **File Agent**: Managed read/write operations for `.txt` and `.csv`.
  - **Database Agent**: Natural language to SQL conversion for data analysis.
  - **Code Executor**: Secure Python environment for computational tasks.
- **Advanced Memory Layer**:
  - **Session Memory**: Maintains short-term conversation context.
  - **Long-Term Memory**: Persists knowledge across sessions.
  - **Vector Search**: Semantic retrieval using FAISS for efficient context injection.
- **Professional Dashboard**: A real-time Streamlit interface with pipeline visualization and file management.

## System Architecture

NEXUS AI operates on a feedback-driven execution loop:

```
graph TD
    User([User Input]) --> Planner[Planner Agent]
    Planner --> Loop{Execution Loop}
    Loop --> Research[Research Agent]
    Loop --> Analyst[Analyst Agent]
    Loop --> Critic[Critic Agent]
    Loop --> Optimizer[Optimizer Agent]
    Loop --> Validator[Validator Agent]
    Validator -- "If Invalid" --> Loop
    Validator -- "If Valid" --> Reporter[Reporter Agent]
    Reporter --> Final([Final Output])
```

## Setup & Installation

### Prerequisites

- Python 3.10+
- Groq API Key (Llama 3.3 70B recommended)

### Installation

```
Navigate to the root folder
cd root

Create and activate virtual environment
python -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the `root` directory:

```env
GROQ_API_KEY=your_api_key_here
```

## Usage

To launch the NEXUS AI Command Center:

```
streamlit run app.py
```

1.  **Enter Task**: Input your complex query (e.g., "Analyze sales.csv and write a summary to report.txt").
2.  **Monitor Pipeline**: Watch specialized agents collaborate in real-time.
3.  **Download Results**: Review and download any generated files directly from the UI.
