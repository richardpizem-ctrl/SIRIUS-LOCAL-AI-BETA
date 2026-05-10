"""
SIRIUS LOCAL AI – Runtime 4.0 Package

This package contains the next‑generation runtime architecture for SIRIUS 4.0.
It provides:
- Core runtime engine (scheduler, dependency graph, module loader)
- Sandbox isolation layer
- Knowledge Packs 2.0 loader and validator
- ENVOY 4.0 integration layer
- Offline reasoning engines
- PC Automation Runtime 4.0
- Diagnostics and self‑repair hooks

All modules inside this package are fully isolated and designed for deterministic,
safe, offline execution.

Security Notes (Runtime 4.0):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
"""

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
]
