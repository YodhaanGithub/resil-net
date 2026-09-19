---
name: Resil-Net Disaster Resilience HUD
colors:
  surface: '#10131a'
  surface-dim: '#10131a'
  surface-bright: '#363941'
  surface-container-lowest: '#0b0e15'
  surface-container-low: '#191b23'
  surface-container: '#1d1f27'
  surface-container-high: '#272a32'
  surface-container-highest: '#32353d'
  on-surface: '#e1e2ec'
  on-surface-variant: '#bbc9cf'
  inverse-surface: '#e1e2ec'
  inverse-on-surface: '#2d3038'
  outline: '#859399'
  outline-variant: '#3c494e'
  surface-tint: '#47d6ff'
  primary: '#a5e7ff'
  on-primary: '#003543'
  primary-container: '#00d2ff'
  on-primary-container: '#00566a'
  inverse-primary: '#00677f'
  secondary: '#aec6ff'
  on-secondary: '#002e6b'
  secondary-container: '#508eff'
  on-secondary-container: '#00275e'
  tertiary: '#69f6b9'
  on-tertiary: '#003824'
  tertiary-container: '#48d99e'
  on-tertiary-container: '#005b3d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b6ebff'
  primary-fixed-dim: '#47d6ff'
  on-primary-fixed: '#001f28'
  on-primary-fixed-variant: '#004e60'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#aec6ff'
  on-secondary-fixed: '#001a43'
  on-secondary-fixed-variant: '#004397'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#10131a'
  on-background: '#e1e2ec'
  surface-variant: '#32353d'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.03em
  headline-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  title-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  mono-data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.02em
  mono-data-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0em
  label-mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 0.75rem
  gutter-mobile: 0.5rem
  margin: 1rem
  margin-mobile: 0.75rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1.25rem
  space-xl: 2rem
---

## Brand & Style

This design system synthesizes the mission-critical ergonomics of aerospace radar stations and air traffic management with computational geographic information systems (GIS). It serves computational cartographers, municipal disaster mitigation leads, and civil infrastructure engineers who must parse dense topological risk surfaces and execute predictive Monte Carlo simulation sweeps in time-sensitive conditions.

The visual tone is analytical, vigilant, and engineered. Surfaces rely on deep obsidian tonal depth layered under luminous, high-chroma vector accents. High-contrast signaling cuts through dense visual telemetry without decorative noise, evoking absolute operational command and mathematical certainty.

## Colors

The palette operates under a calibrated dark regime structured for 24/7 dark-room operations and spatial mapping environments:

- **Primary Canvas & Structural Surfaces**: Deep obsidian `#0A0D14` forms the master canvas foundation. Intermediate monitoring decks, collapsible drawers, and panel surfaces scale upward into `#0F141F` and `#161D2E`. Ghost structure lines and structural panel dividers use `#232D42`.
- **Primary & Secondary Emissive Accents**: Electric Cyan (`#00D2FF`) drives simulation nodes, active flow conduits, and dynamic vectors. Cobalt Velocity (`#0070F3`) handles secondary spatial vectors, timeline scrubbers, and focused telemetry clusters.
- **Alert & State Tokens**: Hazard Red (`#FF3B5C`) isolates breach thresholds, infrastructure failures, and emergency choke zones. Resilient Emerald (`#10B981`) denotes structural survivability, power-grid stability, and cleared evacuation pathways.
- **Telemetry Typography**: Technical labels, sensor IDs, and coordinate headers use tactical muted steel (`#8E9AA8`), shifting to crisp operational slate (`#CAD5E2`) for active values.

## Typography

The typographic hierarchy enforces strict domain division:
1. **Space Grotesk** governs structural titles, viewport mode indicators, and simulation run identifiers, providing angular industrial character without compromising legibility.
2. **Inter** manages descriptive system logs, spatial documentation, incident reports, and conversational annotations.
3. **JetBrains Mono** powers all numerical readouts, latitude/longitude matrices, network throughputs, probabilistic variance scores, and HUD status labels. All label tokens must be displayed in uppercase with open tracking to facilitate zero-latency recognition during high-stress operational reviews.

## Layout & Spacing

This design system uses an edge-to-edge spatial canvas model with absolute screen maximization. The layout prioritizes continuous geospatial viewports over traditional paginated layouts.

