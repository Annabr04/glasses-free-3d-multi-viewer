"""
View allocation scaffold for multi-viewer glasses-free 3D / light-field displays.

Receives tracked 3D eye positions (from the tracking component) and produces
a simple view-to-subpixel or zone assignment with basic interleaving.
Intended as a clean starting point for SVE-style interleaving, zone fusion,
or dynamic SBP allocation.

Dependencies:
    pip install numpy

Stays strictly inside the Allocation Warden boundary.
"""

import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class ViewerEyes:
    viewer_id: int
    left_eye_3d: np.ndarray   # (X, Y, Z) meters
    right_eye_3d: np.ndarray
    confidence: float = 1.0

@dataclass
class ViewAssignment:
    viewer_id: int
    left_view_index: int
    right_view_index: int
    interleave_offset: int    # subpixel or row offset for interleaving
    zone_id: Optional[int] = None

class SimpleViewAllocator:
    def __init__(self, num_views: int = 9, display_width_px: int = 1920, interleave_period: int = 2):
        """
        num_views: total discrete viewpoints available in the light field
        interleave_period: e.g. 2 for odd/even vertical interleaving
        """
        self.num_views = num_views
        self.display_width_px = display_width_px
        self.interleave_period = interleave_period
        # Simple angular mapping: views span roughly -20° to +20° (placeholder)
        self.view_angles = np.linspace(-20, 20, num_views)

    def allocate(self, viewers: List[ViewerEyes]) -> List[ViewAssignment]:
        """
        Assign stereo view indices and interleaving offsets based on horizontal
        angular position of each eye pair. Very simplified; replace with proper
        light-field ray mapping or zone-fusion later.
        """
        assignments = []
        for v in viewers:
            # Approximate viewing angle from midpoint of eyes (horizontal)
            mid = (v.left_eye_3d + v.right_eye_3d) / 2.0
            # Placeholder: assume display at Z=0, viewer at positive Z
            angle_deg = np.degrees(np.arctan2(mid[0], mid[2])) if mid[2] != 0 else 0.0

            # Find nearest view index for left and right eyes (simple stereo separation)
            left_angle = angle_deg - 1.5   # ~IPD angular offset placeholder
            right_angle = angle_deg + 1.5

            left_idx = int(np.argmin(np.abs(self.view_angles - left_angle)))
            right_idx = int(np.argmin(np.abs(self.view_angles - right_angle)))

            # Basic interleaving: alternate offset by viewer id or vertical parity
            offset = (v.viewer_id % self.interleave_period)

            assignments.append(ViewAssignment(
                viewer_id=v.viewer_id,
                left_view_index=left_idx,
                right_view_index=right_idx,
                interleave_offset=offset,
                zone_id=v.viewer_id,  # placeholder zone
            ))
        return assignments

    def build_interleaved_map(self, assignments: List[ViewAssignment], height: int = 1080) -> Dict:
        """
        Placeholder: return a simple mapping description for later rendering.
        In a real system this would generate the subpixel assignment matrix.
        """
        return {
            "assignments": assignments,
            "note": "Use interleave_offset for vertical odd/even or subpixel demultiplexing (SVE-style).",
            "num_views": self.num_views,
        }


# Example usage
if __name__ == "__main__":
    allocator = SimpleViewAllocator(num_views=9)
    # Fake tracked viewers (meters)
    viewers = [
        ViewerEyes(0, np.array([-0.05, 0.0, 0.6]), np.array([0.02, 0.0, 0.6])),
        ViewerEyes(1, np.array([0.15, 0.0, 0.7]), np.array([0.22, 0.0, 0.7])),
    ]
    result = allocator.allocate(viewers)
    for a in result:
        print(f"Viewer {a.viewer_id}: L={a.left_view_index}, R={a.right_view_index}, offset={a.interleave_offset}")
    print(allocator.build_interleaved_map(result))
