"""
SIRIUS LOCAL AI – Filesystem Package 4.3
----------------------------------------
This package contains all filesystem‑related modules used by the
SIRIUS Runtime 4.x.

The filesystem subsystem provides:
- safe file operations
- directory scanning and indexing
- file metadata extraction
- agent‑level filesystem actions
- integration with modules and the workflow engine
- deterministic behavior for Runtime4
- Self‑Repair 4.4 compatibility

Notes:
- Modules inside this package are dynamically loaded by the runtime.
- No imports are performed here to avoid side‑effects during initialization.
- This package is part of the SIRIUS LOCAL AI modular architecture.
"""

__all__ = [
    "fs_agent",
    "fs_scanner",
    "fs_metadata",
    "fs_actions",
    "fs_safe_ops",
]
