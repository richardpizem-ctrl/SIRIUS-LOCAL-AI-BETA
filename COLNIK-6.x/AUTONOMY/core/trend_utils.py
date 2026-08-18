def compute_average(history):
    if not history:
        return 0
    return sum(history) / len(history)

def compute_delta(history):
    if len(history) < 2:
        return 0
    return history[-1] - history[-2]

def compute_trend(history):
    avg = compute_average(history)
    delta = compute_delta(history)

    # Základné prahy – upravíme neskôr
    if delta > 5:
        return "rising"
    elif delta < -5:
        return "falling"
    else:
        return "stable"
 
