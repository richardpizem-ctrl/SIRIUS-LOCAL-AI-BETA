"""
SIRIUS LOCAL AI – Triage Engine Package 4.3.x
---------------------------------------------
Automatic Input Triage Engine (AITE) – the intelligent routing,
classification and decision-making subsystem of SIRIUS LOCAL AI.

The triage subsystem provides:
- natural language input classification (NL Router v4)
- command vs. file vs. workflow detection
- schoolwork priority mode activation (Security Family 4.3.x)
- identity‑aware behavior (OWNER / FAMILY / CHILD / STRANGER)
- restricted‑mode and safe‑mode routing
- integration with Runtime Manager 4.3.x
- integration with Workflow Engine 4.3.x
- deterministic, offline‑only behavior

Security Notes:
- No dynamic imports allowed.
- No side‑effects during initialization.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

TRIAGE_ENGINE_VERSION = "4.3.x"
NL_ROUTER_COMPAT = "v4"
SECURITY_FAMILY_COMPAT = "4.4"
WORKFLOW_ENGINE_COMPAT = "4.3.x"
RUNTIME_MANAGER_COMPAT = "4.3.x"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "aite_core",
    "aite_router",
    "aite_rules",
    "aite_context",
    "aite_schoolwork",
    "aite_security_bridge",
    "aite_file_detector",
    "aite_command_detector",
    "aite_workflow_detector",
    "aite_nl_classifier",

    # Metadata
    "TRIAGE_ENGINE_VERSION",
    "NL_ROUTER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "WORKFLOW_ENGINE_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
]