- **Grid Framework**: 16-column flexible layout grid for ultra-wide command stations, scaling down to a condensed 8-column layout on standard displays, and a 4-column columnated stack on field devices.
- **HUD Shell Architecture**: The layout centers on a continuous underlying map/simulation layer. Side telemetry panels, top-level flight-deck navigation, and bottom scenario timeline bars hover above the canvas with persistent zero-margin docking boundaries.
- **Density Profile**: Compact vertical and horizontal rhythms prioritize high information density, maintaining visual separation through razor-sharp boundaries rather than exaggerated negative space.

## Elevation & Depth

Visual hierarchy uses physical optical layering rather than diffuse blur-shadows, matching radar terminal displays:

- **Level 0 (Map Canvas Ground)**: Raw map topology, spatial risk geometry, and Monte Carlo point clouds rendered over `#0A0D14`.
- **Level 1 (Docked Consoles & Drawers)**: Opaque slate `#0F141F` surfaced with hairline `#232D42` boundaries. Provides solid isolation for persistent instrument panels.
- **Level 2 (HUD Floating Overlays & Cards)**: Translucent, frosted glassmorphic containers using `#161D2E` at 82% opacity with a `backdrop-filter: blur(12px) saturate(180%)`. Border treatment: 1px solid `rgba(0, 210, 255, 0.15)`.
- **Level 3 (Tactical Popovers & Critical Interrupters)**: `#0F141F` backing surrounded by directional 1px perimeter hazard glow using `0 0 16px rgba(255, 59, 92, 0.25)` for alerts, or `0 0 16px rgba(0, 210, 255, 0.25)` for standard focused telemetry.

## Shapes

Corner radii adhere strictly to industrial micro-fillets (`roundedness: 1`, 0.25rem / 4px base). Elements avoid sweeping pill treatments to maintain the geometry of calibrated hardware instruments. Precision telemetry metrics, status pins, and coordinate tags may incorporate 45-degree chamfered edges on outer terminal cards to evoke physical aviation consoles.

## Components

### Action Buttons
- **Primary Execution (Simulation/Trigger)**: Background in solid Cyan `#00D2FF`, label in obsidian `#0A0D14` set in Space Grotesk Bold, 4px corner radius. On hover, produces a soft cyan laser edge (`box-shadow: 0 0 12px rgba(0, 210, 255, 0.5)`).
- **Secondary (Telemetry/Query)**: Transparent background, 1px perimeter border `#232D42`, text `#CAD5E2`. Hover shifts border to `#00D2FF` and text to `#FFFFFF`.
- **Destructive/Emergency**: Background tinted Hazard Red (`rgba(255, 59, 92, 0.15)`), 1px solid border `#FF3B5C`, text `#FF3B5C`.

### Sensor & Scenario Chips
- Compact dimensions: Height 22px, padding 2px 8px.
- Background `rgba(15, 20, 31, 0.85)` with 1px border. Status dot (4px circle) pulsing with `#10B981` (Nominal), `#00D2FF` (Simulating), or `#FF3B5C` (Critical). Text set in `label-mono-sm`.

### HUD Overlay Cards & Floating Telemetry
- Border-box construction with `backdrop-filter: blur(12px)`. Hairline 1px border `#232D42` with optional illuminated cyan corner notches (4px accent lines in top-left and bottom-right corners).
- Header row strictly standardized: Uppercase monospace category label on left, live latency/telemetry stamp (`04:12:09.4Z`) on right.

### Input Fields & Scrubbers
- **Inputs**: Dark field `#0A0D14`, inset 1px border `#232D42`, typography `JetBrains Mono`. Focus state transitions border to `#00D2FF` with a subtle inner glow.
- **Simulation Timeline Scrubbers**: Track height 2px in `#232D42`. Active Monte Carlo duration band rendered in `#0070F3`. Handle is a razor-edged 8x16px vertical diamond or rectangle with a central `#00D2FF` tick mark.

### Precision Toggles & Selection Arrays
- Segmented radio buttons constructed as continuous multi-cell ribbons; active segment highlighted with `#161D2E` fill, `#00D2FF` bottom highlight bar, and crisp text illumination.
- Boolean switches utilize rectangular toggle beds rather than rounded pills, maintaining the avionics aesthetic.

### Domain-Specific HUD Modules
- **Monte Carlo Probability Gauge**: Vertical linear progress arrays or multi-ringed radar meters featuring step indicators graduated in 5% increments.
- **Node Status Matrix**: Dense tabular data grids with zero cell borders, using row highlight scanners, monospaced tabular numerals, and direct color-coded hazard vector indicators.