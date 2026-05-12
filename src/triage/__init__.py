"""
SIRIUS LOCAL AI – Triage Engine Package
---------------------------------------
This package contains the Automatic Input Triage Engine (AITE), the
intelligent routing and decision-making layer of the SIRIUS system.

The triage subsystem provides:
- natural language input classification
- command vs. file vs. workflow detection
- schoolwork priority mode activation
- identity-aware behavior (OWNER / FAMILY / STRANGER)
- safety and restricted-mode routing
- integration with runtime manager and workflow engine

Modules inside this package are dynamically loaded by the runtime.
No imports are performed here to avoid side-effects during initialization.
"""

