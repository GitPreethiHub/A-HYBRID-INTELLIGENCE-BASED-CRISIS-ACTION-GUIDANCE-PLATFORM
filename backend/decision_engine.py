def decision_score(severity, reliability, conflict):

    severity_weight = 0.5
    reliability_weight = 0.3
    conflict_penalty = 0.2

    score = (
        severity_weight * severity +
        reliability_weight * reliability -
        conflict_penalty * conflict
    )

    return score
def alert_level(score):

    if score >= 6:
        return "HIGH"

    elif score >= 3:
        return "MEDIUM"

    else:
        return "LOW"
def action_state(score):

    if score <= 2:
        return "SAFE TO STAY"

    elif score <= 4:
        return "SAFE TO MOVE"

    elif score <= 6:
        return "WAIT FOR UPDATE"

    else:
        return "AVOID AREA"