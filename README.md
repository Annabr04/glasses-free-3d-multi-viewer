# Multi-Viewer Glasses-Free 3D

Research and prototype foundation for multi-viewer autostereoscopic (glasses-free 3D) display systems.

The project aims to enable multiple simultaneous viewers to experience correct stereoscopic imagery without glasses. This is achieved by combining real-time multi-person tracking with dynamic view allocation and content generation.

## Project Structure

- `software/tracking/` — Multi-person face and eye tracking, pose estimation, prediction, and sensor fusion. Supplies 3D viewer positions to other components.
- `software/allocation/` — View allocation, light-field optimization, and interleaving based on tracked positions.
- `software/content/` — Content pipeline, 2D-to-3D conversion helpers, crosstalk reduction, and per-viewer rendering.
- `hardware/` — Future work on directional optics, backlight design, calibration, and compensation.
- `packages/` — Packaged software and hardware modules once components are mature.

## Current Status

Software foundations are under development. Tracking research notes and a basic multi-viewer tracker scaffold are available under `software/tracking/`.

## Contributing

Research notes, code scaffolds, and implementation work are welcome in the appropriate subdirectory. Please keep changes focused on the relevant component.
