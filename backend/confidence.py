source_weights = {
    "government": 1.0,
    "emergency": 0.9,
    "ngo": 0.7,
    "local": 0.6,
    "social_media": 0.4,
    "human_operator": 0.95
}
def weighted_confidence(reports):

    total_weight = 0
    weighted_sum = 0

    for r in reports:

        weight = source_weights.get(r["source"], 0.5)

        weighted_sum += weight * r["confidence"]
        total_weight += weight

    if total_weight == 0:
        return 0

    return weighted_sum / total_weight