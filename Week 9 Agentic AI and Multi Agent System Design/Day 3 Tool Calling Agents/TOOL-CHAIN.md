# Week 9 (Day 3) - Tool Calling Agents (Code, Files, Database, Search)

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To implement a **dynamic multi-agent system** using AutoGen
where an orchestrator intelligently decides which tool/agent to use
step-by-step.

## Agents

### Planner Agent

- Decides next action dynamically
- Outputs JSON:

```json
{ "action": "file | db | code | finish" }
```

### File Agent

- Handles file read/write
- Works with `.txt`, `.csv`
- Returns structured JSON actions

### DB Agent

- Converts queries → SQL
- Runs on SQLite (in-memory)
- Uses CSV as table

### Code Executor Agent

- Executes Python code
- Uses only standard libraries
- Writes outputs to `/data`

## Workflow

1.  User gives query
2.  Planner decides next step
3.  Corresponding agent executes
4.  Output is appended to context
5.  Loop continues until `"finish"`

## Example Flow

    planner -> file_agent -> code_agent -> code_agent -> finish

## Run

```bash
python day3.py
```

---

## Key Features

- Dynamic tool selection
- Multi-step reasoning loop
- Context-aware execution
- Agent workflow tracing
