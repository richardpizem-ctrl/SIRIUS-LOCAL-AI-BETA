"""
SIRIUS LOCAL AI – Runtime Package 4.5
-------------------------------------
This package contains the core runtime components of the
SIRIUS system.

The runtime subsystem provides:
- command execution pipeline
- module loading and lifecycle management
- event bus and workflow engine
- natural language routing
- runtime manager and agent orchestration
- deterministic behavior for Runtime4.5
- Self‑Repair Layer 4.5 compatibility
- stable metadata contract for NL Router 4.5

Notes:
- Modules inside this package are dynamically loaded by the system.
- No imports are performed here to avoid side-effects during initialization.
- Initialization is handled by runtime_manager and module_base.
- All modules must follow the Runtime4.5 deterministic execution model.
"""

__all__ = [
    "ai_loop",
    "cli",
    "engine",
    "event_bus",
    "loader",
    "module_base",
    "nl_router",
    "runtime_manager",
    "sirius_agent",
    "workflow_engine",
    "win_capabilities",
]
