"""
SIRIUS LOCAL AI – UI Package 4.3.x
----------------------------------
This package contains the user interface subsystem for SIRIUS LOCAL AI.

The UI subsystem provides:
- window and panel management (Phase‑4)
- toolbar and layout rendering
- pixel‑level layout engine (PixelLayoutEngine Phase‑4)
- timeline UI components (TimelineUI 4.3.x)
- interactive controls and event handling
- integration with Runtime Manager 4.3.x
- integration with Workflow Engine 4.3.x
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

UI_PACKAGE_VERSION = "4.3.x"
PIXEL_LAYOUT_ENGINE_COMPAT = "Phase‑4"
UI_MANAGER_COMPAT = "Phase‑4"
TIMELINE_UI_COMPAT = "4.3.x"
SECURITY_FAMILY_COMPAT = "4.4"
RUNTIME_MANAGER_COMPAT = "4.3.x"
WORKFLOW_ENGINE_COMPAT = "4.3.x"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "ui_actions",
    "ui_graph",
    "ui_parser",
    "ui_sandbox",
    "ui_win_capabilities",
    "ui_workflow",
    "ui_components",
    "main_window",
    "orb_widget",
    "confirm",

    # Metadata
    "UI_PACKAGE_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "TIMELINE_UI_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "WORKFLOW_ENGINE_COMPAT",
]
