"""
SIRIUS LOCAL AI – Modules Package 4.4
-------------------------------------
This package contains all functional modules used by the
SIRIUS Runtime 4.x.

Modules in this package provide:
- command parsing and routing
- editor and filesystem operations
- workflow automation
- module-level capabilities for the runtime engine
- deterministic behavior for Runtime4
- Self‑Repair Layer 4.4 compatibility
- stable metadata contract for NL Router 4.4

Notes:
- All modules are dynamically discovered by runtime.loader.
- No imports are performed here to avoid side-effects on import.
- Initialization is handled by module_base and runtime_manager.
- All modules must follow the Runtime4.4 deterministic execution model.
"""

__all__ = [
    "command_parser",
    "command_router",
    "editor_module",
    "fs_module",
    "workflow_module",
]
