# Week 9 (Day 4) - Memory Systems (Short Term, Long Term and Vector Memory)

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To implement a hybrid memory architecture for an AI agent:

- Short-term memory (session-based)
- Long-term memory (SQLite Persistence)
- Vector memory (FAISS similarity search)

## Architecture

```
                        User Query
                            |
                            V
                  Vector Search (FAISS)
                            |
                            V
                Retrieve similar past data
                            |
                            V
                Combine with session memory
                            |
                            V
                    Inject into prompt
                            |
                            V
                   LLM generate response
                            |
                            V
                 Store into memory systems
```

## Components

### Session Memory (Short-Term)

- Stores recent conversation
- Maintains context within session

### Long-Term Memory (SQLite)

- Stores important facts
- Persistent across sessions

### Vector Memory (FAISS)

- Stores embeddings
- Enables similarity-based retrieval
