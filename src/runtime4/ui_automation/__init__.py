"""
UI Automation Engine for SIRIUS Runtime 4.2.0

This package provides the complete UI Automation subsystem for SIRIUS Runtime.
It includes:

- UI Graph (window tree abstraction)
- UI Parser (element extraction and normalization)
- UI Actions (safe UI operations and semantic actions)
- UI Sandbox (identity‑aware permission layer)
- UI Workflow (deterministic UI sequences)

The UI Automation Engine is part of runtime4, but does not modify or interfere
with the core runtime engine. All components operate in a fully isolated,
deterministic, offline‑safe environment.

Security Notes (Runtime 4.2.0):
- No direct OS calls are performed in this layer.
- All UI operations must pass through UI Sandbox.
- Semantic actions must remain deterministic and identity‑aware.
- No dynamic imports, no reflection, no eval.
- Only static, verified modules may be exported.
"""

__all__ = [
    "ui_graph",
    "ui_parser",
    "ui_actions",
    "ui_sandbox",
    "ui_workflow",
]
