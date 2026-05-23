"""
SIRIUS LOCAL AI – Runtime Core 4.5
----------------------------------

This package provides the low‑level orchestration layer used by:

- RuntimeEngine 4.5
- PluginLoader 4.5
- EventBus 4.5
- AILoop 4.5
- Security Family 4.5
- Workflow Engine 4.5

Included components:
- DependencyGraph4      (module dependency resolution)
- ModuleLoader4         (module lifecycle + loading)
- SandboxManager4       (execution isolation, security hooks)
- SchedulerManager4     (task scheduling, AI loop integration)
- StateManager4         (runtime state, persistence, recovery)

Runtime Core 4.5 is:
- deterministic
- audit‑ready
- safe‑mode compatible
- Self‑Repair Layer 4.5 compliant
- free of side‑effects during import
"""

# ---------------------------------------------------------
# SAFE IMPORTS (Runtime 4.5 Security Layer)
# ---------------------------------------------------------

from .dependency_graph import DependencyGraph4
from .module_loader import ModuleLoader4
from .sandbox_manager import SandboxManager4
from .scheduler_manager import SchedulerManager4
from .state_manager import StateManager4

# ---------------------------------------------------------
# RUNTIME CORE METADATA
# ---------------------------------------------------------

RUNTIME_CORE_VERSION: str = "4.5"
SECURITY_FAMILY_COMPAT: str = "4.5"
SAFE_MODE_SUPPORTED: bool = True
DETERMINISTIC: bool = True
SELF_REPAIR_READY: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "DependencyGraph4",
    "ModuleLoader4",
    "SandboxManager4",
    "SchedulerManager4",
    "StateManager4",
    "RUNTIME_CORE_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
    "DETERMINISTIC",
    "SELF_REPAIR_READY",
]
