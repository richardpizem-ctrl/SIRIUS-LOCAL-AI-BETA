"""
SIRIUS LOCAL AI – UI Components Package 4.3.x
---------------------------------------------
This package contains the modular UI components used by the SIRIUS UI subsystem.

The UI components subsystem provides:
- reusable UI elements (panels, toolbars, windows)
- pixel‑level layout rendering (PixelLayoutEngine Phase‑4)
- timeline UI integration (TimelineUI 4.3.x)
- animation support via the Animations Engine 4.3.x
- event handling and interactive controls
- integration with the UI Manager and Runtime Manager 4.3.x
- deterministic, offline‑only behavior
- safe‑mode and degraded‑mode compatibility

Security Notes:
- No dynamic imports allowed.
- No side-effects during initialization.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

UI_COMPONENTS_VERSION = "4.3.x"
PIXEL_LAYOUT_ENGINE_COMPAT = "Phase‑4"
UI_MANAGER_COMPAT = "Phase‑4"
TIMELINE_UI_COMPAT = "4.3.x"
SECURITY_FAMILY_COMPAT = "4.4"
RUNTIME_MANAGER_COMPAT = "4.3.x"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "panel",
    "toolbar",
    "window",
    "pixel_layout_engine",
    "timeline_ui_component",
    "manager",

    # Metadata
    "UI_COMPONENTS_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "TIMELINE_UI_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
]
