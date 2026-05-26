```md
# AI QA Workflow Agent (MVP)

An AI-assisted QA workflow orchestration project that combines:

- Jira ticket analysis
- Local LLM reasoning (Ollama + Qwen)
- Playwright test execution
- QA workflow automation
- Human-in-the-loop approval flows

## Project Goal

The goal of this project is to explore how AI agents can assist QA and deployment workflows safely and reliably.

Instead of replacing deterministic automation, the system uses an LLM as a reasoning and orchestration layer that helps:

- classify Jira tickets
- choose relevant test suites
- summarize failures
- draft Jira comments
- assist QA workflows

while keeping humans in control of risky actions.

---

# Current MVP Scope

Current MVP flow:

1. Read Jira ticket
2. Send ticket context to local LLM
3. LLM selects the most relevant Playwright test/tool
4. Python validates returned tool selection
5. Playwright test executes
6. AI summarizes results
7. Human approves Jira actions before execution

---

# Tech Stack

- Python
- Ollama
- Qwen2.5
- Playwright
- Jira API (planned)

---

# Why This Project Exists

This project started as an exploration into:
- AI workflow orchestration
- agent tooling
- QA automation workflows
- conversational/system reasoning
- human-in-the-loop AI systems

The focus is reliability and operational usefulness rather than AI hype.

---

# Current Learning Goals

- Structured LLM outputs
- Tool orchestration
- Workflow routing
- Playwright integration
- Jira automation
- AI-assisted QA workflows
- Agent safety and guardrails

---

# Future Ideas

- Dynamic tool registry
- AI-generated test plans
- Automatic bug report drafting
- Evaluation pipelines
- Workflow memory/retrieval
- UI dashboard
- Multi-step orchestration
- Conversational QA assistant

---

# Current Status

Early MVP / actively being built.
```
