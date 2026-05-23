"""
SIRIUS LOCAL AI – Knowledge Packs Core 4.5.0 (PRO)

KP Core 4.5 provides the foundational structures and rules for the entire
Knowledge Packs subsystem in Runtime 4.5.

This module defines:
- Pack schema structure
- Pack types (strict whitelist)
- Deterministic constraints
- Safe pack container (no executable content)
- Versioning rules
- Base utilities used by all KP modules

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Packs must be pure JSON or Python dicts.
- No executable code inside packs.
- Fully offline, deterministic, isolated.
- All validation must be structural only.
"""

from typing import Dict, Any, Optional


# =========================================================================
# SAFE PACK CONTAINER
# =========================================================================

class KnowledgePack45:
    """
    Deterministic container for a Knowledge Pack 4.5.
    """

    def __init__(
        self,
        name: str,
        version: str,
        pack_type: str,
        data: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
    ):
        self.name = name
        self.version = version
        self.pack_type = pack_type
        self.data = data
        self.metadata = metadata or {}

    # ------------------------------------------------------------------
    # SERIALIZATION
    # ------------------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the pack into a JSON‑safe dictionary.
        Deterministic, no transformation.
        """
        return {
            "name": self.name,
            "version": self.version,
            "pack_type": self.pack_type,
            "data": self.data,
            "metadata": self.metadata,
        }

    # ------------------------------------------------------------------
    # BASIC VALIDATION
    # ------------------------------------------------------------------
    def is_valid(self) -> bool:
        """
        Minimal structural validation.
        Full validation is done by KP Validator 4.5.
        """
        if not isinstance(self.name, str) or not self.name.strip():
            return False
        if not isinstance(self.version, str) or not self.version.strip():
            return False
        if not isinstance(self.pack_type, str) or not self.pack_type.strip():
            return False
        if not isinstance(self.data, dict):
            return False
        if not isinstance(self.metadata, dict):
            return False

        # No executable content allowed
        for key, value in self.data.items():
            if callable(value):
                return False

        return True


# =========================================================================
# CORE UTILITIES
# =========================================================================

class KnowledgePackCore45:
    """
    Core utilities and constants for Knowledge Packs 4.5.
    Deterministic, offline, safe.
    """

    PACK_TYPES = {
        "general",
        "math",
        "language",
        "science",
        "history",
        "geography",
    }

    VERSION_FORMAT = "4.5"

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL VALIDATION
    # ------------------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_data(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        # No executable content allowed
        for v in data.values():
            if callable(v):
                return False
        return True

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ------------------------------------------------------------------
    # CREATE PACK
    # ------------------------------------------------------------------
    def create_pack(
        self,
        name: str,
        pack_type: str,
        data: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Creates a new Knowledge Pack 4.5 container.
        Deterministic, strict validation.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "KP Core disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if pack_type not in self.PACK_TYPES:
            return {
                "status": "error",
                "code": "invalid_pack_type",
                "allowed": sorted(self.PACK_TYPES),
                "version": "4.5",
            }

        if not self._validate_data(data):
            return {"status": "error", "code": "invalid_data", "version": "4.5"}

        if metadata is not None and not isinstance(metadata, dict):
            return {"status": "error", "code": "invalid_metadata", "version": "4.5"}

        try:
            pack = KnowledgePack45(
                name=name,
                version=self.VERSION_FORMAT,
                pack_type=pack_type,
                data=data,
                metadata=metadata,
            )

            if not pack.is_valid():
                return {"status": "error", "code": "invalid_pack_structure", "version": "4.5"}

            return {"status": "ok", "pack": pack, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "create_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "version": "4.5",
        }
