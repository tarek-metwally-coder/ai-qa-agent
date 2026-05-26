import json
from llm_client import call_llm
from tools import ALLOWED_TOOLS

REQUIRED_FIELDS = ["intent", "priority", "tool", "reason"]


def build_routing_prompt(ticket: str) -> str:
    return f"""
You are an AI QA routing assistant.

Your job is to choose the best tool for a Jira ticket.

Available tools:
{ALLOWED_TOOLS}

Rules:
- Choose exactly one tool from the Available tools list.
- If the ticket is related to claim submission, choose claim_submission_test.
- If the ticket is related to login, choose login_test.
- If the ticket is related to payment, choose payment_flow_test.
- If no tool fits, choose unknown.
- Respond ONLY in valid JSON.
- The "tool" value must exactly match one item from Available tools.

Ticket:
{ticket}

Return format:
{{
  "intent": "...",
  "priority": "low | medium | high",
  "tool": "...",
  "reason": "..."
}}
"""


def route_ticket(ticket: str) -> dict:
    prompt = build_routing_prompt(ticket)
    raw_response = call_llm(prompt)

    print("Raw AI Response:")
    print(raw_response)

    parsed = json.loads(raw_response)

    for field in REQUIRED_FIELDS:
        if field not in parsed:
            raise ValueError(f"Missing required field: {field}")

    if parsed["tool"] not in ALLOWED_TOOLS:
        parsed["tool"] = "unknown"

    return parsed