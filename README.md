<div align="center">

# 🤖 Agentic Research Assistant

**Transform any topic into a polished research report and presentation — fully automated, end-to-end.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Mistral AI](https://img.shields.io/badge/Mistral_AI-LLM-FF7000?style=flat-square)](https://mistral.ai)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=flat-square)](https://langchain.com)
[![Tavily](https://img.shields.io/badge/Tavily-Web_Search-4A90D9?style=flat-square)](https://tavily.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)

</div>

---

## What Is This?

You type a topic. The system does the rest.

**Agentic Research Assistant** is a multi-agent AI pipeline that autonomously searches the web, synthesizes information, writes a structured report, and exports it as both a PDF and a PowerPoint — no manual steps required.

It's built to showcase what modern LLM orchestration looks like in practice: specialized agents, each with a single responsibility, passing outputs down a clean pipeline.

---

## Demo

### 🖥️ Streamlit UI (Recommended)

A full dark-themed web interface — live pipeline progress bar, inline results viewer, and one-click downloads.

> UI built with the assistance of [Claude](https://claude.ai) by Anthropic.

**Run the UI:**
```bash
streamlit run app.py
```

**What you get:**
- 🔴→🟢 Live step-by-step pipeline progress bar
- 📰 Search results, analysis, and full report rendered inline
- ⬇️ One-click PDF & PPT download buttons
- 🎈 Completion animation on finish

---

### ⌨️ CLI Mode

```
$ python main.py

ENTER YOUR TOPIC: Quantum AI

[🔍] Research Agent    → Fetching top sources via Tavily...
[🧠] Analysis Agent    → Analyzing and synthesizing content...
[📄] Report Agent      → Writing structured research report...
[📊] Presentation Agent → Generating slide content...
[📑] PDF Export Agent  → Building report.pdf...
[🎞️] PPT Export Agent  → Building report.pptx...

✅ Done! Output files ready:
   → report.pdf
   → report.pptx
```

---

## Architecture

The system follows a strict linear pipeline where each agent receives the previous agent's output as its input:

```
User Topic Input
      │
      ▼
┌─────────────────────────────┐
│   Research Agent            │  ← Tavily Search API
│   Web search & data fetch   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Analysis Agent            │  ← Mistral AI
│   Summarize & identify gaps │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Report Agent              │  ← Mistral AI
│   Structure a full report   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Presentation Agent        │  ← Mistral AI
│   Convert report to slides  │
└────────────┬────────────────┘
             │
      ┌──────┴──────┐
      ▼             ▼
┌──────────┐  ┌──────────┐
│ PDF Agent│  │ PPT Agent│   ← ReportLab / python-pptx
│report.pdf│  │report.pptx│
└──────────┘  └──────────┘
```

Each agent is stateless and independently testable. Swap out any layer without touching the others.

---

## Features

| Capability | Details |
|---|---|
| 🖥️ **Streamlit UI** | Dark-themed web interface with live pipeline progress & downloads |
| 🔍 **Web Research** | Real-time search via Tavily API |
| 🧠 **AI Analysis** | Content synthesis and insight extraction using Mistral AI |
| 📄 **Report Generation** | Structured, section-based research report |
| 📊 **Slide Generation** | Automatically structured presentation content |
| 📑 **PDF Export** | Professional document via ReportLab |
| 🎞️ **PPT Export** | Editable slide deck via python-pptx |
| 🔗 **Modular Agents** | Each agent is a separate, replaceable module |
| ⚡ **Zero Manual Steps** | One command runs the entire pipeline |

---

## Project Structure

```
agentic-research-assistant/
│
├── agents/
│   ├── research_agent.py       # Web search via Tavily
│   ├── analysis_agent.py       # Data synthesis via Mistral
│   ├── report_agent.py         # Structured report generation
│   ├── presentation_agent.py   # Slide content generation
│   ├── pdf_export_agent.py     # PDF rendering via ReportLab
│   └── ppt_export_agent.py     # PPT creation via python-pptx
│
├── prompts/
│   ├── analysis_prompt.py      # Prompt template for analysis
│   ├── report_prompt.py        # Prompt template for report
│   └── presentation_prompt.py  # Prompt template for slides
│
├── main.py                     # CLI pipeline orchestrator
├── app.py                      # Streamlit web UI
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.10+ |
| UI | Streamlit |
| LLM | Mistral AI |
| Orchestration | LangChain |
| Web Search | Tavily Search API |
| PDF Generation | ReportLab |
| PPT Generation | python-pptx |
| Config | python-dotenv |

---

## Getting Started

### Prerequisites

- Python 3.10+
- A [Mistral AI](https://console.mistral.ai/) API key
- A [Tavily](https://tavily.com/) API key

### 1. Clone the repository

```bash
git clone https://github.com/dev-karthikeyan/agentic-research-assistant.git
cd agentic-research-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
MISTRAL_API_KEY=your_mistral_key_here
TAVILY_API_KEY=your_tavily_key_here
```

### 4. Run the app

**Option A — Streamlit UI (recommended):**
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

**Option B — CLI:**
```bash
python main.py
```

### Output

Two files will be generated in your working directory:

- `report.pdf` — A formatted, multi-section research document
- `report.pptx` — A presentation-ready slide deck

---

## How Each Agent Works

### 🔍 Research Agent
Queries Tavily's real-time search API and retrieves top relevant sources for the given topic. Returns raw content passages ranked by relevance.

### 🧠 Analysis Agent
Passes the raw search results to Mistral AI with a structured analysis prompt. Extracts key themes, identifies knowledge gaps, and produces a clean analytical summary.

### 📄 Report Agent
Takes the analysis and generates a complete research report with sections: Executive Summary, Background, Key Findings, Analysis, and Conclusion.

### 📊 Presentation Agent
Converts the report into a slide-by-slide content structure (title, bullet points, speaker notes) ready for export.

### 📑 PDF Export Agent
Uses ReportLab to render the report into a professionally formatted PDF with typography, spacing, and section headers.

### 🎞️ PPT Export Agent
Uses python-pptx to generate an editable `.pptx` file from the slide content, with layout and styling applied automatically.

---

## Roadmap

- [ ] Fact-checking agent with source verification
- [x] Streamlit UI dashboard *(shipped)*
- [ ] Support for multiple LLM providers (OpenAI, Gemini, Claude)
- [ ] Async parallel agent execution
- [ ] Real-time progress streaming
- [ ] Auto GitHub repo generator from report
- [ ] Web deployment (Docker + FastAPI)

---

## Contributing

Contributions are welcome. Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push and open a Pull Request

---

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

**Built with 🔥 as part of an AI Agent Engineering journey.**

If this project helped you, give it a ⭐ — it keeps the momentum going.

</div>