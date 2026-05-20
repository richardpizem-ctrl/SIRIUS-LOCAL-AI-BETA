"""
SIRIUS LOCAL AI – Context Package (v4.4.0)
------------------------------------------

This package contains all context‑related modules used by the SIRIUS Runtime4.

Context System 4.4 provides:
    - State management (ContextManager 4.4)
    - Profile handling
    - History tracking with snapshots
    - Memory load/save operations
    - Rollback and restore capabilities
    - Translation utilities
    - Structured introspection for NL Router 4.4
    - Deterministic behavior for Self‑Repair Layer 4.4
    - Integrity metadata for Runtime4
    - Health reporting for System Health Engine 4.4

Design rules (4.4):
    - No side‑effects on import.
    - No global initialization.
    - All initialization is handled by:
        - context.manager.ContextManager
        - runtime.runtime_manager.RuntimeManager
    - Modules must remain pure and deterministic.
    - All context operations must be reversible (snapshot → rollback).
    - All context mutations must be logged by Runtime4.
    - All modules must support Self‑Repair Layer 4.4 integrity checks.
    - All modules must expose stable introspection metadata.

This package is dynamically loaded by the runtime.
"""
