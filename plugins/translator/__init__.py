"""
SIRIUS LOCAL AI – Translator Plugin (v4.5.0)
--------------------------------------------

This package provides the Translator Plugin for SIRIUS Runtime 4.5.0.
It enables text translation through the ContextManager.translate() API.

Capabilities (4.5):
    - Natural language translation commands
    - AI task bindings for programmatic translation
    - Workflow integration (auto-translate workflows)
    - AI Loop rules for periodic translation checks
    - GUI elements for quick translation actions
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
