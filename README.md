# Autonomous Multi-Agent Content Engine: Research to Social Media

A production-ready multi-agent system built with [CrewAI](https://crewai.com) that automates the lifecycle of content creation: from trending topic research to long-form writing and social media distribution.

## Key Features
- **Auto-Research**: Uses `SerperDevTool` to scan the web for the latest tech news.
- **Multi-Agent Workflow**: Sequential execution involving a Planner, Writer, Editor, and Social Media Manager.
- **Daily Automation**: Configurable to run daily across multiple tech domains (AI, ML, LLMs, etc.).
- **Social Media Ready**: Automatically generates markdown-ready LinkedIn posts for every article.

## Project Structure
- `main.py`: Entry point for the content engine.
- `config.yaml`: Configuration for domains and news sources.
- `src/`: Modular core package.
- `scheduler.py`: Script for periodic execution.

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/WajahatAliBasharat073/Autonomous-Multi-Agent-Content-Engine-Research-to-Social-Media.git
   ```
2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Setup**:
   Copy `.env.example` to `.env` and add your `OPENAI_API_KEY` and `SERPER_API_KEY`.
