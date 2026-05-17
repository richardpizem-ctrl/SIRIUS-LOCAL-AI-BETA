"""
SIRIUS LOCAL AI – Runtime Core 4.3+
----------------------------------

This package provides the low‑level orchestration layer used by:

- RuntimeEngine 4.3
- PluginLoader 4.3+
- EventBus 4.3
- AILoop 4.3
- Security Family 4.4

Included components:
- DependencyGraph4      (module dependency resolution)
- ModuleLoader4         (module lifecycle + loading)
- SandboxManager4       (execution isolation, security hooks)
- SchedulerManager4     (task scheduling, AI loop integration)
- StateManager4         (runtime state, persistence, recovery)

Runtime Core 4.3 is Self‑Repair‑ready and safe‑mode compatible.
"""

# ---------------------------------------------------------
# SAFE IMPORTS (Runtime 4.3 Security Layer)
# ---------------------------------------------------------

from .dependency_graph import DependencyGraph4
from .module_loader import ModuleLoader4
from .sandbox_manager import SandboxManager4
from .scheduler_manager import SchedulerManager4
from .state_manager import StateManager4

# ---------------------------------------------------------
# RUNTIME CORE METADATA
# ---------------------------------------------------------

RUNTIME_CORE_VERSION: str = "4.3"
SECURITY_FAMILY_COMPAT: str = "4.4"
SAFE_MODE_SUPPORTED: bool = True

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
]
