"""
SIRIUS LOCAL AI – UI Components Package 4.5.0 PRO
-------------------------------------------------
This package contains the modular UI components used by the SIRIUS UI subsystem.

The UI components subsystem provides:
- reusable UI elements (panels, toolbars, windows)
- pixel‑level layout rendering (PixelLayoutEngine Phase‑4)
- timeline UI integration (TimelineUI 4.5)
- animation support via the Animations Engine 4.5
- event handling and interactive controls
- integration with the UI Manager and Runtime Manager 4.5
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

UI_COMPONENTS_VERSION = "4.5.0"
PIXEL_LAYOUT_ENGINE_COMPAT = "Phase‑4"
UI_MANAGER_COMPAT = "4.5.0"
TIMELINE_UI_COMPAT = "4.5.0"
SECURITY_FAMILY_COMPAT = "4.5"
RUNTIME_MANAGER_COMPAT = "4.5.0"
SELF_REPAIR_COMPAT = "4.5"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "panel_4_5",
    "toolbar_4_5",
    "window_4_5",
    "pixel_layout_engine_4_5",
    "timeline_ui_component_4_5",
    "manager_4_5",

    # Metadata
    "UI_COMPONENTS_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "TIMELINE_UI_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "SELF_REPAIR_COMPAT",
]
