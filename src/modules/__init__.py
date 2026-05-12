"""
SIRIUS LOCAL AI – Modules Package
---------------------------------
This package contains all functional modules used by the SIRIUS runtime.

Modules in this package provide:
- command parsing and routing
- editor and filesystem operations
- workflow automation
- module-level capabilities for the runtime engine

All modules are dynamically discovered by runtime.loader and should not
perform side-effects on import. Initialization is handled by module_base
and runtime_manager.
"""
