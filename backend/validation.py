import time

def remove_expired_reports(reports):

    valid_reports = []

    now = time.time()

    for r in reports:

        expiry_time = r["timestamp"] + r["ttl"]

        if now <= expiry_time:
            valid_reports.append(r)

    return valid_reports