import streamlit as st
import time
import os
from dotenv import load_dotenv

from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.report_agent import report_agent
from agents.presentation_agent import presentation_agent
from agents.pdf_export_agent import pdf_export_agent
from agents.ppt_export_agent import ppt_export_agent

load_dotenv()

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Agentic Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #0a0a0f;
        color: #e2e8f0;
    }

    /* Hero */
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.25rem;
    }

    .hero-sub {
        text-align: center;
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 2.5rem;
        letter-spacing: 0.02em;
    }

    /* Pipeline Steps */
    .pipeline-bar {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.25rem;
        flex-wrap: wrap;
        margin-bottom: 2.5rem;
    }

    .step-chip {
        padding: 0.3rem 0.75rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 500;
        border: 1px solid #1e293b;
        background: #0f172a;
        color: #475569;
        transition: all 0.3s ease;
    }

    .step-chip.active {
        border-color: #a78bfa;
        background: #1e1b4b;
        color: #a78bfa;
        box-shadow: 0 0 12px #a78bfa44;
    }

    .step-chip.done {
        border-color: #34d399;
        background: #022c22;
        color: #34d399;
    }

    .step-arrow {
        color: #1e293b;
        font-size: 0.75rem;
    }

    /* Search box */
    .stTextInput > div > div > input {
        background: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        font-size: 1rem !important;
        padding: 0.85rem 1.2rem !important;
        transition: border-color 0.2s;
    }

    .stTextInput > div > div > input:focus {
        border-color: #a78bfa !important;
        box-shadow: 0 0 0 3px #a78bfa22 !important;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.65rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        width: 100% !important;
        transition: opacity 0.2s !important;
    }

    .stButton > button:hover {
        opacity: 0.9 !important;
    }

    /* Cards */
    .result-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
    }

    .result-card:hover {
        border-color: #334155;
    }

    .result-card a {
        color: #60a5fa;
        font-size: 0.8rem;
        text-decoration: none;
    }

    .result-card .rtitle {
        font-weight: 600;
        color: #e2e8f0;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }

    .section-label {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #475569;
        margin-bottom: 0.75rem;
        margin-top: 1.5rem;
    }

    .content-box {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 1.5rem;
        color: #cbd5e1;
        font-size: 0.9rem;
        line-height: 1.8;
        white-space: pre-wrap;
    }

    /* Download buttons */
    .stDownloadButton > button {
        background: #0f172a !important;
        border: 1px solid #1e293b !important;
        color: #e2e8f0 !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
        width: 100% !important;
        transition: border-color 0.2s !important;
    }

    .stDownloadButton > button:hover {
        border-color: #a78bfa !important;
        color: #a78bfa !important;
    }

    /* Status */
    .status-row {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.5rem 0;
        color: #94a3b8;
        font-size: 0.88rem;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #a78bfa;
        animation: pulse 1.2s infinite;
        flex-shrink: 0;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(0.7); }
    }

    /* Hide Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 2rem; max-width: 860px; }
</style>
""", unsafe_allow_html=True)


# ─── Session State Init ──────────────────────────────────────────────────────
for key in ["results", "analysis", "report", "presentation", "pdf_file", "ppt_file", "running", "step"]:
    if key not in st.session_state:
        st.session_state[key] = None

if "step" not in st.session_state:
    st.session_state.step = 0


# ─── Pipeline Steps Meta ─────────────────────────────────────────────────────
STEPS = [
    ("🔍", "Research"),
    ("🧠", "Analysis"),
    ("📄", "Report"),
    ("📊", "Slides"),
    ("📑", "PDF"),
    ("🎞️", "PPT"),
]


def render_pipeline(current_step):
    chips = ""
    for i, (icon, label) in enumerate(STEPS):
        if i < current_step:
            cls = "done"
            icon = "✓"
        elif i == current_step:
            cls = "active"
        else:
            cls = ""
        chips += f'<span class="step-chip {cls}">{icon} {label}</span>'
        if i < len(STEPS) - 1:
            chips += '<span class="step-arrow">›</span>'
    st.markdown(f'<div class="pipeline-bar">{chips}</div>', unsafe_allow_html=True)


def status(msg):
    st.markdown(
        f'<div class="status-row"><div class="status-dot"></div>{msg}</div>',
        unsafe_allow_html=True
    )


# ─── Hero ────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">Agentic Research Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Enter a topic → get a full research report, analysis, PDF & presentation</div>', unsafe_allow_html=True)

# ─── Pipeline Bar ────────────────────────────────────────────────────────────
current_step = st.session_state.step or 0
render_pipeline(current_step)

# ─── Input ───────────────────────────────────────────────────────────────────
col1, col2 = st.columns([5, 1])
with col1:
    topic = st.text_input("", placeholder="e.g. Quantum AI, Climate Tech, Neuromorphic Computing...", label_visibility="collapsed")
with col2:
    run = st.button("Research →")


# ─── Run Pipeline ────────────────────────────────────────────────────────────
if run and topic.strip():
    st.session_state.step = 0

    progress_placeholder = st.empty()

    # Step 1 — Research
    with progress_placeholder.container():
        render_pipeline(0)
        status("Research Agent is searching the web...")
    st.session_state.results = research_agent(topic)
    st.session_state.step = 1

    # Step 2 — Analysis
    with progress_placeholder.container():
        render_pipeline(1)
        status("Analysis Agent is synthesizing findings...")
    st.session_state.analysis = analysis_agent(st.session_state.results)
    st.session_state.step = 2

    # Step 3 — Report
    with progress_placeholder.container():
        render_pipeline(2)
        status("Report Agent is writing the structured report...")
    st.session_state.report = report_agent(st.session_state.analysis)
    st.session_state.step = 3

    # Step 4 — Presentation
    with progress_placeholder.container():
        render_pipeline(3)
        status("Presentation Agent is generating slide content...")
    st.session_state.presentation = presentation_agent(st.session_state.report)
    st.session_state.step = 4

    # Step 5 — PDF
    with progress_placeholder.container():
        render_pipeline(4)
        status("Exporting PDF...")
    st.session_state.pdf_file = pdf_export_agent(st.session_state.report)
    st.session_state.step = 5

    # Step 6 — PPT
    with progress_placeholder.container():
        render_pipeline(5)
        status("Exporting PowerPoint...")
    st.session_state.ppt_file = ppt_export_agent(st.session_state.presentation)
    st.session_state.step = 6

    progress_placeholder.empty()
    st.balloons()

elif run and not topic.strip():
    st.warning("Please enter a topic first.")


# ─── Results ─────────────────────────────────────────────────────────────────
if st.session_state.results:

    # Downloads
    if st.session_state.pdf_file and st.session_state.ppt_file:
        st.markdown('<div class="section-label">📦 Downloads</div>', unsafe_allow_html=True)
        dl1, dl2 = st.columns(2)
        with dl1:
            with open(st.session_state.pdf_file, "rb") as f:
                st.download_button("⬇ Download PDF Report", f, file_name="report.pdf", mime="application/pdf")
        with dl2:
            with open(st.session_state.ppt_file, "rb") as f:
                st.download_button("⬇ Download PPT Slides", f, file_name="report.pptx",
                                   mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")

    # Search Results
    st.markdown('<div class="section-label">🔍 Search Results</div>', unsafe_allow_html=True)
    for i, result in enumerate(st.session_state.results.get("results", []), start=1):
        st.markdown(f"""
        <div class="result-card">
            <div class="rtitle">{i}. {result.get('title', 'Untitled')}</div>
            <a href="{result.get('url', '#')}" target="_blank">{result.get('url', '')}</a>
        </div>
        """, unsafe_allow_html=True)

    # Analysis
    if st.session_state.analysis:
        st.markdown('<div class="section-label">🧠 Analysis</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="content-box">{st.session_state.analysis}</div>', unsafe_allow_html=True)

    # Report
    if st.session_state.report:
        st.markdown('<div class="section-label">📄 Research Report</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="content-box">{st.session_state.report}</div>', unsafe_allow_html=True)

    # Presentation
    if st.session_state.presentation:
        st.markdown('<div class="section-label">📊 Presentation Content</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="content-box">{st.session_state.presentation}</div>', unsafe_allow_html=True)