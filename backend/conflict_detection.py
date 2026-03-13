def conflict_score(reports):

    events = set()

    for r in reports:
        events.add(r["event_type"])

    if len(events) > 1:
        return 1
    else:
        return 0