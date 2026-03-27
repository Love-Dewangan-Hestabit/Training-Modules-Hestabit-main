import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["JOBLIB_START_METHOD"] = "fork"

import streamlit as st
import asyncio
import sys


ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import nest_asyncio
nest_asyncio.apply()

@st.cache_resource
def get_orchestrator():
    """
    Initialize the orchestrator once and cache it across Streamlit reloads.
    This prevents memory pile-up and 'atexit' threading errors.
    """
    from orchestrator.orchestrator import NexusOrchestrator
    return NexusOrchestrator()

st.set_page_config(page_title="NEXUS AI", layout="wide")

st.markdown("""
<style>
    .null-agent { color: #888; font-style: italic; }
    .final-output { font-weight: 500; font-size: 1.1rem; }
    div[data-testid="stExpander"] details summary p {
        font-weight: 600;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

if "orchestrator" not in st.session_state:
    try:
        st.session_state.orchestrator = get_orchestrator()
    except Exception as e:
        st.error(f"Failed to initialize Nexus AI: {e}")
        st.stop()

with st.sidebar:
    st.title("NEXUS AI")
    st.write("Autonomous Multi-Agent Intelligence")
    st.divider()
    
    st.subheader("Workspace Files")
    st.write("Upload CSV or TXT files to use with the Database and File agents.")
    uploaded_files = st.file_uploader("Upload Data", accept_multiple_files=True)
    if uploaded_files:
        os.makedirs("data", exist_ok=True)
        current_uploads = []
        for f in uploaded_files:
            file_path = os.path.join("data", f.name)
            with open(file_path, "wb") as out:
                out.write(f.getbuffer())
            current_uploads.append(f.name)
        st.session_state.uploaded_filenames = current_uploads
        st.success(f"Files securely loaded: {', '.join(current_uploads)}")
    
    st.divider()
    st.subheader("Memory Stats")
    vec_count = st.session_state.orchestrator.vector_store.count()
    lt_count = st.session_state.orchestrator.long_term.count()
    sess_count = st.session_state.orchestrator.session_memory.size()
    
    col1, col2 = st.columns(2)
    col1.metric("Vector Store", vec_count)
    col2.metric("Long Term DB", lt_count)
    st.metric("Session Context", f"{sess_count} messages")

st.title("Command Center")
st.write("Ask NEXUS AI to analyze data, execute code, write files, or plan strategies.")


user_task = st.chat_input("Enter your task here...")

if user_task:

    with st.chat_message("user"):
        st.write(user_task)
    
    st.write("---")
    st.header("Agent Pipeline")
    
    status_msg = st.status("Initializing...", expanded=True)
    
    col_tools, col_agents = st.columns([1, 2])
    
    with col_tools:
        st.subheader("Tools")
        tool_block = st.empty()
        
    with col_agents:
        st.subheader("Agents")
        agent_names = [
            "research_agent", "analyst_agent", "critic_agent", 
            "optimizer_agent", "validator_agent", "reporter_agent"
        ]
        agent_blocks = {name: st.empty() for name in agent_names}
    

    with tool_block.container():
        with st.expander("🛠️ Tools [Null]", expanded=False):
            st.markdown("<span class='null-agent'>No tools used in this pipeline.</span>", unsafe_allow_html=True)
            
    for name in agent_names:
        with agent_blocks[name].container():
            with st.expander(f"⚪ {name.replace('_', ' ').title()} [Null]", expanded=False):
                st.markdown("<span class='null-agent'>Not utilized for this task.</span>", unsafe_allow_html=True)
                
    st.write("---")
    st.header("Final Output")
    final_box = st.empty()
    
   
    tool_outputs_list = []
    generated_files_list = []
    
    def ui_callback(event_type, data):
        if event_type == "phase":
            status_msg.update(label=f"Phase: {data}")
            
        elif event_type == "tool":
            tool_outputs_list.append(f"**{data['name']}**\n```text\n{data['output'][:1000]}\n```")
            if "File written:" in data["output"]:
                import re
                m = re.search(r"File written:\s*(.+?)\s*\(", data["output"])
                if m:
                    generated_files_list.append(m.group(1).strip())
                    
            with tool_block.container():
                with st.expander("🛠️ Tools [Active]", expanded=False):
                    for t in tool_outputs_list:
                        st.markdown(t)
                        
        elif event_type == "agent":
            name = data["name"]
            out = data["output"]
            if name in agent_blocks:
                with agent_blocks[name].container():
                    with st.expander(f"🟢 {name.replace('_', ' ').title()} [Active]", expanded=False):
                        st.markdown(out)
    
    final_answer = ""
    try:
        
        active_files = st.session_state.get("uploaded_filenames", [])
        
        final_answer = asyncio.run(
            st.session_state.orchestrator.run(
                user_task, 
                ui_callback=ui_callback,
                active_files=active_files
            )
        )
        
        with final_box.container():
            st.info(final_answer)
            
        if generated_files_list:
            st.write("---")
            st.header("Generated Files")
            for fpath in set(generated_files_list):
                if os.path.exists(fpath):
                    st.subheader(fpath)
                    try:
                        with open(fpath, "r", encoding="utf-8") as f:
                            content = f.read()
                        st.code(content, language="markdown")
                        
                        with open(fpath, "rb") as f:
                            st.download_button(label=f"Download {os.path.basename(fpath)}", data=f, file_name=os.path.basename(fpath))
                    except Exception:
                        st.warning(f"Could not read {fpath}")
            
    except Exception as e:
        status_msg.update(label="Pipeline Error", state="error")
        st.error(str(e))
