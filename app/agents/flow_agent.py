def optimize_queue(state):
    severity = state.get("severity")
    load = state.get("load", 50)

    if severity == "CRITICAL":
        return 1
    elif severity == "URGENT":
        return 2 if load < 70 else 3
    elif severity == "NORMAL":
        return 4
    else:
        return 5