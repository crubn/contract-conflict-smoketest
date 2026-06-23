# negative control: call site updated to NEW signature
from payments import charge


def run_checkout():
    return charge(100, "usd")
