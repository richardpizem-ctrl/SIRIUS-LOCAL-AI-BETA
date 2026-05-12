"""
SIRIUS LOCAL AI – Context Package
---------------------------------
This package contains all context‑related modules used by the SIRIUS runtime.

The context system provides:
- state management
- profile handling
- history tracking
- memory load/save operations
- rollback and restore capabilities

Modules inside this package are dynamically loaded by the runtime and
should not perform side‑effects on import. Initialization is handled by
context.manager and runtime_manager.
"""

