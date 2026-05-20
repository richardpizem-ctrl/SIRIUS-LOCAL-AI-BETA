"""
SIRIUS LOCAL AI – System Tools Plugin (v4.4.0)
----------------------------------------------

This package provides the System Tools Plugin for SIRIUS Runtime 4.4.0.

Capabilities (4.4):
    - CPU usage monitoring
    - RAM usage monitoring
    - Disk usage reporting
    - OS information retrieval
    - Natural language system info commands
    - AI task bindings for diagnostics
    - Workflow integration (system_diagnostics workflow)
    - GUI elements for quick system checks
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
