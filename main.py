from router import route_ticket
from tools import TOOL_MAP

ticket = "Claim submission modal does not open after clicking submit button."

result = route_ticket(ticket)

print("\nParsed fields:")
print("Intent:", result["intent"])
print("Priority:", result["priority"])
print("Tool:", result["tool"])
print("Reason:", result["reason"])

tool = result["tool"]

if tool in TOOL_MAP:
    TOOL_MAP[tool]()
else:
    print("No valid tool selected. Human review needed.")