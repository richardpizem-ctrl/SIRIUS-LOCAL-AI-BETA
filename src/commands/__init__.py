"""
SIRIUS LOCAL AI – Commands Package
----------------------------------
This package contains all command modules used by the SIRIUS runtime.

The commands are dynamically discovered and registered through:
- registry.py
- command_router.py
- loader.py

This file intentionally does not import individual commands to avoid
side‑effects during module discovery and to keep initialization clean.
"""

