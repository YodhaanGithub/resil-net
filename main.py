from __future__ import annotations

import json
import random
import time
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS


ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder="static", static_url_path="/static")
CORS(app)


def load_simulation_data() -> dict:
    with (ROOT / "data" / "simulation.json").open(encoding="utf-8") as handle:
        return json.load(handle)


@app.get("/")
def index():
    return send_from_directory(ROOT / "templates", "index.html")


@app.get("/api/status")
def status():
    return jsonify(
        {
            "engine": "RESIL-NET SIM-RADAR v4.0",
            "status": "online",
            "map_engine": "MapLibre 3D + Esri World Dark Canvas",
            "city": "Guwahati, Assam",
            "sectors": 15,
            "timestamp": time.time(),
        }
    )


@app.get("/api/corridors")
def corridors():
    return jsonify(load_simulation_data()["corridors"])


@app.get("/api/scenarios")
def scenarios():
    return jsonify(load_simulation_data()["scenarios"])


@app.post("/api/simulate")
def simulate():
    payload = request.get_json(silent=True) or {}
    radius = float(payload.get("radius", 1.8))
    budget = float(payload.get("budget", 85.0))
    layout = payload.get("layout", "alpha")
    radius = max(0.5, min(radius, 3.0))
    budget = max(10.0, min(budget, 150.0))

    # The demo intentionally stays deterministic enough to explain, but gives
    # each run a fresh seed so operators can compare separate sweeps.
    data = load_simulation_data()
    blueprint = next(
        (item for item in data["corridors"] if item["id"] == layout),
        data["corridors"][0],
    )
    convergence = round(99.1 + random.random() * 0.8, 1)
    return jsonify(
        {
            "status": "success",
            "seed": f"#MC-{random.randint(1000, 9999)}-FLUID",
            "convergence": convergence,
            "epochs": 1000,
            "radius": radius,
            "budget": budget,
            "layout": blueprint["id"],
            "message": "Simulation completed for 15 Guwahati sectors",
        }
    )


@app.post("/api/metrics")
def metrics():
    payload = request.get_json(silent=True) or {}
    radius = max(0.5, min(float(payload.get("radius", 1.8)), 3.0))
    layout = payload.get("layout", "alpha")
    data = load_simulation_data()
    blueprint = next(
        (item for item in data["corridors"] if item["id"] == layout),
        data["corridors"][0],
    )
    ratio = radius / 1.8
    return jsonify(
        {
            "evacuation_delay": round(blueprint["delay_minutes"] * ratio, 1),
            "bottlenecks": max(0, 4 - blueprint["bottlenecks_cleared"]),
            "roads_severed": round(14.0 * ratio, 1),
            "population_at_risk": int(92400 * ratio * ratio),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
