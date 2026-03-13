# Hybrid Intelligence Based Crisis Action Guidance Platform

A decision-support platform designed to assist human operators during crisis situations by transforming uncertain multi-source information into clear zone-level guidance.

The system combines **human intelligence** (reports from authorities, NGOs, social media, or operators) with **algorithmic reasoning** to produce safe and explainable crisis recommendations.

---

# Project Overview

During emergencies, people often face conflicting and incomplete information from multiple sources.
This platform aggregates those updates and generates **conservative guidance decisions** for affected zones.

Instead of presenting dozens of raw reports, the system produces **clear actionable instructions** such as:

* SAFE TO MOVE
* CAUTION
* WAIT FOR UPDATE

The goal is to **reduce information overload and support safer decisions during crises.**

---

# Key Features

## Hybrid Intelligence Architecture

Combines human-generated reports with automated reasoning.

## Multi-Source Data Integration

Supports data from:

* Government alerts
* NGOs
* Social media reports
* Human operator input
* Simulated crisis feeds

## Reliability Evaluation

Different sources have different credibility levels.
The system weights each report accordingly.

## Conflict Detection

Conflicting reports increase uncertainty and influence decisions.

## Temporal Validity

Reports expire after a defined time window to prevent outdated information from affecting guidance.

## Risk Scoring Engine

Each report contributes to a zone risk score using severity, reliability, and conflict factors.

## Conservative Decision Logic

Zone decisions prioritize safety using deterministic rules.

## Interactive Dashboard

A web-based interface displays:

* Zone status
* Crisis map
* Decision timeline
* Live activity feed
* Human report submission

---

# System Architecture

<img width="1536" height="631" alt="architecture" src="https://github.com/user-attachments/assets/01853c28-1eb5-4c94-92fe-27840df13729" />

```
Crisis Data Sources
        ↓
Data Validation
        ↓
Temporal Filtering
        ↓
Reliability Evaluation
        ↓
Conflict Detection
        ↓
Risk Scoring Engine
        ↓
Zone Aggregation
        ↓
Decision Engine
        ↓
Dashboard Visualization
```


---

# Technology Stack

## Backend

* Python
* FastAPI

## Frontend

* HTML
* CSS
* JavaScript
* Leaflet.js (Map visualization)
* Chart.js (Timeline graphs)

## Data Storage

* JSON-based data storage

---

# Project Structure

```
backend/
│
├── main.py
├── decision_engine.py
├── confidence.py
├── conflict_detection.py
├── validation.py
└── simulator.py

frontend/
│
└── dashboard.html

data/
│
├── reports.json
└── history.json
```

---

# Running the System

## Install Dependencies

```
pip install fastapi uvicorn
```

## Start the Backend

```
python -m uvicorn main:app --reload
```

## Open the Dashboard

```
http://127.0.0.1:8000/dashboard
```

---

# Dashboard

<img width="1919" height="966" alt="image" src="https://github.com/user-attachments/assets/98e2296d-9e18-4154-b583-bb3f5c2cc430" />


* Crisis Map showing zone-level alerts
* Live crisis activity feed
* Decision score timeline
* Human operator reporting panel
* Zone guidance display

---

# Output
## Crisis Map

<img width="1884" height="956" alt="image" src="https://github.com/user-attachments/assets/26dbed02-c335-48ee-9fa4-4f5065461ce8" />

## Field report and Decision Timeline

<img width="1897" height="972" alt="image" src="https://github.com/user-attachments/assets/01f10ffa-2178-4d0e-a65e-d0f490c6ebee" />

---

# Ethical Design Considerations

The system avoids sensitive data collection and does not use:

* personal identifiers
* biometric tracking
* predictive behavioral profiling

The focus is **transparent and explainable decision support.**

---

# Future Improvements

Possible extensions include:

* real-time data integration from external APIs
* geospatial risk heatmaps
* mobile crisis reporting interface
* automated anomaly detection
* advanced uncertainty modeling

---

# License

This project is intended for academic and research purposes.
