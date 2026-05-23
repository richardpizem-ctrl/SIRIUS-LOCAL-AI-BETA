"""
SIRIUS LOCAL AI – Triage Engine Package 4.5.0 (PRO)
---------------------------------------------------
Automatic Input Triage Engine (AITE) – Phase‑4 intelligent routing,
classification and decision-making subsystem of SIRIUS LOCAL AI.

Provides:
- natural language input classification (NL Router v4)
- command vs. file vs. workflow detection
- schoolwork priority mode activation (Security Family 4.5)
- identity‑aware behavior (OWNER / FAMILY / CHILD / STRANGER)
- restricted‑mode and safe‑mode routing
- integration with Runtime Manager 4.5
- integration with Workflow Engine 4.5
- deterministic, offline‑only behavior
- safe-mode & degraded-mode compatible

Security Notes:
- No dynamic imports allowed.
- No side-effects during initialization.
- Fully compatible with Security Family 4.5.
- Self‑Repair 4.5 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

TRIAGE_ENGINE_VERSION: str = "4.5.0"
NL_ROUTER_COMPAT: str = "v4"
SECURITY_FAMILY_COMPAT: str = "4.5"
WORKFLOW_ENGINE_COMPAT: str = "4.5.0"
RUNTIME_MANAGER_COMPAT: str = "4.5.0"
SELF_REPAIR_COMPAT: str = "4.5"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "aite_core_4_5",
    "aite_router_4_5",
    "aite_rules_4_5",
    "aite_context_4_5",
    "aite_schoolwork_4_5",
    "aite_security_bridge_4_5",
    "aite_file_detector_4_5",
    "aite_command_detector_4_5",
    "aite_workflow_detector_4_5",
    "aite_nl_classifier_4_5",

    # Metadata
    "TRIAGE_ENGINE_VERSION",
    "NL_ROUTER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "WORKFLOW_ENGINE_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "SELF_REPAIR_COMPAT",
]
