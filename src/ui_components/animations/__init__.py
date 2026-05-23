"""
SIRIUS LOCAL AI – UI Animations Package 4.5.0 (PRO)
---------------------------------------------------
This package contains the animation engine and animation components used
by the SIRIUS UI subsystem.

The animations subsystem provides:
- scene management and transitions (Phase‑4)
- animated UI objects and effects
- timeline‑driven animation playback
- integration with PixelLayoutEngine (Phase‑4)
- integration with UI Manager (Phase‑4)
- reusable animation primitives for UI components
- deterministic, offline‑only behavior
- safe‑mode and degraded‑mode compatibility

Security Notes:
- No dynamic imports allowed.
- No side-effects during initialization.
- Fully compatible with Security Family 4.5.
- Self‑Repair 4.5 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

ANIMATIONS_VERSION = "4.5.0"
PIXEL_LAYOUT_ENGINE_COMPAT = "Phase‑4"
UI_MANAGER_COMPAT = "Phase‑4"
SECURITY_FAMILY_COMPAT = "4.5"
SELF_REPAIR_COMPAT = "4.5"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "engine_4_5",
    "manager_4_5",
    "objects_4_5",
    "orb_factory_4_5",
    "orb_renderer_4_5",
    "scenes_4_5",

    # Metadata
    "ANIMATIONS_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "SELF_REPAIR_COMPAT",
]
