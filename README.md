# glasses-free-3d-multi-viewer

Structured foundation for multi-viewer glasses-free 3D (autostereoscopic) systems.

You invent. The system supplies research sparks, code scaffolds, issue quarantine, progress organization, and packaging.

## Blueprint

### Software Side First (Three Equal Parts — the Wardens)
1. **Tracking Warden** — Multi-person face/eye tracking, pose estimation, prediction, sensor fusion.
2. **Allocation Warden** — View allocation, light-field optimization, interleaving based on tracked positions.
3. **Content Warden** — Content pipeline, 2D-to-3D helpers, crosstalk reduction, per-viewer rendering.

### Guards (15 total — 5 dedicated to each Warden)
Each warden has five specialized guards that quarantine issues, research, scaffolds, status, and boundaries so nothing spills across areas.

#### Tracking Warden Guards
- Tracking Guard
- Tracking Research Guard
- Tracking Scaffold Guard
- Tracking Issue Guard
- Tracking Status Guard

#### Allocation Warden Guards
- Allocation Guard
- Allocation Research Guard
- Allocation Scaffold Guard
- Allocation Issue Guard
- Allocation Status Guard

#### Content Warden Guards
- Content Guard
- Content Research Guard
- Content Scaffold Guard
- Content Issue Guard
- Content Status Guard

### Sequence
1. Software pieces accumulate research notes, scaffolds, and issues in this repo.
2. Wardens and guards retarget to the hardware side (directional optics, freeform/metasurface support, calibration & compensation).
3. Package software side and hardware side as clean, documented modules.

## Structure
- `software/` — tracking, allocation, content
- `hardware/` — future optics, backlight, calibration
- `issues/` — quarantined problem notes (mirrored from GitHub issues)
- `packages/` — final packaged outputs
- `GUARDS.md` — full guard roster and duties

Progress is deliberate. No rushing. The plan guides the path.
