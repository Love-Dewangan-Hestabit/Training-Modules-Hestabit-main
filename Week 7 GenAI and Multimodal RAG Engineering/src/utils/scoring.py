def faithfulness_score(llm, question, context, answer):
    prompt = f"""
Rate faithfulness of the answer to context on scale 0 to 1.

Question:
{question}

Context:
{context}

Answer:
{answer}

Return only number.
"""

    try:
        score = float(llm.generate(prompt))
    except:
        score = 0.5

    return max(0.0, min(1.0, score))


def confidence_score(faithfulness, hallucinated):
    if hallucinated:
        return round(faithfulness * 0.5, 2)
    return round(faithfulness, 2)