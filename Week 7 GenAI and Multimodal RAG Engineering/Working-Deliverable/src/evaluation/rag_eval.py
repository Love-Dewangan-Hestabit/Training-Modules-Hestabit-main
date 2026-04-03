from utils.scoring import faithfulness_score
from utils.hallucination import detect_hallucination

def evaluate_sample(llm, question, context, answer):
    faithfulness = faithfulness_score(llm, question, context, answer)
    hallucinated = detect_hallucination(llm, question, context, answer)

    return {
        "faithfulness": faithfulness,
        "hallucinated": hallucinated
    }