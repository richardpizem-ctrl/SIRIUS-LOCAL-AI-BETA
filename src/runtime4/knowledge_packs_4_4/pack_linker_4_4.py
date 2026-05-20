knowledge_packs_4_4/pack_linker_4_4.py
"""
SIRIUS LOCAL AI – Pack Linker 4.4.0

Pack Linker 4.4 provides deterministic, offline‑safe linking between
Knowledge Packs 4.4.

It supports:
- Cross‑pack references
- Dependency linking
- Relationship mapping
- Safe resolution of references
- Zero code execution (data‑only)
- Integration with KP Registry 4.4 and KP Metadata 4.4

Security Notes:
- No dynamic imports, no eval, no reflection.
- Only JSON/dict structures are processed.
- Linking is deterministic and reversible.
"""

from typing import Dict, Any, List


class PackLinker44:
    """
    Deterministic linker for Knowledge Packs 4.4.
    """

    def __init__(self, registry=None, metadata=None):
        self.registry = registry
        self.metadata = metadata

        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                self.registry.initialize()
            if self.metadata:
                self.metadata.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # RESOLVE REFERENCES
    # ------------------------------------------------------------------
    def resolve_references(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolves cross‑pack references of the form:
        {
            "ref": "pack_name:key"
        }

        Example:
        {
            "ref": "math_pack:pi"
        }
        """

        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

        resolved_pack = dict(pack)

        for key, value in pack.items():
            if isinstance(value, dict) and "ref" in value:
                ref = value["ref"]

                # Format: pack:key
                if ":" not in ref:
                    return {
                        "status": "error",
                        "reason": "invalid_reference_format",
                        "ref": ref,
                    }

                pack_name, ref_key = ref.split(":", 1)

                target_pack = self.registry.get(pack_name)
                if not target_pack:
                    return {
                        "status": "error",
                        "reason": "target_pack_not_found",
                        "ref": ref,
                    }

                if ref_key not in target_pack:
                    return {
                        "status": "error",
                        "reason": "target_key_not_found",
                        "ref": ref,
                    }

                resolved_pack[key] = target_pack[ref_key]

        return {"status": "ok", "resolved": resolved_pack}

    # ------------------------------------------------------------------
    # LINK MULTIPLE PACKS
    # ------------------------------------------------------------------
    def link_all(self) -> Dict[str, Any]:
        """
        Resolves references for all registered packs.
        """

        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

        linked = {}
        failed = []

        for name, pack in self.registry.get_all().items():
            result = self.resolve_references(pack)
            if result.get("status") == "ok":
                linked[name] = result["resolved"]
            else:
                failed.append({"pack": name, "error": result})

        return {
            "status": "ok",
            "linked": linked,
            "failed": failed,
        }

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }

