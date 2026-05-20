"""
SIRIUS LOCAL AI – UI Package 4.4.0 (PRO)
----------------------------------------
This package contains the user interface subsystem for SIRIUS LOCAL AI.

The UI subsystem provides:
- window and panel management (Phase‑4)
- toolbar and layout rendering
- pixel‑level layout engine (PixelLayoutEngine Phase‑4)
- timeline UI components (TimelineUI 4.4.0 PRO)
- interactive controls and event handling
- integration with Runtime Manager 4.4
- integration with Workflow Engine 4.4
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

UI_PACKAGE_VERSION: str = "4.4.0"
PIXEL_LAYOUT_ENGINE_COMPAT: str = "Phase‑4"
UI_MANAGER_COMPAT: str = "4.4.0"
TIMELINE_UI_COMPAT: str = "4.4.0"
SECURITY_FAMILY_COMPAT: str = "4.4"
RUNTIME_MANAGER_COMPAT: str = "4.4.0"
WORKFLOW_ENGINE_COMPAT: str = "4.4.0"
SELF_REPAIR_COMPAT: str = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "ui_manager_4_4",
    "ui_action_router_4_4",
    "ui_element_resolver_4_4",
    "ui_os_bridge_4_4",
    "ui_sandbox_4_4",
    "ui_workflow_4_4",
    "ui_automation_4_4",
    "UI_PACKAGE_VERSION",
    "PIXEL_LAYOUT_ENGINE_COMPAT",
    "UI_MANAGER_COMPAT",
    "TIMELINE_UI_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "WORKFLOW_ENGINE_COMPAT",
    "SELF_REPAIR_COMPAT",
]
