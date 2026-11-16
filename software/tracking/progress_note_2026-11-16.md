# Tracking Research Note — 2026-11-16

**Focus**: Multi-person face/eye tracking, pose estimation, short-horizon prediction, and sensor fusion relevant to multi-viewer autostereoscopic (glasses-free 3D) displays.

This note stays strictly inside the Tracking Warden boundary. It feeds 3D eye positions (and predicted positions) to the allocation and content layers.

## Research Summary (2–4 useful advances)

### 1. AI-assisted retinal projection with eye-motion prediction (Lin et al., iOptics 2026)
- **Key takeaways**: Combines retina-resolved imaging with AI-based eye localization (pupil centers treated as retinal centers), noise suppression on eye-tracker signals, and real-time eye-motion prediction. Compensates end-to-end latency in a time-sequential directional-backlight autostereoscopic display. Supports a seamless viewing zone while preserving full panel resolution per eye; substantially reduces ghost images during viewer movement. Demonstrated on desktop-scale hardware with both motion phantoms and human subjects.
- **Relevance**: Latency-aware prediction of retinal / eye position is critical for stable multi-viewer 3D without ghosting. AI prediction can be layered on top of classical trackers. Directly applicable to directional or light-field systems that must steer light to moving eyes.
- **Reference**: Lin et al., *AI-powered retinal projection for immersive autostereoscopic display*, iOptics 2(1):100030 (2026). DOI: 10.1016/j.iopt.2026.100030

### 2. Hybrid low-latency multi-viewer eye tracking for light-field displays (Lu et al., SID 2026)
- **Key takeaways**: Hybrid pipeline (neural detection + optical flow + Kalman filtering + interpupillary-distance (IPD) based yaw estimation). Embedded in a light-field prototype: tracking latency <10 ms, end-to-end motion-to-photon latency <20 ms, range up to 4.5 m, 360° coverage. Explicitly addresses latency limitations of pure neural models for multi-viewer scenarios at distance.
- **Relevance**: Practical hybrid design that meets perceptual tolerances for motion disparity. Kalman + optical flow is a lightweight way to add prediction and smooth multi-person tracks. IPD-based yaw helps with head orientation without full pose solvers.
- **Reference**: Lu et al., *A Real-Time Eye Tracking System for Man-to-Machine Interaction on Light Field Display*, SID Symposium Digest (2026). DOI: 10.1002/sdtp.70003_11

### 3. Gaze-aware inverse light-field mapping with decoupled tracking (Su et al., J. Russ. Laser Res. 2026)
- **Key takeaways**: Decouples real-time gaze tracking from inverse light-field mapping into parallel threads. Depth-camera video is processed by a deep neural network to localize 3D eye coordinates in real time; the mapping thread uses those coordinates to build an inverse model from elemental images to the scene. Eliminates pixel holes at depth discontinuities that appear in classical algorithms and scales better with resolution (speedup ~1.15–1.20× when resolution doubles).
- **Relevance**: Clean separation of tracking (sensor fusion + DNN localization) from content generation. Useful architectural pattern for multi-viewer systems: keep tracking fast and independent, then feed stable 3D eye positions downstream.
- **Reference**: Su et al., *Gaze-Aware inverse light field mapping for autostereoscopic displays*, Journal of Russian Laser Research 47:250–263 (2026). DOI: 10.1007/s10946-026-10297-2

### 4. Real-time multi-view multi-person markerless motion capture (survey, Nagorny et al. 2025)
- **Key takeaways**: Systematic review (2020–2024) of real-time markerless systems. Neural 2D/3D pose estimation now enables ≥25 FPS multi-person multi-view tracking. Evaluated on accuracy, end-to-end latency, and computational efficiency; architectural choices (top-down, bottom-up, voxel-based) strongly affect scalability with number of cameras and people. Remaining challenges include optimal trade-offs and robust handling of occlusions / extreme poses.
- **Relevance**: Provides the broader sensor-fusion and multi-camera foundation. For a large multi-viewer display, fusing several RGB or RGB-D cameras with modern pose estimators is a viable path to robust 3D eye / head positions.
- **Reference**: Nagorny et al., *A Comprehensive Review of Real-Time Multi-View Multi-Person Markerless Motion Capture*, ACM Computing Surveys (2025). DOI: 10.1145/3757733

## Code Scaffold / Pseudocode Note

The existing `multi_viewer_tracker_scaffold.py` already provides a minimal OpenCV + MediaPipe multi-face pipeline with nearest-neighbor association and constant-velocity prediction. A useful next incremental improvement is a lightweight Kalman filter for smoother 3D eye positions and better short-horizon prediction (aligns with the hybrid systems above).

**Simple 3D Kalman prediction sketch (Python / NumPy style):**
```python
# Per-viewer state: [x, y, z, vx, vy, vz]
# Constant-velocity model; measurement = eye-center 3D position

class SimpleEyeKalman:
    def __init__(self, dt=0.033):
        self.dt = dt
        # State transition (constant velocity)
        self.F = np.eye(6)
        self.F[0,3] = self.F[1,4] = self.F[2,5] = dt
        # Process / measurement noise (tune empirically)
        self.Q = np.eye(6) * 1e-4
        self.R = np.eye(3) * 1e-3
        self.H = np.hstack([np.eye(3), np.zeros((3,3))])
        self.x = np.zeros(6)
        self.P = np.eye(6)

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q
        return self.x[:3]

    def update(self, z):
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(6) - K @ self.H) @ self.P
        return self.x[:3]
```

Drop this (or a filterpy / OpenCV KalmanFilter equivalent) into the existing scaffold’s per-ID track dictionary. Predict 20–50 ms ahead for latency compensation; keep association simple (IoU or Euclidean on predicted positions) until multi-camera fusion is added.

## Next Steps (tracking only)

- Integrate a Kalman (or similar) predictor into the scaffold and measure latency vs. accuracy on multi-person sequences.
- Explore depth-camera or multi-view fusion for true 3D eye positions (building on the Su and multi-view survey results).
- Evaluate hybrid neural + classical pipelines for multi-viewer range and robustness.

No changes outside the tracking component.
