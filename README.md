# glasses-free-3d-multi-viewer

Structured foundation for multi-viewer glasses-free 3D (autostereoscopic) systems.

You invent. The system supplies research sparks, code scaffolds, issue quarantine, progress organization, and packaging.

## Blueprint

### Software Side First (Three Equal Parts — the Wardens)
1. **Tracking Warden** — Multi-person face/eye tracking, pose estimation, prediction, sensor fusion.
2. **Allocation Warden** — View allocation, light-field optimization, interleaving based on tracked positions.
3. **Content Warden** — Content pipeline, 2D-to-3D helpers, crosstalk reduction, per-viewer rendering.

### Guards
Five supporting agents quarantine issues, monitor boundaries, track progress, and keep the structure clean so problems stay contained.

### Sequence
1. Software pieces accumulate research notes, scaffolds, and issues in this repo.
2. Wardens and guards retarget to the hardware side (directional optics, freeform/metasurface support, calibration & compensation).
3. Package software side and hardware side as clean, documented modules.

## Structure
- `software/` — tracking, allocation, content
- `hardware/` — future optics, backlight, calibration
- `issues/` — quarantined problem notes (mirrored from GitHub issues)
- `packages/` — final packaged outputs

Progress is deliberate. No rushing. The plan guides the path.
