"""
SIRIUS LOCAL AI – UI Automation Engine 4.4.0

This package contains the next‑generation UI Automation Engine for Runtime 4.4.
It extends the 4.3.x UI Automation stack with:

- OS‑level UI bridge (Win32 / UIA / WinRT abstraction)
- Semantic element resolution (fuzzy + structural matching)
- Deterministic UI action routing
- Hardened UI sandbox for OS‑level operations
- Multi‑step UI workflows with safety constraints

All logic is deterministic, offline, and fully isolated.

Security Notes (UI Automation 4.4.0):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- STRANGER‑mode and behavior‑based safety ready.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

UI_AUTOMATION_VERSION_4_4 = "4.4.0"
UI_AUTOMATION_SECURITY_FAMILY = "4.4"
UI_AUTOMATION_OS_LEVEL = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (no imports here)
# -------------------------------------------------------------------------

__all__ = [
    "ui_os_bridge_4_4",
    "ui_element_resolver_4_4",
    "ui_action_router_4_4",
    "ui_sandbox_4_4",
    "ui_workflow_4_4",
    "UI_AUTOMATION_VERSION_4_4",
    "UI_AUTOMATION_SECURITY_FAMILY",
    "UI_AUTOMATION_OS_LEVEL",
]
