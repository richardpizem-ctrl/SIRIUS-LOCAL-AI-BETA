"""
SIRIUS LOCAL AI – Example Plugin (v4.3.x)
-----------------------------------------

This package contains the Example Plugin for SIRIUS Runtime 4.3.x.
It serves as a reference implementation for creating new SIRIUS plugins.

Demonstrated Concepts:
    - Plugin folder structure
    - manifest.json usage (Phase‑4 format)
    - NL command registration
    - AI task registration
    - Workflow integration
    - AI Loop rule integration
    - GUI element registration
    - Safe, deterministic plugin initialization

Architecture Notes:
    - The plugin is dynamically loaded through PluginLoader 4.3.x.
    - No imports are performed at package level to avoid side-effects.
    - The actual implementation resides in plugin.py.
    - Manifest.json defines plugin metadata, capabilities, and architecture flags.
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
