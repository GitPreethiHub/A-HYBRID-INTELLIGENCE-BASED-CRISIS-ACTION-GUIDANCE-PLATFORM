from fastapi.responses import FileResponse
from fastapi import FastAPI, Body
import json
import time

from confidence import weighted_confidence
from validation import remove_expired_reports
from conflict_detection import conflict_score
from decision_engine import decision_score, action_state
from simulator import add_report

app = FastAPI()

def alert_level(score):

    if score >= 6:
        return "HIGH"

    elif score >= 3:
        return "MEDIUM"

    else:
        return "LOW"

@app.get("/dashboard")
def dashboard():
    return FileResponse("../frontend/dashboard.html")


@app.get("/")
def home():
    return {"message": "Crisis Guidance System Running"}

@app.get("/simulate")
def simulate():

    add_report()

    return {"status": "new report generated"}


@app.get("/decision")
def generate_decision():

    with open("../data/reports.json") as f:
        reports = json.load(f)

    reports = remove_expired_reports(reports)

    zones = {}

    for r in reports:

        location = r["location"]

        if location not in zones:
            zones[location] = []

        zones[location].append(r)

    results = {}

    for zone, zone_reports in zones.items():

        confidence = weighted_confidence(zone_reports)

        conflict = conflict_score(zone_reports)

        scores = []

        for r in zone_reports:

            severity = r["severity"]

            reliability = r["confidence"]

            age = time.time() - r["timestamp"]

            decay = 2.718 ** (-0.0001 * age)

            risk = decision_score(severity, reliability, conflict) * decay

            scores.append(risk)

        # conservative aggregation
        score = max(scores)

        action = action_state(score)

        level = alert_level(score)

        history_entry = {
            "time": time.time(),
            "zone": zone,
            "score": score,
            "action": action
        }

        with open("../data/history.json") as f:
            history = json.load(f)

        history.append(history_entry)

        with open("../data/history.json", "w") as f:
            json.dump(history, f, indent=2)

        
        results[zone] = {
        "confidence": confidence,
        "conflict": conflict,
        "severity": max([r["severity"] for r in zone_reports]),
        "decision_score": score,
        "alert_level": level,
        "recommended_action": action,
        "explanation": {
            "severity_factor": max([r["severity"] for r in zone_reports]),
            "confidence_factor": confidence,
            "conflict_factor": conflict
        }
        }

    return results

@app.get("/history")
def history():

    with open("../data/history.json") as f:
        data = json.load(f)

    return data

@app.get("/reports")
def recent_reports():

    with open("../data/reports.json") as f:
        data = json.load(f)

    return data[-10:]

@app.post("/human-report")
def add_human_report(report: dict = Body(...)):

    required_fields = [
        "location",
        "event_type",
        "severity",
        "confidence"
    ]

    for field in required_fields:
        if field not in report:
            return {"error": f"missing field: {field}"}

    report["source"] = "human_operator"
    report["timestamp"] = time.time()
    report["ttl"] = 21600

    with open("../data/reports.json") as f:
        data = json.load(f)

    data.append(report)

    with open("../data/reports.json","w") as f:
        json.dump(data,f,indent=2)

    return {"status":"human report added"}

@app.post("/override")
def override(zone: str, action: str):

    return {
        "zone": zone,
        "override_action": action,
        "note": "Human operator override applied"
    }