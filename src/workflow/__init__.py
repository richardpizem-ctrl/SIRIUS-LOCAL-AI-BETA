"""
SIRIUS LOCAL AI – Workflow Engine Package 4.5.0 PRO
---------------------------------------------------
This package contains the workflow engine and workflow‑related modules
used by the SIRIUS runtime.

The workflow subsystem provides:
- workflow graph construction and validation (Phase‑4)
- pack loading and linking (Knowledge Packs 2.0)
- workflow execution pipeline
- sandboxed workflow operations (Sandbox Layer 4.5)
- scheduler integration (Scheduler 4.5)
- runtime‑level workflow orchestration (Runtime Manager 4.5)
- deterministic, offline‑only behavior
- safe‑mode and degraded‑mode compatibility

Security Notes:
- No dynamic imports allowed.
- No side-effects during initialization.
- Fully compatible with Security Family 4.5.
- Self‑Repair 4.5 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

WORKFLOW_ENGINE_VERSION = "4.5.0"
KNOWLEDGE_PACKS_COMPAT = "2.0"
SANDBOX_LAYER_COMPAT = "4.5"
SCHEDULER_COMPAT = "4.5"
RUNTIME_MANAGER_COMPAT = "4.5"
SECURITY_FAMILY_COMPAT = "4.5"
SELF_REPAIR_COMPAT = "4.5"

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    "engine_4_5",
    "graph_4_5",
    "loader_4_5",
    "sandbox_4_5",
    "scheduler_4_5",
    "executor_4_5",
    "packs_4_5",
    "validator_4_5",

    # Metadata
    "WORKFLOW_ENGINE_VERSION",
    "KNOWLEDGE_PACKS_COMPAT",
    "SANDBOX_LAYER_COMPAT",
    "SCHEDULER_COMPAT",
    "RUNTIME_MANAGER_COMPAT",
    "SECURITY_FAMILY_COMPAT",
    "SELF_REPAIR_COMPAT",
]
