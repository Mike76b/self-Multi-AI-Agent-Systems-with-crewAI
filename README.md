# Self‑Multi‑AI‑Agent‑Systems‑with‑CrewAI

## Overview
This repository hosts the full set of exercises and example implementations from the **DeepLearningAI "Multi‑AI‑Agent Systems with CrewAI"** course.  Each sub‑directory demonstrates a distinct multi‑agent workflow built with **CrewAI**, ranging from research article generation to automated customer‑support, outreach campaigns, event planning, financial analysis, and job‑application automation.

The top‑level `main.py` script showcases a **sales‑lead generation crew** that combines custom tools (directory reading, web search, sentiment analysis) to profile a lead and craft personalized outreach drafts.  The project also includes Jupyter notebooks, auxiliary scripts, and documentation to help you explore, extend, and experiment with CrewAI‑powered agents.

---

## Repository Structure
```
.
├── crew_1_research_write_articles/   # Agents that research a topic and draft a markdown article
├── crew_2_customer_support_automation/ # Automated ticket triage & response generation
├── crew_3_tools_customer_outreach_campaign/ # End‑to‑end sales outreach workflow (featured in main.py)
├── crew_4_automate_event_planning/   # Event‑planning assistant agents
├── crew_5_multi-agent_financial_analysis/ # Financial data extraction & reporting agents
├── crew_6_job_application_crew/      # Resume parsing and cover‑letter generation
├── compl_docs/                       # Supplementary documentation & notes
├── expl.ipynb                         # Interactive notebook for quick experimentation
├── main.py                            # Entry‑point demonstrating a two‑agent sales crew
├── pyproject.toml                     # Poetry/PEP‑517 project metadata & dependencies
└── README.md                          # (this file)
```

---

## Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/self-Multi-AI-Agent-Systems-with-CrewAI.git
   cd self-Multi-AI-Agent-Systems-with-CrewAI
   ```
2. **Create a virtual environment** (Python ≥ 3.10 recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -e .               # installs the package in editable mode
   pip install -r requirements.txt  # if a requirements file is provided
   ```
   The `pyproject.toml` already declares the required libraries (crewai, crewai‑tools, python‑dotenv, etc.).
4. **Set required environment variables**
   ```bash
   export OPENAI_API_KEY=your_openai_key
   export SERPER_API_KEY=your_serper_key   # needed for web‑search tool
   ```
5. **Run the demo**
   ```bash
   python main.py
   ```
   The script will produce a `customer_outreach_campaign.md` file containing the generated outreach drafts.

---

## Detailed Usage Examples
### 1. Research‑Write Article Crew
```bash
python crew_1_research_write_articles/main_L2.py
```
Generates an article markdown (`article.md`) based on a supplied topic.

### 2. Customer‑Support Automation
```bash
python crew_2_customer_support_automation/main.py
```
Simulates ticket classification and response drafting.

### 3. Event Planning Crew
```bash
python crew_4_automate_event_planning/main.py
```
Creates a schedule, invites, and budget plan for a fictional event.

*Each crew follows the same pattern:* define agents, attach tools, create tasks, assemble a `Crew`, and `kickoff` with a dictionary of inputs.

---

## Extending the Project
- **Add new tools** by subclassing `BaseTool` (see `SentimentAnalysisTool` in `main.py`).
- **Create additional agents** with custom roles/backstories to experiment with different LLM behaviours.
- **Swap LLM providers** by setting `OPENAI_MODEL_NAME` or configuring other providers supported by CrewAI (e.g., Anthropic, Ollama).
- **Persist memory**: set `memory=True` on the `Crew` construction to retain context across multiple runs.

---

## License
This work is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## Acknowledgements
- **DeepLearningAI** – for the original course material and inspiration.
- **CrewAI** – the underlying multi‑agent orchestration framework.
- **OpenAI** and **Serper** – for the language model and web‑search capabilities used throughout the examples.

---

*Feel free to send me an email at miguel76b@protonmail.com with any improvements, new agent ideas, or bug fixes.*
