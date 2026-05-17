"""
SIRIUS LOCAL AI – Timeline Package 4.3.x
----------------------------------------
This package contains the timeline UI subsystem used by SIRIUS LOCAL AI.

The timeline subsystem provides:
- real‑time playback visualization
- timeline UI rendering (Phase‑4)
- playhead, markers, snapping, grid interaction
- integration with PixelLayoutEngine (Phase‑4)
- integration with UI Manager (Phase‑4)
- deterministic, offline-only behavior
- safe-mode and degraded-mode compatible

Security Notes:
- No dynamic imports allowed.
- No side-effects during initialization.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

TIMELINE_VERSION = "4.3.x"
PIXEL_LAYOUT_ENGINE_COMPAT = "Phase‑4"
UI_MANAGER_COMPAT = "Phase‑4"
SECURITY_FAMILY_COMPAT = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "timeline_ui",
    "timeline_ui_component",
    "TIMELINE_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
]
