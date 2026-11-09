# Tracking Warden Progress Note — 2026-11-09

**Focus**: Multi-person face/eye tracking, pose estimation, prediction, and sensor fusion for autostereoscopic (glasses-free 3D) multi-viewer displays.

## Research Summary (2–4 useful advances)

### 1. EyeReal (Nature, 2025) — Dynamic light-field optimization guided by real-time eye tracking
- **Key takeaway**: Desktop-scale full-parallax glasses-free 3D with >100° seamless viewing at >50 Hz / 1080p using stacked LCDs + deep-learning real-time optimization. RGB-D camera tracks pupils/eyes in real time; the network generates optimal light fields only around the current binocular positions (exploiting limited space-bandwidth product). Eye tracking primarily guides directional delivery rather than inventing content.
- **Relevance**: Directly applicable prototype for single-viewer; multi-viewer extension requires robust multi-face tracking + per-viewer light-field allocation. Demonstrates that precise, low-latency 3D eye position is the critical input.
- **Reference**: Ma et al., *Nature* 648, 76–83 (2025). Code: https://github.com/WeijieMax/EyeReal

### 2. Multi-view Gaze Target Estimation (ICCV 2025)
- **Key takeaway**: First multi-view model for gaze target estimation. Fuses information from multiple calibrated cameras (Head Information Aggregation, Uncertainty-based Gaze Selection, Epipolar-based Scene Attention). Significantly outperforms single-view baselines, especially under occlusion or when one view has a clear face. Can estimate gaze in one view using only the person image from another view. Introduces MVGT dataset (13k+ images, 28 subjects, 6 cameras).
- **Relevance**: Multi-camera sensor fusion improves robustness for multi-person scenes where faces may be partially occluded or at extreme angles. Useful foundation for fusing several RGB/RGB-D cameras around a large display.
- **Reference**: Miao et al., arXiv:2508.05857 / ICCV 2025. Project: https://www3.cs.stonybrook.edu/~cvl/multiview_gte.html

### 3. Practical multi-user eye-tracked autostereoscopic systems (SID 2024–2025)
- **Key takeaway**: Several conference papers (e.g., Xu et al. SID 2025; Surman et al. SID 2024; Yuan et al. SID 2025) demonstrate 2-user or multi-person glasses-free 3D using LCD + lenticular/parallax barrier + real-time eye tracking. Techniques include dynamic collimated backlights, spatiotemporal multiplexing, and simple multi-person eye trackers that steer a single stereo pair or multiple views. Viewing zones expanded to tens of degrees with good freedom of movement.
- **Relevance**: Shows mature engineering paths that already combine multi-person tracking with view allocation hardware. Tracking latency and accuracy directly determine crosstalk and usable viewing range.
- **References**: SID Symposium Digest papers on eye-tracked multi-user glasses-free 3D (2024–2025).

### 4. Lightweight multi-person detection + landmark pipelines (YOLO + MediaPipe)
- **Key takeaway**: Hybrid pipelines (YOLOv8/v9/v11 for person/face detection + MediaPipe Face Mesh / Pose / Iris for landmarks and gaze) deliver real-time multi-person face, iris, and head-pose tracking on commodity hardware (often >30–100 FPS on CPU/GPU). Stable ID tracking via IoU or DeepSORT-style association. Depth from RGB-D or monocular estimation can be fused for 3D eye positions. Simple Kalman or constant-velocity prediction reduces perceived latency.
- **Relevance**: Practical starting point for the Tracking Warden. Easy to scaffold, extend with multi-view fusion or IMU/sensor fusion later, and feed 3D eye positions to the Allocation Warden.

## Code Scaffold / Pseudocode Note

See `multi_viewer_tracker_scaffold.py` in this directory for a minimal Python scaffold using OpenCV + MediaPipe (or easy swap to Ultralytics YOLO). It detects multiple faces, extracts approximate eye centers / head pose, applies a simple predictor, and outputs per-viewer 3D positions (placeholder depth). Intended as a clean starting point that stays inside the tracking boundary.

## Status & Boundaries

- Research and scaffold added under `software/tracking/` only.
- No changes to allocation or content areas.
- Issues remain quarantined; a tracking-labeled issue can be opened if further discussion is needed.
- Next suggested steps (tracking only): integrate RGB-D depth, multi-camera fusion, and predictive filtering; evaluate latency vs. accuracy on multi-person datasets.

Progress is deliberate. Tracking stays isolated.
