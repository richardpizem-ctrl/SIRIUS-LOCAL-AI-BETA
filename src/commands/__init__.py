"""
SIRIUS LOCAL AI – Commands Package (Runtime 4.5.0)
--------------------------------------------------

This package contains all command modules used by the SIRIUS Runtime 4.5.x.

Command System 4.5 provides:
    - Deterministic command discovery
    - Safe dynamic loading (Loader 4.5)
    - NL routing and resolution (CommandRouter 4.5)
    - Central registry for command classes (Registry 4.5)
    - Self‑Repair Layer 4.5 integration
    - Integrity metadata for command modules
    - Sandbox‑safe initialization
    - Baseline‑compatible command behavior (4.5)

Architecture Notes (4.5):
    - This package does NOT import individual commands directly.
    - Commands are discovered dynamically by loader.py.
    - registry.py registers command CLASSES, not instances.
    - command_router.py resolves NL → command mapping.
    - All modules must remain side‑effect free at import time.
    - This __init__.py file must remain strictly passive.

Compatibility:
    - RuntimeManager 4.5.x
    - CommandRouter 4.5.x
    - CommandLoader 4.5.x
    - SystemAgent 4.5.x
    - Workflow Engine 4.5.x
    - Self‑Repair Layer 4.5

This file intentionally contains no executable code.
"""
