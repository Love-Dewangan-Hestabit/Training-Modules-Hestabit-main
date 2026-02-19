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



# Hybrid Search
docs = retriever.search(query, filters=filters)

# Rerank
reranked = reranker.rerank(query, docs, top_k=5)

# Build Context
context = builder.build_context(reranked)

print("\nFINAL CONTEXT SENT TO LLM:\n")
print(context)
