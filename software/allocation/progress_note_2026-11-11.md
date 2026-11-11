# Allocation Research Note — 2026-11-11

**Focus**: View allocation, light-field optimization, interleaving, and multi-viewer light distribution for autostereoscopic / light-field displays. Receives 3D eye positions from tracking.

## Research Summary

### 1. Subpixel-demultiplexing viewpoint-interleaving encoding (SVE) + full-field dual-plane lens optimization (PhotoniX, 2026)
- **Key takeaway**: SVE pre-encodes light-field images with dual assignment strategies (including odd–even vertical viewpoint interleaving) to produce an aliasing-free high-density subpixel array on the multiplexed panel. Combined with optical FDLO, a 5.5-inch prototype achieves ~2.7–3.0 lp/mm spatial resolution and 1.45 VIPD angular resolution with smooth parallax and improved visual comfort across the FOV.
- **Relevance**: Direct technique for interleaving multiple viewpoints so each tracked viewer receives a clean stereo pair. Vertical interleaving reduces discontinuities; useful as a software mapping layer before optical delivery.
- **Reference**: PhotoniX 7, 73 (2026). DOI: 10.1186/s43074-026-00292-w

### 2. Freeform directional backlight multi-viewer autostereoscopic display (Displays, 2026)
- **Key takeaway**: True continuous freeform backlight + eye-tracking delivers full native panel resolution to multiple simultaneous viewers with ~44° FOV on a 27-inch prototype, average crosstalk <7.1% (single) / <8.8% (three-viewer). Decouples illumination from image content for independent binocular modulation.
- **Relevance**: Hardware-assisted allocation of light cones to tracked eye pairs. Software side mainly needs to generate correct left/right images per viewer and synchronize with tracking.
- **Reference**: Displays 95, 103581 (2026). DOI: 10.1016/j.displa.2026.103581

### 3. Adaptive viewing-zone fusion for high-density light-field displays (Chinese Optics Letters, 2026)
- **Key takeaway**: Distortion-suppressed composite light-control device + observation-position-driven fusion algorithm with active buffering expands effective viewing angle from 14° to 84° while supporting 168 viewpoints at 2880	imes1620 per view. Improves zone uniformity and eliminates jumps/reversals.
- **Relevance**: Dynamic zone assignment and fusion based on viewer position—core allocation logic for multi-viewer scenarios. Active buffering handles tracking noise and motion.
- **Reference**: Chinese Optics Letters 24, 053301 (2026). DOI: 10.3788/COL202624.053301

### 4. EyeReal dynamic space-bandwidth-product optimization (Nature, 2025)
- **Key takeaway**: Real-time deep-learning generation of optimal light fields strictly around currently tracked binocular positions, enabling >100° seamless full-parallax viewing on desktop-scale stacked LCDs at >50 Hz / 1080p. Exploits limited optical capacity by concentrating resources where eyes actually are.
- **Relevance**: Computational allocation strategy. Multi-viewer extension possible via time-multiplexing or directional backlighting; provides a model for prioritizing light-field energy to multiple tracked eye pairs.
- **Reference**: Ma et al., Nature 648, 76–83 (2025). Code: https://github.com/WeijieMax/EyeReal

## Code Scaffold

See `view_allocation_scaffold.py` in this directory for a minimal Python scaffold. It takes a list of tracked viewer 3D eye positions, assigns discrete views or stereo pairs (with simple interleaving offset), and produces a mapping suitable for subpixel or zone-based interleaving. Placeholder for later optimization of crosstalk or zone fusion.

## Next Steps

Integrate with tracking output; implement zone-fusion or SVE-style interleaving; evaluate multi-viewer crosstalk under motion; explore computational SBP allocation for more than two viewers.
