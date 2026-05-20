"""
SIRIUS LOCAL AI – Timeline Package 4.4.0 (PRO)
----------------------------------------------
Phase‑4 timeline subsystem for SIRIUS LOCAL AI.

Provides:
- real‑time playback visualization
- Phase‑4 timeline UI rendering
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

TIMELINE_VERSION: str = "4.4.0"
PIXEL_LAYOUT_ENGINE_COMPAT: str = "Phase‑4"
UI_MANAGER_COMPAT: str = "Phase‑4"
SECURITY_FAMILY_COMPAT: str = "4.4"
SELF_REPAIR_COMPAT: str = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "timeline_ui_4_4",
    "timeline_ui_component_4_4",
    "TIMELINE_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "SELF_REPAIR_COMPAT",
]
