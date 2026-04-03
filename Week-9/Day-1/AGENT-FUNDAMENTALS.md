# Week 9 (Day 1) - Agent Foundations and Message Based Communication

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To implement agents for Research, Summarizer and Answer also each agent has a unique role, unique system prompt, memory window = 10 and Strict job separation.

## Implementation Overview

This project I have implemented using **AutoGen** and a **Local Large Language Model (TinyLlama)**.

The system contains three specialized agents:

- Research Agent
- Summarizer Agent
- Answer Agent

## Agent Architecture

The system follows a **multi-agent pipeline** where information flows between agents.

```
                         User Query
                             |
                             V
            Research Agent -> Collect raw information
                             |
                             V
        Summarizer Agent -> Convert research into summary
                             |
                             V
                Answer Agent -> Generate final answer
```

## Agents Implemented

### 1. Research Agent

#### Role

The Research Agent is responsible for collecting **raw factual information** about the user's query.

#### Responsibilities

- To retrieve relevant information
- To provide detailed research data
- To pass the information to the Summarizer Agent

### 2. Summarizer Agent

#### Role

The Summarizer Agent converts the research output into a **concise and structured summary**.

#### Responsibilities

- To read research output
- To extract key insights
- To produce a clear summary

### 3. Answer Agent

#### Role

The Answer Agent generates the **final response for the user**.

#### Responsibilities

- To interpret the summarized information
- To generate a clear explanation
- To provide the final answer

## Perception -> Reasoning -> Action Loop

Each agent follows the standard AI agent loop:

### Perception

The agent receives input (user query or previous agent output).

### Reasoning

The LLM processes the input using the system prompt.

### Action

The agent generates the required output based on its role.

## Role Isolation

Each agent has **strict role isolation**, meaning it performs only its assigned responsibility.

```
| Agent            | Responsibility        | Restricted Tasks         |
| ---------------- | --------------------- | ------------------------ |
| Research Agent   | Information gathering | Summarization, answering |
| Summarizer Agent | Summarization         | Research, answering      |
| Answer Agent     | Final response        | Research, summarization  |
```

## Technology Stack

The implementation follows the required stack:

| Component       | Technology |
| --------------- | ---------- |
| Agent Framework | AutoGen    |
| LLM Model       | Mistral    |
| Runtime         | Ollama     |
| Language        | Python     |
