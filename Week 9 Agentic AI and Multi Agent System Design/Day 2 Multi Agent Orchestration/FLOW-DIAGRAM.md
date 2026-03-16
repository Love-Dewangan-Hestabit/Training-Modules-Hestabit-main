# Week 9 (Day 2) - MULTI-AGENT ORCHESTRATION

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Architecture

```
                 User Query
                     |
                     V
            Planner / Orchestrator
                     |
                     V
             Task Decomposition
                     |
                     V
           Parallel Worker Agents
                     |
                     V
             Reflection Agent
                     |
                     V
             Validator Agent
                     |
                     V
                Final Answer
```

## Execution Tree Example

User: Explain the impact of AI in healthcare and finance

```
Planner
├─ Worker 1 → Research AI in healthcare
├─ Worker 2 → Research AI in finance
└─ Worker 3 → Compare both industries
```

```
                        Workers Output
                               |
                               V
                  Reflection Agent (improves combined answer)
                               |
                               V
                 Validator Agent (checks correctness)
                               |
                               V
                          Final Answer
```

## Agent Responsibilities

### Planner / Orchestrator

- Break user query into smaller tasks
- Generate task list
- Delegate tasks to worker agents

### Worker Agents

- Execute tasks provided by planner
- Run in parallel
- Produce task-specific results

### Reflection Agent

- Combine worker outputs
- Improve clarity and coherence
- Remove redundancy

### Validator Agent

- Verify correctness
- Check logical consistency
- Ensure completeness
- Return final validated answer

## System Flow

```
         User Query
             |
             V
          Planner
             |
             V
      Parallel Workers
             |
             V
         Reflection
             |
             V
         Validation
             |
             V
        Final Answer
```
