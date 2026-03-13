import random
import json
import time
import uuid

zones = ["Z01", "Z02", "Z03"]

events = ["flood", "wildfire", "storm"]

sources = [
    "government",
    "ngo",
    "local_authority",
    "citizen_report"
]

def generate_report():

    report = {
        "update_id": str(uuid.uuid4()),

        "location": random.choice(zones),

        "event_type": random.choice(events),

        "source": random.choice(sources),

        "severity": random.randint(4, 9),

        "confidence": round(random.uniform(0.4, 0.9), 2),

        "timestamp": time.time(),

        "ttl": 21600,

        "message": "Simulated crisis update"
    }

    return report


def add_report():

    with open("../data/reports.json") as f:
        data = json.load(f)

    data.append(generate_report())

    # keep only the latest 50 reports
    if len(data) > 50:
        data = data[-50:]

    with open("../data/reports.json", "w") as f:
        json.dump(data, f, indent=2)