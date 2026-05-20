"""
SIRIUS LOCAL AI – UI Components Package 4.4.0 PRO
-------------------------------------------------
This package contains the modular UI components used by the SIRIUS UI subsystem.

The UI components subsystem provides:
- reusable UI elements (panels, toolbars, windows)
- pixel‑level layout rendering (PixelLayoutEngine Phase‑4)
- timeline UI integration (TimelineUI 4.4)
- animation support via the Animations Engine 4.4
- event handling and interactive controls
- integration with the UI Manager and Runtime Manager 4.4
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

UI_COMPONENTS_VERSION = "4.4.0"
PIXEL_LAYOUT_ENGINE_COMPAT = "Phase‑4"
UI_MANAGER_COMPAT = "4.4.0"
TIMELINE_UI_COMPAT = "4.4.0"
SECURITY_FAMILY_COMPAT = "4.4"
RUNTIME_MANAGER_COMPAT = "4.4.0"
SELF_REPAIR_COMPAT = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "panel_4_4",
    "toolbar_4_4",
    "window_4_4",
    "pixel_layout_engine_4_4",
    "timeline_ui_component_4_4",
    "manager_4_4",

    # Metadata
    "UI_COMPONENTS_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "TIMELINE_UI_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "SELF_REPAIR_COMPAT",
]
