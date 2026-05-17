"""
SIRIUS LOCAL AI – Clipboard Plugin (v4.3.x)
-------------------------------------------

This package provides the Clipboard Plugin for SIRIUS Runtime 4.3.x.

Capabilities:
    - Read clipboard text
    - Write text to clipboard
    - Natural language clipboard commands
    - AI task bindings
    - Workflow integration
    - GUI elements for quick clipboard actions
    - Safe-mode + degraded-mode support
    - Deterministic, offline-only behavior
    - Self‑Repair 4.4 ready

Architecture Notes:
    - The plugin is dynamically loaded through PluginLoader 4.3.x.
    - No imports are performed at package level to avoid side-effects.
    - The actual implementation resides in plugin.py.
    - Manifest.json defines plugin metadata and capabilities.
    - This __init__.py file must remain side‑effect free.

Compatibility:
    - RuntimeManager 4.3.x
    - PluginLoader 4.3.x
    - NL Router 4.3.x
    - SystemAgent 4.3.x
    - Workflow Engine 4.3.x
    - AI Loop 4.3.x

This file intentionally contains no executable code.
"""
