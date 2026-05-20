"""
SIRIUS LOCAL AI – UI Automation Engine 4.3 (PRO)

This package provides the complete UI Automation subsystem for SIRIUS Runtime.
It includes:

- UI Graph (window tree abstraction)
- UI Parser (element extraction and normalization)
- UI Actions (safe UI operations and semantic actions)
- UI Sandbox (identity‑aware permission layer)
- UI Workflow (deterministic UI sequences)

The UI Automation Engine is part of Runtime 4.3, but does not modify or
interfere with the core runtime engine. All components operate in a fully
isolated, deterministic, offline‑safe environment.

Security Notes (Runtime 4.3 / Security Family 4.4):
- No direct OS calls are performed in this layer.
- All UI operations must pass through UI Sandbox.
- Semantic actions must remain deterministic and identity‑aware.
- No dynamic imports, no reflection, no eval.
- Only static, verified modules may be exported.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS (DETERMINISTIC)
# ---------------------------------------------------------

from . import ui_graph
from . import ui_parser
from . import ui_actions
from . import ui_sandbox
from . import ui_workflow

# ---------------------------------------------------------
# PACKAGE METADATA (READ‑ONLY)
# ---------------------------------------------------------

UI_AUTOMATION_VERSION: str = "4.3"
SECURITY_FAMILY_COMPAT: str = "4.4"
SAFE_MODE_SUPPORTED: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST (NAMESPACES ONLY)
# ---------------------------------------------------------

__all__ = [
    "ui_graph",
    "ui_parser",
    "ui_actions",
    "ui_sandbox",
    "ui_workflow",
    "UI_AUTOMATION_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
