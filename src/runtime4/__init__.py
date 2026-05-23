"""
SIRIUS LOCAL AI – Runtime 4.5.0 Package (PRO)

This package contains the next‑generation runtime architecture for SIRIUS 4.5.
It provides:

- Core runtime engine (scheduler, dependency graph, module loader)
- Sandbox isolation layer (Sandbox 4.5)
- Knowledge Packs 2.0 loader and validator
- ENVOY 4.0 integration layer
- Offline reasoning engines
- PC Automation Runtime 4.5
- Diagnostics and Self‑Repair 4.5 (Phase‑5)
- UI Automation Engine 4.5 (graph, parser, actions, sandbox, workflow)

All modules inside this package are fully isolated and designed for
deterministic, safe, offline execution.

Security Notes (Runtime 4.5.0):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.5.
- Self‑Repair Layer Phase‑5 ready.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA (Runtime 4.5.0)
# -------------------------------------------------------------------------

RUNTIME_VERSION: str = "4.5.0"
SECURITY_FAMILY_COMPAT: str = "4.5"
SAFE_MODE_SUPPORTED: bool = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (static, verified modules only)
# -------------------------------------------------------------------------

__all__ = [
    "core",          # Core runtime engine
    "sandbox",       # Sandbox 4.5
    "packs",         # Knowledge Packs 2.0
    "envoy",         # ENVOY 4.0 integration
    "reasoning",     # Offline reasoning engines
    "automation",    # PC Automation Runtime 4.5
    "diagnostics",   # Diagnostics + Self‑Repair 4.5
    "ui_automation", # UI Automation Engine 4.5
    "RUNTIME_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
