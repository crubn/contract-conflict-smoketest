# live cross-PR contract-break smoketest trigger (run 1)
from payments import charge


def run_checkout():
    return charge(100)
