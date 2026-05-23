"""
SIRIUS LOCAL AI – Notes Plugin (v4.5.0)
---------------------------------------

This package provides the Notes Plugin for SIRIUS Runtime 4.5.0.

Capabilities (4.5):
    - Create notes
    - List notes
    - Read notes
    - Delete notes
    - Natural language note commands
    - AI task bindings
    - Workflow integration
    - GUI elements for note management
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
