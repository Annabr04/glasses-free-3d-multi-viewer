# Allocation Research Note — 2026-11-25

**Focus**: View allocation, light-field optimization, interleaving, and multi-viewer light distribution for autostereoscopic / light-field displays. Receives 3D eye positions from tracking; stays strictly within the allocation boundary. Issues remain quarantined.

## Research Summary (3 useful techniques)

### 1. Forward-model-based non-imaging optimization for lenticular lenses (Chinese Optics Letters, 2026)
- **Key takeaway**: Conventional imaging-based lens design ignores real subpixel emission size and angular distribution. The forward-model approach directly optimizes viewpoint width and evaluates binocular crosstalk at the subpixel level. Demonstrated 78.75% crosstalk reduction at maximum viewing angle when paired with directional backlight.
- **Relevance**: Allocation layer can use the resulting viewpoint-width targets and crosstalk model to decide how densely to pack views around each tracked eye pair and where to place guard bands.
- **Reference**: Liu et al., Chin. Opt. Lett. 24, 023301 (2026). DOI: 10.3788/COL202624.023301

### 2. Triangular-periodicity subpixel arrangement (TPSA) + adaptive light-field encoding (Optics Communications, 2025)
- **Key takeaway**: Rectangular subpixel grids mismatch slanted lenticulars, producing uneven zones and high crosstalk. TPSA + ALE yields geometric matching, static ±22° FOV with crosstalk down to 4.3% (H) / 5.5% (V), and eye-tracking (90 fps) extends effective FOV to ~100° while supporting collaborative horizontal-vertical parallax.
- **Relevance**: Software interleaving pattern that better matches common slanted optics. Adaptive encoding can re-map view indices on the fly from tracked positions without hardware changes.
- **Reference**: Optics Communications 595, 132364 (2025). DOI: 10.1016/j.optcom.2025.132364

### 3. Polarization-dependent deflection metasurface + time-multiplexed switching for angular-resolution doubling (Optics Express, 2025)
- **Key takeaway**: A single physical pixel projects two adjacent views by switching polarization, effectively doubling angular resolution (18 views over ~50° FOV, deflection error <0.2°). Highly collimated backlight keeps inter-view crosstalk low. Proof-of-concept 4-view color panel demonstrated.
- **Relevance**: Allocation can treat the time-multiplexed pair as a single logical viewpoint slot or as two tightly spaced views assigned to nearby eyes, increasing effective density without increasing panel pixel count.
- **Reference**: Optics Express 33, 43837 (2025). DOI: 10.1364/OE.577171

### 4. Angular-aligned lens array + adaptive eye-tracking for dynamic viewing-zone expansion (Optics and Lasers in Engineering, 2025)
- **Key takeaway**: Segmented AALA + compact beam deflector + deep-learning eye tracker steers light only to the currently occupied segments. Viewing zones are designed not to overlap, allowing seamless extension of horizontal FOV while preserving 3D fidelity.
- **Relevance**: Direct multi-viewer light-distribution strategy. Allocation logic selects which pre-generated elemental-image array (or view set) to send to each active AALA segment based on tracked positions.
- **Reference**: Optics and Lasers in Engineering 195, 109219 (2025). DOI: 10.1016/j.optlaseng.2025.109219

## Code Scaffold / Pseudocode Note

Minimal extension to the existing `SimpleViewAllocator` that incorporates viewpoint-width targets and simple zone assignment (inspired by the forward-model and AALA ideas):

```python
# Pseudocode addition inside allocate()
def assign_with_width_and_zones(self, viewers, viewpoint_width_deg=1.2):
    assignments = []
    for v in viewers:
        mid = (v.left_eye_3d + v.right_eye_3d) / 2.0
        angle = np.degrees(np.arctan2(mid[0], mid[2]))
        # Snap to nearest discrete view, then reserve a small guard based on width
        base_idx = int(np.argmin(np.abs(self.view_angles - angle)))
        left_idx = max(0, base_idx - 1)
        right_idx = min(self.num_views - 1, base_idx + 1)
        # Zone = coarse angular bin for multi-viewer light steering
        zone_id = int((angle + 30) // 10)   # example 10° bins
        assignments.append(ViewAssignment(
            viewer_id=v.viewer_id,
            left_view_index=left_idx,
            right_view_index=right_idx,
            interleave_offset=v.viewer_id % 2,
            zone_id=zone_id,
        ))
    return assignments
```

Existing scaffold already supports `zone_id` and `interleave_offset`; the above is a drop-in refinement that can later call a crosstalk estimator derived from the forward model.

## Next Steps (allocation only)

- Fold viewpoint-width and subpixel crosstalk estimates into the assignment cost function.
- Prototype TPSA-style geometric remapping for slanted-lenticular targets.
- Evaluate time-multiplexed view pairing versus pure spatial interleaving under multi-viewer motion.
- Keep all new logic inside the allocation module; no changes outside this boundary.

*No new GitHub issue opened (quarantine maintained).*
