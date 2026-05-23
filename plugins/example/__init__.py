"""
SIRIUS LOCAL AI – Example Plugin (v4.5.0)
-----------------------------------------

This package contains the Example Plugin for SIRIUS Runtime 4.5.0.
It serves as a reference implementation for creating new SIRIUS plugins.

Demonstrated Concepts (4.5):
    - Plugin folder structure (Phase‑4.5)
    - manifest.json usage with integrity + self‑repair metadata
    - NL command registration
    - AI task registration
    - Workflow integration
    - AI Loop rule integration
    - GUI element registration
    - Deterministic, safe-mode aware plugin initialization
    - Plugin Integrity Hooks (4.5)
    - Health Metadata (4.5)
    - Self‑Repair Layer 4.5 compatibility

Architecture Notes:
    - Dynamically loaded through PluginLoader 4.5.0.
    - No imports at package level (side‑effect free).
    - Implementation resides in plugin.py.
    - manifest.json defines plugin metadata, capabilities, integrity rules, and health metadata.
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
