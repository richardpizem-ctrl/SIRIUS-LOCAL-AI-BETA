"""
SIRIUS LOCAL AI – Developer Automation 4.5.0

This package contains the Developer Automation Engine for Runtime 4.5.
It provides:

- Static offline code analysis
- Deterministic refactoring engine
- Project scaffolding generator
- Offline documentation extractor

All modules inside this package are deterministic, isolated, and offline‑safe.

Security Notes (Developer Automation 4.5.0):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.5.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

DEV_AUTOMATION_VERSION_4_5 = "4.5.0"
DEV_AUTOMATION_SECURITY_FAMILY = "4.5"
DEV_AUTOMATION_OFFLINE = True
DEV_AUTOMATION_DETERMINISTIC = True
DEV_AUTOMATION_SELF_REPAIR_READY = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (no imports here)
# -------------------------------------------------------------------------

__all__ = [
    "dev_code_analyzer_4_5",
    "dev_refactor_engine_4_5",
    "dev_project_scaffolder_4_5",
    "dev_doc_extractor_4_5",
    "DEV_AUTOMATION_VERSION_4_5",
    "DEV_AUTOMATION_SECURITY_FAMILY",
    "DEV_AUTOMATION_OFFLINE",
    "DEV_AUTOMATION_DETERMINISTIC",
    "DEV_AUTOMATION_SELF_REPAIR_READY",
]
