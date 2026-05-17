"""
SIRIUS LOCAL AI – Workflow Engine Package 4.3.x
-----------------------------------------------
This package contains the workflow engine and workflow‑related modules
used by the SIRIUS runtime.

The workflow subsystem provides:
- workflow graph construction and validation (Phase‑4)
- pack loading and linking (Knowledge Packs 2.0)
- workflow execution pipeline
- sandboxed workflow operations (Sandbox Layer 4.3.x)
- scheduler integration (Scheduler 4.3.x)
- runtime‑level workflow orchestration (Runtime Manager 4.3.x)
- deterministic, offline‑only behavior
- safe‑mode and degraded‑mode compatibility

Security Notes:
- No dynamic imports allowed.
- No side-effects during initialization.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

WORKFLOW_ENGINE_VERSION = "4.3.x"
KNOWLEDGE_PACKS_COMPAT = "2.0"
SANDBOX_LAYER_COMPAT = "4.3.x"
SCHEDULER_COMPAT = "4.3.x"
RUNTIME_MANAGER_COMPAT = "4.3.x"
SECURITY_FAMILY_COMPAT = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "engine",
    "graph",
    "loader",
    "sandbox",
    "scheduler",
    "executor",
    "packs",
    "validator",

    # Metadata
    "WORKFLOW_ENGINE_VERSION",
    "KNOWLEDGE_PACKS_COMPAT",
    "SANDBOX_LAYER_COMPAT",
    "SCHEDULER_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
]
