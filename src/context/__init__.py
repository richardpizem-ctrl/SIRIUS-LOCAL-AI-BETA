"""
SIRIUS LOCAL AI – Context Package (v4.3)
----------------------------------------

This package contains all context‑related modules used by the SIRIUS Runtime4.

The context system provides:
- state management (ContextManager 4.3)
- profile handling
- history tracking with snapshots
- memory load/save operations
- rollback and restore capabilities
- translation utilities
- structured introspection for NL Router 4.x
- deterministic behavior for Self‑Repair 4.4

Design rules (v4.3):
- No side‑effects on import.
- No global initialization.
- All initialization is handled by:
    - context.manager.ContextManager
    - runtime.runtime_manager.RuntimeManager
- Modules must remain pure and deterministic.
- All context operations must be reversible (snapshot → rollback).
- All context mutations must be logged by Runtime4.

This package is dynamically loaded by the runtime.
"""
