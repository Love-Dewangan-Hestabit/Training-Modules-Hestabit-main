from fastapi import FastAPI
from pydantic import BaseModel

from memory.memory_store import MemoryStore
from utils.refinement import refine_answer
from utils.hallucination import detect_hallucination
from utils.scoring import faithfulness_score, confidence_score

from retriever.hybrid_retriever import HybridRetriever
from retriever.reranker import Reranker
from pipelines.context_builder import ContextBuilder
from generator.llm_client import LLMClient
from pipelines.sql_pipeline import SQLPipeline
from retriever.image_search import HybridImageSearch

app = FastAPI()

memory = MemoryStore()
retriever = HybridRetriever()
reranker = Reranker()
builder = ContextBuilder()
llm = LLMClient()
sql_pipeline = SQLPipeline("database.db")
image_search = HybridImageSearch()


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_text(req: QuestionRequest):

    past_context = memory.get_recent_context()

    docs = retriever.search(req.question)
    docs = reranker.rerank(req.question, docs)

    context = builder.build_context(docs)
    full_context = past_context + "\n" + context

    draft = llm.generate(
        f"Answer using only context:\n{full_context}\n\nQuestion:{req.question}"
    )

    refined = refine_answer(llm, req.question, full_context, draft)

    hallucinated = detect_hallucination(
        llm, req.question, full_context, refined
    )

    faithfulness = faithfulness_score(
        llm, req.question, full_context, refined
    )

    confidence = confidence_score(faithfulness, hallucinated)

    memory.save_interaction(req.question, refined, {
        "confidence": confidence,
        "hallucinated": hallucinated
    })

    return {
        "answer": refined,
        "confidence": confidence,
        "hallucinated": hallucinated
    }


@app.post("/ask-sql")
def ask_sql(req: QuestionRequest):
    result = sql_pipeline.run(req.question)
    return {"answer": result}


@app.post("/ask-image")
def ask_image(req: QuestionRequest):
    results = image_search.text_to_image(req.question)
    return {"results": results}