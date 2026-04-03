from retriever.hybrid_retriever import HybridRetriever
from retriever.reranker import Reranker
from pipelines.context_builder import ContextBuilder

retriever = HybridRetriever()
reranker = Reranker()
builder = ContextBuilder()

query = "Explain how global supply chain disruptions and semiconductor shortages affected Aptiv's 2022 financial performance and risk exposure."


filters = {
    "source": "raw.pdf"
}



docs = retriever.search(query, filters=filters)

reranked = reranker.rerank(query, docs, top_k=3)

context = builder.build_context(reranked)

print("\nFinal content sent to llm:\n")
print(context)
