# File: src/runtime4/self_repair/__init__.py
"""
Self-Repair Layer (Phase‑5)
Version: 4.5.0
Module: self_repair

This module provides:
- Integrity scanning
- Automatic recovery
- Deterministic repair actions
- Fallback logic
- Repair logging
- Runtime stabilization hooks
"""

from .self_repair_engine import SelfRepairEngine
from .integrity_scanner import IntegrityScanner
from .recovery_protocol import RecoveryProtocol
from .module_rebuilder import ModuleRebuilder
from .fallback_manager import FallbackManager
from .repair_log import RepairLog

__all__ = [
    "SelfRepairEngine",
    "IntegrityScanner",
    "RecoveryProtocol",
    "ModuleRebuilder",
    "FallbackManager",
    "RepairLog",
]
