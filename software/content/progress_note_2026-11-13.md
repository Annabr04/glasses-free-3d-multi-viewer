# Content Research Note — 2026-11-13

**Focus**: Content pipelines for multi-viewer glasses-free 3D — 2D-to-3D conversion, multi-view / disparity generation, crosstalk reduction, per-viewer rendering, and computational pre-correction.

## Research Summary

### 1. Multi-view glasses-free 3D content generation via Gaussian Splatting (Zheng et al., SID 2025 / JSID 2026)
- **Key takeaway**: Reconstruct a real-world scene with 3D Gaussian Splatting from sparse captures, then insert a virtual off-axis camera array to render a dense set of disparity images. These are synthesized into the elemental image array for a lenticular + LCD autostereoscopic display. Avoids physical multi-camera rigs.
- **Relevance**: Practical content pipeline for turning ordinary 2D/sparse captures into multi-view content suitable for glasses-free displays. Explicit 3DGS representation makes it easy to re-render views on demand for tracked viewer positions.
- **Reference**: Zheng et al., SID Symposium Digest / Journal of the Society for Information Display. DOI: 10.1002/jsid.70037 / 10.1002/sdtp.18869

### 2. EyeReal — real-time per-viewer light-field synthesis (Ma et al., Nature 2025)
- **Key takeaway**: Deep-learning engine that, given tracked binocular eye positions, optimally allocates the limited space-bandwidth product of a stacked-LCD light-field display around the eyes. Produces full-parallax (stereo + motion + focal) imagery at >50 Hz / 1080p with >100° seamless viewing range without specialized optics.
- **Relevance**: Canonical computational per-viewer rendering approach. Multi-viewer extension can time-multiplex or spatially partition the optimization across tracked eye pairs supplied by the tracking component.
- **Reference**: Ma et al., Nature 648, 76–83 (2025). Code: https://github.com/WeijieMax/EyeReal

### 3. Semi-physical neural-network pre-correction for achromatic, crosstalk-free light-field 3D (Zhou et al., Advanced Photonics Nexus 2026)
- **Key takeaway**: Device-specific calibration maps (pixel-level crosstalk and chromatic dispersion) are baked into a semi-physical neural network. The network pre-distorts the elemental image array so that, after the imperfect optics, the viewer sees reduced crosstalk (~36% average reduction) and chromatism (~39% reduction) with no extra hardware.
- **Relevance**: Software-only computational pre-correction that can sit at the end of any content pipeline. One-time measurement + fast inference makes it practical for multi-viewer systems where residual optical crosstalk must be suppressed.
- **Reference**: Zhou et al., Advanced Photonics Nexus 5(6), 066005 (2026).

### 4. Real-time monocular 2D-to-3DGS for glasses-free telepresence (MonoFlex3D, ACM 2025) and related depth-AI pipelines
- **Key takeaway**: Compositional 3D Gaussian Splatting (body + face templates) driven from a single commodity RGB camera yields high-fidelity, low-latency (~100 ms end-to-end) glasses-free 3D teleconference. Complementary commercial/research pipelines use monocular depth-estimation models (CNN/ViT) to convert ordinary 2D video into left/right views on the fly, synchronized with eye tracking for lenticular or directional-backlight displays.
- **Relevance**: Lightweight 2D-to-3D conversion suitable for live or recorded content. Feeds cleanly into the allocation layer once per-viewer views are selected.
- **Reference**: MonoFlex3D, Proceedings of the 3rd ACM Workshop on Mobile Immersive Computing (2025). Related depth-AI + eye-tracking signage demos (2026).

## Code Scaffold

See `content_pipeline_scaffold.py` in this directory for a minimal Python scaffold. It sketches the main stages: optional monocular depth estimation → multi-view / stereo pair generation (or 3DGS virtual cameras) → per-viewer view selection from tracked eye positions → simple computational pre-correction / crosstalk compensation → output of interleaved elemental images ready for the allocation stage.

## Next Steps

Integrate with tracking (3D eye positions) and allocation (view mapping); prototype a lightweight depth-to-disparity path; add a simple measured-crosstalk lookup or CNN pre-correction stub; evaluate multi-viewer consistency and residual crosstalk under motion.
