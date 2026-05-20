dev_automation_4_4/__init__.py
"""
SIRIUS LOCAL AI – Developer Automation 4.4.0

This package contains the Developer Automation Engine for Runtime 4.4.
It provides:

- Static offline code analysis
- Deterministic refactoring engine
- Project scaffolding generator
- Offline documentation extractor

All modules inside this package are deterministic, isolated, and offline‑safe.

Security Notes (Developer Automation 4.4.0):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

DEV_AUTOMATION_VERSION_4_4 = "4.4.0"
DEV_AUTOMATION_SECURITY_FAMILY = "4.4"
DEV_AUTOMATION_OFFLINE = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (no imports here)
# -------------------------------------------------------------------------

__all__ = [
    "dev_code_analyzer_4_4",
    "dev_refactor_engine_4_4",
    "dev_project_scaffolder_4_4",
    "dev_doc_extractor_4_4",
    "DEV_AUTOMATION_VERSION_4_4",
    "DEV_AUTOMATION_SECURITY_FAMILY",
    "DEV_AUTOMATION_OFFLINE",
]
