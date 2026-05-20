"""
SIRIUS LOCAL AI – Commands Package (Runtime 4.4.0)
--------------------------------------------------

This package contains all command modules used by the SIRIUS Runtime 4.4.x.

Command System 4.4 provides:
    - Deterministic command discovery
    - Safe dynamic loading (Loader 4.4)
    - NL routing and resolution (CommandRouter 4.4)
    - Central registry for command classes (Registry 4.4)
    - Self‑Repair Layer 4.4 integration
    - Integrity metadata for command modules
    - Sandbox‑safe initialization

Architecture Notes (4.4):
    - This package does NOT import individual commands directly.
    - Commands are discovered dynamically by loader.py.
    - registry.py registers command CLASSES, not instances.
    - command_router.py resolves NL → command mapping.
    - All modules must remain side‑effect free at import time.
    - This __init__.py file must remain strictly passive.

Compatibility:
    - RuntimeManager 4.4.x
    - CommandRouter 4.4.x
    - CommandLoader 4.4.x
    - SystemAgent 4.4.x
    - Workflow Engine 4.4.x
    - Self‑Repair Layer 4.4

This file intentionally contains no executable code.
"""
