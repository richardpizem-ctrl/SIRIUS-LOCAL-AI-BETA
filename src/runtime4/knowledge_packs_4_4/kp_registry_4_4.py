"""
SIRIUS LOCAL AI – Knowledge Pack Registry 4.5.0 (PRO)

KP Registry 4.5 is the central deterministic storage for all loaded
Knowledge Packs. It provides:

- Safe registration
- Duplicate detection
- Version tracking
- Retrieval by name
- Listing all packs
- Clearing registry
- Integration with Loader, Validator, Linker, Query Engine

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Registry stores ONLY JSON/dict structures.
- Fully offline, deterministic, isolated.
- No executable content allowed.
"""

from typing import Dict, Any, Optional


class KnowledgePackRegistry45:
    """
    Deterministic registry for Knowledge Packs 4.5.
    """

    def __init__(self):
        self.packs: Dict[str, Dict[str, Any]] = {}
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL VALIDATION
    # ------------------------------------------------------------------
    def _validate_pack(self, pack: Any) -> bool:
        if not isinstance(pack, dict):
            return False

        required = ["name", "version", "pack_type", "data"]
        for r in required:
            if r not in pack:
                return False

        if not isinstance(pack["name"], str) or not pack["name"].strip():
            return False

        if not isinstance(pack["version"], str) or not pack["version"].strip():
            return False

        if not isinstance(pack["pack_type"], str) or not pack["pack_type"].strip():
            return False

        if not isinstance(pack["data"], dict):
            return False

        # No executable content allowed
        for v in pack["data"].values():
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
            self.packs = {}
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
    # REGISTER PACK
    # ------------------------------------------------------------------
    def register(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Registry disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_pack(pack):
            return {"status": "error", "code": "invalid_pack", "version": "4.5"}

        name = pack["name"]

        # Duplicate detection
        if name in self.packs:
            return {
                "status": "error",
                "code": "duplicate_pack",
                "existing_version": self.packs[name].get("version"),
                "version": "4.5",
            }

        try:
            # Store pack deterministically
            self.packs[name] = dict(pack)
            return {
                "status": "ok",
                "name": name,
                "version": pack["version"],
                "version_info": "4.5",
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "register_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # GET PACK BY NAME
    # ------------------------------------------------------------------
    def get(self, name: str) -> Optional[Dict[str, Any]]:
        if not isinstance(name, str) or not name.strip():
            return None
        return self.packs.get(name)

    # ------------------------------------------------------------------
    # GET ALL PACKS
    # ------------------------------------------------------------------
    def get_all(self) -> Dict[str, Dict[str, Any]]:
        return dict(self.packs)

    # ------------------------------------------------------------------
    # CLEAR REGISTRY
    # ------------------------------------------------------------------
    def clear(self) -> Dict[str, Any]:
        try:
            self.packs.clear()
            return {"status": "ok", "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "clear_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "count": len(self.packs),
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "version": "4.5",
        }
