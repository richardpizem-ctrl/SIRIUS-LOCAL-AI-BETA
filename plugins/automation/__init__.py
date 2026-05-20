"""
SIRIUS LOCAL AI – Automation Plugin (v4.4.0)
--------------------------------------------

This package provides the Automation Plugin for SIRIUS Runtime 4.4.0.

Capabilities (4.4):
    - Sandboxed shell command execution
    - Sandboxed script execution
    - Autonomous automation tasks
    - Workflow-triggered automation
    - Natural language command bindings
    - AI task bindings
    - GUI elements for automation control
    - Safe‑Mode / Degraded‑Mode support
    - Deterministic offline-only behavior
    - Plugin Integrity Hooks (4.4)
    - Health Metadata (4.4)
    - Self‑Repair Layer 4.4 compatibility

Architecture Notes:
    - Dynamically loaded through PluginLoader 4.4.0.
    - No imports at package level (side‑effect free).
    - Implementation resides in plugin.py.
    - manifest.json defines plugin metadata, health, and integrity rules.
    - This __init__.py file must remain strictly passive.

Compatibility:
    - RuntimeManager 4.4.0
    - PluginLoader 4.4.0
    - NL Router 4.4.0
    - SystemAgent 4.4.0
    - Workflow Engine 4.4.0
    - AI Loop 4.4.0
    - Self‑Repair Layer 4.4

This file intentionally contains no executable code.
"""
