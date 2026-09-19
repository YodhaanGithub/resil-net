# RESIL-NET

RESIL-NET is a disaster-resilience command dashboard for exploring evacuation
corridors across Guwahati's 15-sector metropolitan grid. The map is a dark
MapLibre/Esri canvas surrounded by a calmer light operations shell so risk
geometry, bottlenecks, and active routes remain easy to parse.

## What is included

- MapLibre GL map centered on Guwahati with Esri World Dark Gray tiles
- 15 hardcoded Guwahati sectors, road mesh, flood epicenter, safe havens, and
  critical chokepoints
- Five generative corridor blueprints with live selection and budget gating
- Scenario controls for flood radius, infrastructure cap, constraints, and
  historic baseline loading
- Monte Carlo run overlay backed by Flask API endpoints
- GeoJSON and simulated shapefile export actions
- Responsive shell for tablet and field-device widths

## Run locally

```bash
python -m pip install -r requirements.txt
python main.py
```

Open `http://localhost:8080`.

## API

- `GET /api/status`
- `GET /api/corridors`
- `GET /api/scenarios`
- `POST /api/simulate`
- `POST /api/metrics`

The map uses public Esri raster tiles and requires no API key.