# Content Research Note — 2026-11-27

**Focus**: Content pipelines for multi-viewer glasses-free 3D — recent advances in 2D-to-3D conversion, crosstalk reduction, per-viewer / real-time multi-view rendering, and computational pre-correction.

## Research Summary

### 1. Ref2Light: Feed-forward interactive light-field characters from a single image (Zhang, Wang & Song, arXiv:2611.29678, Nov 2026)
- **Key takeaway**: Maps a single A-pose illustration plus continuous pose/expression controls to display-native light-field animation without per-character 3D reconstruction, rigging, or test-time optimization. Decomposes synthesis into static identity (cached multi-scale features), view-dependent parallax (ordered angular anchors), and control-driven articulation. Calibrated differentiable subpixel interlacing produces the native panel raster for end-to-end supervision. Achieves 34–40 FPS on 1440×2560 rasters and substantially better LPIPS / expression fidelity than 2D/3D baselines.
- **Relevance**: Direct content pipeline for dynamic character content that outputs display-ready multi-view / light-field rasters. Supports rapid character switching and real-time pose control, ideal for multi-viewer interactive experiences.
- **Reference**: https://arxiv.org/abs/2611.29678

### 2. EyeReal: Per-viewer real-time light-field optimization with deep learning (Ma et al., Nature, Nov 2025)
- **Key takeaway**: Desktop-scale full-parallax glasses-free 3D display with seamless viewing >100° at >50 Hz and 1920×1080. Uses accurate binocular modeling + a lightweight CNN that generates optimal layered phase patterns only around the tracked eyes (exploiting limited space-bandwidth product). Stacked LCD panels + RGB-D eye tracking; no specialized optics required. Delivers stereo, motion, and focal parallax.
- **Relevance**: Strong example of computational per-viewer rendering and pre-correction: content is optimized in real time for specific eye positions rather than broadcasting dense views. The eye-position interface aligns directly with our multi-viewer allocation layer.
- **Reference**: https://www.nature.com/articles/s41586-025-09752-y

### 3. Low-cost precompensation for crosstalk suppression in naked-eye 3D (Zhu et al., SID Digest 2026)
- **Key takeaway**: Precompensation algorithm reduces crosstalk from ~4% to below 2% on 4K binocular cylindrical-lens devices without added hardware cost or modification. Addresses the classic trade-off between crosstalk reduction, cost, and refresh rate.
- **Relevance**: Practical computational pre-correction stage that can be applied after view generation or interleaving. Complements earlier adaptive-filter approaches and is suitable for measured optical leakage models.
- **Reference**: SID Symposium Digest of Technical Papers, Vol. 57, 2026 (e.g., 79-2 / 86-1).

### 4. Cascaded light-field propagation: turning crosstalk into signal for continuous volumetric holography (Gan, Yang et al., Nature Photonics, Sep 2026)
- **Key takeaway**: Instead of suppressing interplane crosstalk, the method reuses the outgoing field from each projection plane as constructive input for subsequent planes. Physics-embedded untrained network (Holo-Prior-Net) designs holograms that produce axially and laterally continuous free-space 3D projections with a single SLM. Demonstrated on continuous DNA helix, cylinders, and spheres.
- **Relevance**: Conceptual advance for content generation in volumetric or holographic glasses-free systems. Suggests joint design of content and propagation rather than independent per-plane compensation; useful when the hardware component supplies a propagation model.
- **Reference**: https://www.nature.com/articles/s41566-026-02016-9

## Pseudocode Scaffold Note

Useful incremental addition for display-native light-field output (inspired by Ref2Light-style anchor + interlacing):

```python
def synthesize_display_native_raster(
    identity_features: np.ndarray,
    pose_expr_controls: dict,
    angular_anchors: int = 12,
    optical_calibration: dict = None,
) -> np.ndarray:
    """
    Stub for feed-forward light-field synthesis to native panel raster.
    1. Decode ordered angular anchor views from identity + controls.
    2. Apply calibrated subpixel interlacing (view-to-subpixel mapping).
    Returns the interleaved elemental image ready for the allocation layer.
    """
    # anchors = decoder(identity_features, pose_expr_controls)  # list of views
    # raster = subpixel_interlace(anchors, optical_calibration)
    # return raster
    return np.zeros((1080, 1920, 3), dtype=np.uint8)  # placeholder
```

This can sit after candidate-view generation when the target is a light-field panel rather than simple left/right pairs.

## Next Steps

- Evaluate feed-forward single-image to multi-view / light-field paths (Ref2Light-style or 3DGS-based) for the 2D-to-3D stage.
- Prototype real-time per-viewer light-field optimization using tracked eye positions (EyeReal-inspired), keeping the interface limited to eye coordinates.
- Integrate a measured-crosstalk precompensation module (Zhu-style or correlation-adaptive) after interleaving.
- Keep all content work isolated to this directory; coordinate only via the shared eye-position interface with tracking and allocation.
