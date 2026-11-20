# Content Research Note — 2026-11-20

**Focus**: Content pipelines for multi-viewer glasses-free 3D — recent advances in 2D-to-3D conversion, crosstalk reduction, per-viewer / real-time multi-view rendering, and computational pre-correction.

## Research Summary

### 1. Lightweight Multiplane Images Network (LMPIN) for real-time planar-to-stereo conversion (Diao et al., arXiv:2412.03102, Dec 2024)
- **Key takeaway**: MPI-based network with a lightweight depth-semantic branch that implicitly extracts depth-aware features (no explicit monocular depth network at inference). Uses a heavy-training / light-inference strategy with a coarse-to-fine auxiliary branch present only during training. Simplified MPI rendering yields comparable subjective quality to TMPI / ADAMPI while delivering >40× inference speedup and real-time performance at 2K resolution.
- **Relevance**: Efficient 2D-to-3D conversion stage that can feed candidate views into the per-viewer selection and allocation layers without heavy depth estimation overhead. Suitable for live or recorded planar content.
- **Reference**: https://arxiv.org/abs/2412.03102

### 2. Artifact-free crosstalk reduction via adaptive multi-view correlation filters (Lim, Jeon, Lee & Kim, Optica Open preprint, Sep 2024)
- **Key takeaway**: Inter-view crosstalk is mitigated by an optimized reduction filter chosen adaptively per pixel according to the correlation between neighboring light-field views. Avoids the color overshoot artifacts common in conventional crosstalk cancellation. Prototype measurements show ~20.4% better crosstalk reduction than prior methods without introducing out-of-range values.
- **Relevance**: Practical computational pre-correction that can be applied after view generation or interleaving. The correlation-driven adaptation is especially useful in multi-viewer settings where residual leakage between allocated views must be suppressed without degrading color fidelity.
- **Reference**: Optica Open preprint (figshare/Optica Open ID 27109210)

### 3. Real-time super-multiview rendering inside standard game engines (Qin et al., Optics and Lasers in Engineering / SPIE 2025–2026)
- **Key takeaway**: Demonstrates equivalence between viewpoint generation and voxel lookup for SMV / integral-imaging displays. A voxel-pixel LUT is stored as an additional texture and consumed by a post-process shader, replacing repeated draw calls with simple texture fetches. Combined with an eye-tracking-driven virtual lens-shift, the method extends the usable viewing angle beyond ±30° without crosstalk and achieves 60 fps on a 4K SMV prototype (liquid-crystal lenticular) using a laptop-class RTX 4090 and Unreal Engine.
- **Relevance**: Engine-native path for generating dense multi-view content on demand. Directly supports per-viewer rendering by shifting the effective lens according to tracked eye positions, reducing the need for a large static candidate set.
- **Reference**: Qin et al., Optics and Lasers in Engineering 204, 109855 (2026); SPIE Advances in Display Technologies XV (2025).

### 4. Joint computational encoding + dual-plane lens optimization for higher spatial/angular resolution (Scienmag summary of recent optical engineering work, Nov 2026)
- **Key takeaway**: Subpixel-demultiplexing viewpoint-interleaving encoding paired with full-field dual-plane lens optimization produces an aliasing-free effective subpixel array (example: 4320 × 3840) and improves peak spatial resolution 124–152% while maintaining fine angular sampling (~0.69° viewpoint interval). Computational pre-encoding is co-designed with the optical stack.
- **Relevance**: Illustrates how content-side pre-correction / encoding can be jointly optimized with optics to raise both spatial and angular quality—useful when the hardware component later supplies a measured optical model.
- **Reference**: Recent dual-optimization light-field display results (summarized Nov 2026).

## Pseudocode Scaffold Note

The existing `content_pipeline_scaffold.py` already covers the main stages. A useful incremental addition for the adaptive crosstalk technique is a correlation-aware filter stub:

```python
def adaptive_crosstalk_filter(self, views: List[np.ndarray], neighbor_corr_threshold: float = 0.7) -> List[np.ndarray]:
    """
    Placeholder for Lim et al.-style per-pixel adaptive filter.
    Compute local correlation between neighboring views; select a stronger
    or weaker cancellation coefficient so that out-of-range (color overshoot)
    values are avoided.
    """
    corrected = []
    for i, v in enumerate(views):
        # Stub: simple fixed-k compensation; replace with correlation map
        k = 0.05 if i == 0 else 0.08
        # ... apply adaptive inverse model ...
        corrected.append(np.clip(v, 0, 255))
    return corrected
```

This can be inserted after candidate-view generation or after per-viewer selection.

## Next Steps

- Prototype a lightweight LMPIN-style or Depth-Anything + simplified MPI path for the 2D-to-3D stage.
- Add a correlation-map driven crosstalk pre-correction stub that respects measured inter-view leakage from the optical calibration.
- Explore engine-shader LUT rendering for dense views when the allocation layer requests many simultaneous viewpoints.
- Keep all content work isolated to this directory; coordinate only via the shared eye-position interface with tracking and allocation.
