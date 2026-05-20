knowledge_packs_4_4/kp_registry_4_4.py
"""
SIRIUS LOCAL AI – Knowledge Pack Registry 4.4.0

KP Registry 4.4 is the central deterministic storage for all loaded
Knowledge Packs. It provides:

- Safe registration
- Duplicate detection
- Version tracking
- Retrieval by name
- Listing all packs
- Clearing registry
- Integration with Loader, Validator, Linker, Query Engine

Security Notes:
- No dynamic imports, no eval, no reflection.
- Registry stores ONLY JSON/dict structures.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any, Optional


class KnowledgePackRegistry44:
    """
    Deterministic registry for Knowledge Packs 4.4.
    """

    def __init__(self):
        self.packs: Dict[str, Dict[str, Any]] = {}
        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.packs = {}
            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # REGISTER PACK
    # ------------------------------------------------------------------
    def register(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registers a Knowledge Pack 4.4.
        Pack must contain:
        - name
        - version
        - pack_type
        - data
        """

        name = pack.get("name")
        version = pack.get("version")

        if not name or not version:
            return {
                "status": "error",
                "reason": "missing_required_fields",
            }

        # Duplicate detection
        if name in self.packs:
            return {
                "status": "error",
                "reason": "duplicate_pack",
                "existing_version": self.packs[name].get("version"),
            }

        # Store pack
        self.packs[name] = pack
        return {"status": "ok", "name": name, "version": version}

    # ------------------------------------------------------------------
    # GET PACK BY NAME
    # ------------------------------------------------------------------
    def get(self, name: str) -> Optional[Dict[str, Any]]:
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
        self.packs.clear()
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "count": len(self.packs),
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
