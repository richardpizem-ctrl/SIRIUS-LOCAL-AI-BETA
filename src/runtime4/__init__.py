"""
SIRIUS LOCAL AI – Runtime 4.3.x Package (PRO)

This package contains the next‑generation runtime architecture for SIRIUS 4.3.
It provides:

- Core runtime engine (scheduler, dependency graph, module loader)
- Sandbox isolation layer (Sandbox 4.3)
- Knowledge Packs 2.0 loader and validator
- ENVOY 4.0 integration layer
- Offline reasoning engines
- PC Automation Runtime 4.3
- Diagnostics and Self‑Repair 4.4 hooks
- UI Automation Engine 4.3.x (graph, parser, actions, sandbox, workflow)

All modules inside this package are fully isolated and designed for
deterministic, safe, offline execution.

Security Notes (Runtime 4.3.x):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA (Runtime 4.3.x)
# -------------------------------------------------------------------------

RUNTIME_VERSION: str = "4.3.x"
SECURITY_FAMILY_COMPAT: str = "4.4"
SAFE_MODE_SUPPORTED: bool = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (static, verified modules only)
# -------------------------------------------------------------------------

__all__ = [
    "core",          # Core runtime engine
    "sandbox",       # Sandbox 4.3
    "packs",         # Knowledge Packs 2.0
    "envoy",         # ENVOY 4.0 integration
    "reasoning",     # Offline reasoning engines
    "automation",    # PC Automation Runtime 4.3
    "diagnostics",   # Diagnostics + Self‑Repair 4.4 hooks
    "ui_automation", # UI Automation Engine 4.3.x
    "RUNTIME_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
