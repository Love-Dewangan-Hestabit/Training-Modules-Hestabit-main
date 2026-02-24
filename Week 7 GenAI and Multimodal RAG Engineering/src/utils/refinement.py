def refine_answer(llm, question, context, draft_answer):
    prompt = f"""
You are reviewing an answer for quality.

Question:
{question}

Context:
{context}

Draft Answer:
{draft_answer}

Check:
- Is it grounded in context?
- Is anything hallucinated?
- Improve clarity.
- Keep answer concise.

Return improved answer only.
"""
    return llm.generate(prompt)