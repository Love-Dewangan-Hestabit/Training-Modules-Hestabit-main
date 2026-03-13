import streamlit as st
import os
import tempfile
import sqlite3
import pandas as pd
from tabulate import tabulate



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




memory = MemoryStore()
retriever = HybridRetriever()
reranker = Reranker()
builder = ContextBuilder()
llm = LLMClient()
image_search = HybridImageSearch()




st.set_page_config(
    page_title="Advanced Multimodal RAG System",
    layout="wide"
)

st.title("Advanced Multimodal RAG System")

mode = st.sidebar.selectbox(
    "Choose Mode",
    ["Text RAG (/ask)", "SQL RAG (/ask-sql)", "Image RAG (/ask-image)"]
)

show_debug = st.sidebar.checkbox("Show Debug Traces", value=False)


with st.sidebar.expander("Memory (Last 5)"):
    history = memory.load_memory()
    for item in history:
        st.write(f"**Q:** {item['question']}")
        st.write(f"**A:** {item['answer'][:100]}...")
        st.divider()


if mode == "Text RAG (/ask)":

    question = st.text_input("Ask your question")

    if st.button("Submit") and question:

        with st.spinner("Processing..."):

            debug_data = {}

            past_context = memory.get_recent_context()

            docs = retriever.search(question)
            docs = reranker.rerank(question, docs)

            context = builder.build_context(docs)
            full_context = past_context + "\n" + context

            debug_data["retrieved_docs"] = len(docs)

            draft = llm.generate(
                f"Answer using ONLY provided context:\n{full_context}\n\nQuestion:{question}"
            )

            refined = refine_answer(
                llm, question, full_context, draft
            )

            hallucinated = detect_hallucination(
                llm, question, full_context, refined
            )

            faithfulness = faithfulness_score(
                llm, question, full_context, refined
            )

            confidence = confidence_score(
                faithfulness, hallucinated
            )

            memory.save_interaction(
                question,
                refined,
                {
                    "confidence": confidence,
                    "hallucinated": hallucinated
                }
            )

        st.subheader("Answer")
        st.write(refined)

        col1, col2, col3 = st.columns(3)

        col1.metric("Faithfulness", faithfulness)
        col2.metric("Confidence", confidence)
        col3.metric("Hallucination", "YES" if hallucinated else "NO")

        if show_debug:
            st.subheader("🔍 Debug Traces")
            st.json(debug_data)




elif mode == "SQL RAG (/ask-sql)":

    st.header("Upload Database / CSV / Excel")

    uploaded_file = st.file_uploader(
        "Upload .db, .csv or .xlsx file",
        type=["db", "csv", "xlsx"]
    )

    if uploaded_file is not None:

        temp_dir = tempfile.gettempdir()
        db_path = os.path.join(temp_dir, "uploaded_database.db")

        if uploaded_file.name.endswith(".db"):

            with open(db_path, "wb") as f:
                f.write(uploaded_file.read())

            st.success("SQLite database loaded successfully.")


        elif uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

            conn = sqlite3.connect(db_path)
            table_name = uploaded_file.name.replace(".csv", "")
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            conn.close()

            st.success(f"CSV loaded as table: {table_name}")


        elif uploaded_file.name.endswith(".xlsx"):

            excel = pd.ExcelFile(uploaded_file)
            conn = sqlite3.connect(db_path)

            for sheet in excel.sheet_names:
                df = excel.parse(sheet)
                df.to_sql(sheet, conn, if_exists="replace", index=False)

            conn.close()

            st.success(f"Excel sheets loaded as tables: {excel.sheet_names}")


        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()

        st.write("### Available Tables:")
        st.write(tables)

        question = st.text_input("Ask database question")

        if st.button("Run Query") and question:

            sql_pipeline = SQLPipeline(db_path)

            with st.spinner("Generating SQL..."):

                schema = sql_pipeline.schema_loader.load_schema()

                sql = sql_pipeline.generator.generate_sql(question, schema)

                st.subheader("Generated SQL")
                st.code(sql, language="sql")

                try:
                    sql_pipeline.validate_sql(sql)
                    columns, rows = sql_pipeline.execute_sql(sql)

                    if rows:

                        st.subheader("Query Result")
                        st.dataframe(rows)

                        result_table = tabulate(
                            rows,
                            headers=columns,
                            tablefmt="grid"
                        )

                        summary = sql_pipeline.generator.summarize(
                            question,
                            result_table
                        )

                        st.subheader("Summary")
                        st.write(summary)

                        memory.save_interaction(question, summary)

                    else:
                        st.warning("No results found.")

                except Exception as e:
                    st.error(f"SQL Error: {e}")



elif mode == "Image RAG (/ask-image)":

    question = st.text_input("Describe the image you are looking for")

    if st.button("Search Images") and question:

        with st.spinner("Searching..."):
            results = image_search.text_to_image(question)

        st.subheader("Results")

        for res in results:
            st.image(res["image_path"], width="stretch")
            st.write("Caption:", res["caption"])
            st.write("OCR:", res["ocr_text"][:200])
            st.divider()

        memory.save_interaction(question, "Returned image results")