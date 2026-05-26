import requests
import json

def claim_submission_test():
    print("Running claim submission Playwright test...")

allowed_tools = ["claim_submission_test", "login_test", "payment_flow_test", "unknown"]
tool_map = {
    "claim_submission_test": claim_submission_test,
}
required_fields = ["intent", "priority", "tool", "reason"]


prompt = f"""
You are an AI QA routing assistant.

Your job is to choose the best tool for a Jira ticket.

Available tools:
{allowed_tools}

Rules:
- Choose exactly one tool from the Available tools list.
- If the ticket is related to claim submission, choose claim_submission_test.
- If no tool fits, choose unknown.
- Respond ONLY in valid JSON.
- The "tool" value must exactly match one item from Available tools.

Ticket:
Claim submission modal does not open after clicking submit button.

Return format:
{{
  "intent": "...",
  "priority": "low | medium | high",
  "tool": "...",
  "reason": "..."
}}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5",
        "prompt": prompt,
        "stream": False
    },
    timeout=60
)

data = response.json()

raw_ai_response = data["response"]

print("Raw AI Response:")
print(raw_ai_response)

parsed = json.loads(raw_ai_response)

for field in required_fields:
    if field not in parsed:
        raise ValueError(f"Missing required field: {field}")

print("\nParsed fields:")
print("Intent:", parsed["intent"])
print("Priority:", parsed["priority"])
print("Raw Tool:", parsed["tool"])
if parsed["tool"] not in allowed_tools:
    parsed["tool"] = "unknown"



print("Tool:", parsed["tool"])
print("Reason:", parsed["reason"])

if parsed["tool"] in tool_map:
    tool_map[parsed["tool"]]()
else:
    print("No valid tool selected. Human review needed.")