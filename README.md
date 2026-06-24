# AI QA Workflow Agent (MVP)

An AI-assisted QA workflow orchestration project that combines:

- Jira ticket analysis
- Local LLM reasoning with Ollama and Qwen
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

## Current MVP Scope

Current MVP flow:

1. Read a Jira ticket
2. Send ticket context to a local LLM
3. Let the LLM select the most relevant Playwright test or tool
4. Validate the returned tool selection in Python
5. Execute the selected test stub
6. Summarize the result
7. Keep Jira actions behind human approval

## Setup

This repo is intentionally lightweight. The current runnable prototype only depends on `requests`.

1. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

2. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Make sure Ollama is running locally and the `qwen2.5` model is available.

5. Run the demo:

   ```powershell
   python main.py
   ```

   You can also pass a different ticket string:

   ```powershell
   python main.py "Login button does not open the auth modal."
   ```

## Tech Stack

- Python
- Requests
- Ollama
- Qwen2.5
- Playwright support planned
- Jira API support planned

## Current Status

Early MVP and actively being built.
