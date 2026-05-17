"""
SIRIUS LOCAL AI – Commands Package (Runtime4)
--------------------------------------------
This package contains all command modules used by the SIRIUS Runtime 4.x.

Commands are dynamically discovered and registered through:

- registry.py        → central command registry (classes, not instances)
- command_router.py  → NL routing and command resolution
- loader.py          → safe dynamic loading and registration

Design notes:
- This package does NOT import individual commands directly.
- This avoids side effects during module discovery.
- Initialization remains clean, deterministic, and sandbox‑safe.
"""
