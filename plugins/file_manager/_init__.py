"""
SIRIUS LOCAL AI – File Manager Plugin (v4.5.0)
----------------------------------------------

This package provides the File Manager Plugin for SIRIUS Runtime 4.5.0.

Capabilities (4.5):
    - Create folders
    - Move files
    - Delete files
    - List directory contents
    - Natural language file operations
    - AI task bindings
    - Workflow integration
    - GUI elements for file actions
    - Safe‑Mode / Degraded‑Mode support
    - Deterministic offline-only behavior
    - Plugin Integrity Hooks (4.5)
    - Health Metadata (4.5)
    - Self‑Repair Layer 4.5 compatibility

Architecture Notes:
    - Dynamically loaded through PluginLoader 4.5.0.
    - No imports at package level (side‑effect free).
    - Implementation resides in plugin.py.
    - manifest.json defines plugin metadata, health, and integrity rules.
    - This __init__.py file must remain strictly passive.

Compatibility:
    - RuntimeManager 4.5.0
    - PluginLoader 4.5.0
    - NL Router 4.5.0
    - SystemAgent 4.5.0
    - Workflow Engine 4.5.0
    - AI Loop 4.5.0
    - Self‑Repair Layer 4.5

This file intentionally contains no executable code.
"""
