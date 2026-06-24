import argparse

from router import route_ticket
from tools import TOOL_MAP


DEFAULT_TICKET = "Claim submission modal does not open after clicking submit button."


def execute_ticket(ticket: str) -> dict:
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

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the AI QA routing demo.")
    parser.add_argument(
        "ticket",
        nargs="?",
        default=DEFAULT_TICKET,
        help="Jira ticket text to route.",
    )
    args = parser.parse_args()
    execute_ticket(args.ticket)


if __name__ == "__main__":
    main()
