def detect_hallucination(llm, question, context, answer):
    prompt = f"""
Question:
{question}

Context:
{context}

Answer:
{answer}

Is the answer fully supported by the context?
Reply with:
SUPPORTED
or
HALLUCINATED
"""

    result = llm.generate(prompt)

    return "HALLUCINATED" in result.upper()