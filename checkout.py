from payments import charge


def run_checkout():
    return charge(100)
# hop-e trigger: re-run zar/contract-conflicts check (no logic change; charge(100) untouched)
# trigger: re-run zar/contract-conflicts (no logic change; charge(100) untouched)
