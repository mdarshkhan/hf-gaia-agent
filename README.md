# HF GAIA Agent 🤖

An autonomous AI agent for solving GAIA benchmark tasks using Hugging Face tools and transformer models.

## 🎯 Project Goal

Build a working autonomous agent that:
- Calls tools to fetch questions from the GAIA benchmark
- Uses an LLM to reason through problems
- Submits answers to the evaluation framework
- Deploys publicly on Hugging Face Spaces

## 📦 Tech Stack

- **Python** — Core language
- **Transformers** — LLM inference
- **Requests** — API calls
- **Smolagents** — Agent framework (extensible)
- **Gradio** — UI (optional)
- **Hugging Face Spaces** — Deployment

## 📁 Project Structure

```
hf-gaia-agent/
├── app.py           # Main application
├── agent.py         # Agent logic
├── tools.py         # GAIA API functions
├── submit.py        # Answer submission
├── requirements.txt # Dependencies
└── README.md        # This file
```

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/mdarshkhan/hf-gaia-agent.git
cd hf-gaia-agent
pip install -r requirements.txt
```

### 2. Run Locally

```bash
python app.py
```

This will:
1. Fetch a random question from GAIA
2. Pass it to the agent
3. Generate and display an answer

## 📋 File Overview

### `tools.py`
API integration for fetching questions:
- `get_random_question()` — Fetch one random question
- `get_all_questions()` — Fetch all available questions

### `agent.py`
Simple autonomous agent:
- `SimpleAgent` class with LLM reasoning
- Customizable model selection
- `think()` method for generating answers

### `app.py`
Main application:
- Initializes agent
- Fetches questions
- Displays results

### `submit.py`
Submit answers to GAIA:
- `submit_answers()` function
- Handles API requests
- Includes your HF username (Arshkhan7)

## 🎓 Next Steps: Improve Your Agent

Upgrade gradually:

### Level 1: Better Models
Replace `gpt2` with stronger models:
```python
agent = SimpleAgent(model="Qwen/Qwen2.5-1.5B-Instruct")
# or
agent = SimpleAgent(model="meta-llama/Llama-3.2-3B-Instruct")
```

### Level 2: Add Tools
- Web search capability
- Calculator tool
- File reader
- Memory system

### Level 3: Advanced Reasoning
- ReAct prompting
- Chain-of-thought
- Structured outputs
- Multi-step workflows

### Level 4: Production Ready
- Error handling
- Logging
- Caching
- Rate limiting

## 🌐 Deploy to Hugging Face Spaces

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose **Gradio** SDK
4. Set to **Public**
5. Upload your files
6. Space deploys automatically

**Your Space URL:** `https://huggingface.co/spaces/Arshkhan7/your-space-name`

## 📊 Portfolio Description

Use this in your resume:

> Built an autonomous AI agent system using Hugging Face tools and transformer models to solve benchmark tasks from the GAIA evaluation framework. Implemented tool calling, API integration, and multi-step reasoning workflows, then deployed the solution publicly on Hugging Face Spaces.

## 📚 Learning Path

1. ✅ Understand this project completely
2. ✅ Deploy publicly
3. ✅ Explain architecture clearly
4. 🔄 Iterate and improve
5. 📈 Learn: LangChain, LangGraph, CrewAI, LlamaIndex

## 🔗 Resources

- [GAIA Benchmark](https://huggingface.co/gaia-benchmark)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Smolagents Docs](https://huggingface.co/docs/smolagents)
- [Hugging Face Spaces](https://huggingface.co/spaces)

## 👤 Author

Arshkhan7 (mdarshkhan)

## 📄 License

MIT
