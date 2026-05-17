"""
SIRIUS LOCAL AI – Runtime 4.3.x Package

This package contains the next‑generation runtime architecture for SIRIUS 4.3.
It provides:
- Core runtime engine (scheduler, dependency graph, module loader)
- Sandbox isolation layer (Sandbox 4.3)
- Knowledge Packs 2.0 loader and validator
- ENVOY 4.0 integration layer
- Offline reasoning engines
- PC Automation Runtime 4.3
- Diagnostics and self‑repair hooks
- UI Automation Engine 4.3.x (graph, parser, actions, sandbox, workflow)

All modules inside this package are fully isolated and designed for deterministic,
safe, offline execution.

Security Notes (Runtime 4.3.x):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

RUNTIME_VERSION = "4.3.x"
SECURITY_FAMILY_COMPAT = "4.4"
SAFE_MODE_SUPPORTED = True

# ---------------------------------------------------------
# SAFE EXPORT LIST (no imports here)
# ---------------------------------------------------------

__all__ = [
    "core",
    "sandbox",
    "packs",
    "envoy",
    "reasoning",
    "automation",
    "diagnostics",
    "ui_automation",   # UI Automation Engine 4.3.x
    "RUNTIME_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
