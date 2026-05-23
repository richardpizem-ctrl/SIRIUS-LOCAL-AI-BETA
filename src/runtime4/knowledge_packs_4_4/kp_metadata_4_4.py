"""
SIRIUS LOCAL AI – Knowledge Pack Metadata Engine 4.5.0 (PRO)

KP Metadata 4.5 provides deterministic, offline‑safe metadata handling for
Knowledge Packs. It enriches packs with:

- Version info
- Deterministic timestamps (monotonic, not real-time)
- Author info
- Tags
- Descriptions

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Metadata must be pure JSON/dict.
- Fully offline, deterministic, isolated.
- No real-time system calls allowed (Runtime 4.5 PRO rule).
"""

from typing import Dict, Any


class KnowledgePackMetadata45:
    """
    Deterministic metadata handler for Knowledge Packs 4.5.
    """

    VERSION = "4.5.0"

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # Deterministic timestamp counter (Runtime 4.5 PRO requirement)
        self._counter = 1

    # ------------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------------
    def _next_timestamp(self) -> int:
        """
        Deterministic timestamp generator.
        Runtime 4.5 PRO forbids real-time calls.
        """
        ts = self._counter
        self._counter += 1
        return ts

    def _validate_json_safe(self, value: Any) -> bool:
        return isinstance(value, (str, int, float, bool, dict, list))

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
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # ATTACH METADATA TO PACK
    # ------------------------------------------------------------------
    def attach_metadata(self, pack) -> Dict[str, Any]:
        """
        Enriches a Knowledge Pack with deterministic metadata fields.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Metadata engine disabled in safe-mode.",
                "version": "4.5",
            }

        try:
            meta = pack.metadata or {}

            # Deterministic timestamps
            meta.setdefault("created_at", self._next_timestamp())
            meta["updated_at"] = self._next_timestamp()

            # Version
            meta.setdefault("kp_version", self.VERSION)

            # Tags
            if "tags" not in meta or not isinstance(meta["tags"], list):
                meta["tags"] = []

            # Description
            if "description" not in meta or not isinstance(meta["description"], str):
                meta["description"] = f"Knowledge Pack '{pack.name}'"

            # Validate JSON-safe metadata
            for key, value in meta.items():
                if not self._validate_json_safe(value):
                    return {
                        "status": "error",
                        "code": "invalid_metadata_value",
                        "field": key,
                        "version": "4.5",
                    }

            pack.metadata = meta
            return {"status": "ok", "pack": pack, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "attach_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # MERGE METADATA
    # ------------------------------------------------------------------
    def merge_metadata(self, pack, new_meta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Safely merges new metadata fields into an existing pack.
        Deterministic, JSON-safe only.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Metadata engine disabled in safe-mode.",
                "version": "4.5",
            }

        try:
            meta = pack.metadata or {}

            for key, value in new_meta.items():
                if self._validate_json_safe(value):
                    meta[key] = value
                else:
                    return {
                        "status": "error",
                        "code": "invalid_metadata_value",
                        "field": key,
                        "version": "4.5",
                    }

            # Update timestamp deterministically
            meta["updated_at"] = self._next_timestamp()

            pack.metadata = meta
            return {"status": "ok", "pack": pack, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "merge_failed",
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
