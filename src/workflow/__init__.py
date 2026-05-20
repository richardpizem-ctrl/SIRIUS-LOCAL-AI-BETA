"""
SIRIUS LOCAL AI – Workflow Engine Package 4.4.0 PRO
---------------------------------------------------
This package contains the workflow engine and workflow‑related modules
used by the SIRIUS runtime.

The workflow subsystem provides:
- workflow graph construction and validation (Phase‑4)
- pack loading and linking (Knowledge Packs 2.0)
- workflow execution pipeline
- sandboxed workflow operations (Sandbox Layer 4.4)
- scheduler integration (Scheduler 4.4)
- runtime‑level workflow orchestration (Runtime Manager 4.4)
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

WORKFLOW_ENGINE_VERSION = "4.4.0"
KNOWLEDGE_PACKS_COMPAT = "2.0"
SANDBOX_LAYER_COMPAT = "4.4"
SCHEDULER_COMPAT = "4.4"
RUNTIME_MANAGER_COMPAT = "4.4"
SECURITY_FAMILY_COMPAT = "4.4"
SELF_REPAIR_COMPAT = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "engine_4_4",
    "graph_4_4",
    "loader_4_4",
    "sandbox_4_4",
    "scheduler_4_4",
    "executor_4_4",
    "packs_4_4",
    "validator_4_4",

    # Metadata
    "WORKFLOW_ENGINE_VERSION",
    "KNOWLEDGE_PACKS_COMPAT",
    "SANDBOX_LAYER_COMPAT",
    "SCHEDULER_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "SELF_REPAIR_COMPAT",
]
