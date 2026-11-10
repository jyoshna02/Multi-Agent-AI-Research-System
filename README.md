# Multi-Agent AI Research System

An interactive Python-based research automation system that uses multiple specialized agents to perform web research, analyze information, conduct preliminary keyword-based fact checking, and generate structured research reports.

The project provides a simple Streamlit dashboard where users can enter a research topic and specific claims to investigate.

## Project Overview

Researching a topic manually can take time because information needs to be collected, analyzed, reviewed, and organized.

This project addresses that workflow by dividing the research process into multiple specialized agents. Each agent performs a specific task, and the Orchestrator Agent coordinates the complete workflow.

## Key Features

- **Automated Web Research:** Collects relevant search results using DuckDuckGo.
- **Keyword-Based Analysis:** Identifies and counts selected keywords in collected content.
- **Preliminary Fact Checking:** Compares user-provided claims with keywords found in available sources.
- **Multi-Agent Workflow:** Coordinates multiple agents through an Orchestrator Agent.
- **Automated Report Generation:** Creates structured research reports.
- **PDF Export:** Downloads research reports in PDF format.
- **Markdown Export:** Provides reports in Markdown format.
- **Research History:** Stores previous research records using SQLite.
- **Interactive Dashboard:** Provides a user-friendly interface using Streamlit.

## System Architecture

The project consists of the following agents:

### 1. Research Agent
- Accepts a research topic.
- Sends the topic to the web search tool.
- Collects search results, titles, URLs, and descriptions.

### 2. Analysis Agent
- Processes the collected source content.
- Searches for predefined keywords.
- Counts keyword occurrences.
- Produces basic analysis results.

### 3. Fact-Checking Agent
- Accepts claims entered by the user.
- Compares important claim keywords against available source content.
- Identifies matching sources and matching keywords.
- Provides preliminary evidence indicators.

**Note:** This is a keyword-matching approach, not an advanced semantic fact-checking system. Results require manual verification.

### 4. Report Agent
- Organizes research and analysis results.
- Generates a structured research report.
- Supports report export.

### 5. Orchestrator Agent
- Coordinates all the agents.
- Passes information between the agents.
- Collects their results.
- Produces the final research output.

## Workflow

1. User enters a research topic.
2. User provides claims to investigate.
3. Research Agent collects web search results.
4. Analysis Agent performs keyword analysis.
5. Fact-Checking Agent compares the claims against source content.
6. Report Agent generates the research report.
7. Orchestrator Agent combines the results.
8. The Streamlit dashboard displays the output.
9. Research history is stored in SQLite.
10. Users can download reports in PDF and Markdown formats.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive dashboard |
| DuckDuckGo (ddgs) | Web search |
| SQLite | Research history storage |
| ReportLab | PDF generation |
| Regular Expressions | Keyword extraction and matching |
| Git | Version control |
| GitHub | Project hosting |

## Project Structure

```text
Multi-Agent-AI-Research-System/
│
├── agents/
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── fact_check_agent.py
│   ├── report_agent.py
│   └── orchestrator_agent.py
│
├── tools/
│   ├── web_search.py
│   ├── pdf_generator.py
│   └── research_history.py
│
├── database/
│   └── research_history.db
│
├── reports/
│   └── Generated research reports
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: Generated database and report files may be excluded from GitHub through `.gitignore`.*

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- Visual Studio Code
- Internet connection

### Step 1: Clone the Repository

```bash
git clone https://github.com/jyoshna02/Multi-Agent-AI-Research-System.git
```

### Step 2: Navigate to the Project

```bash
cd Multi-Agent-AI-Research-System
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## How to Use

1. Open the Streamlit application.
2. Enter a research topic.
3. Enter claims, with one claim per line.
4. Click **Start Research**.
5. Review the collected sources.
6. Explore keyword analysis results.
7. Review preliminary fact-checking results.
8. Read the final research report.
9. Download the report as PDF or Markdown.
10. View previous research records in the research history section.

## Example Input

**Research Topic:**

Benefits of Drinking Water

**Claims:**

- Water helps regulate body temperature.
- Water supports digestion.
- Drinking enough water prevents dehydration.
- Water helps transport nutrients in the body.
- Drinking more water always improves health.

The system searches for information related to the topic and compares the provided claims with the collected source content.

## Limitations

- Search results depend on the availability of the DuckDuckGo search service.
- Keyword analysis is based on predefined keywords.
- Fact checking uses keyword matching and does not establish whether a claim is scientifically true.
- Search results and generated reports should be reviewed manually.
- The current version does not use an LLM for semantic reasoning.

## Future Improvements

- Add semantic analysis using NLP techniques.
- Improve fact verification with reliable evidence sources.
- Add source credibility evaluation.
- Improve report customization.
- Add visual analytics and research trend analysis.
- Deploy the application online.

## Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and modular development.
- Building a multi-agent workflow.
- Web search integration.
- Text processing and keyword analysis.
- Streamlit application development.
- SQLite database integration.
- PDF report generation.
- Git and GitHub version control.

GitHub: https://github.com/jyoshna02

---

*This project was developed as a hands-on learning project to explore Python automation, multi-agent architecture, web research, and data analysis.*
