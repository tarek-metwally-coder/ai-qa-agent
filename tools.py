def claim_submission_test():
    print("Running claim submission Playwright test...")


def login_test():
    print("Running login Playwright test...")


def payment_flow_test():
    print("Running payment flow Playwright test...")


TOOL_MAP = {
    "claim_submission_test": claim_submission_test,
    "login_test": login_test,
    "payment_flow_test": payment_flow_test,
}

ALLOWED_TOOLS = [
    "claim_submission_test",
    "login_test",
    "payment_flow_test",
    "unknown",
]