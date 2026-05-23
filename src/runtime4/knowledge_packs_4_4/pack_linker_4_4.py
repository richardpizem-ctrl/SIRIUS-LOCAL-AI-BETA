"""
SIRIUS LOCAL AI – Pack Linker 4.5.0 (PRO)

Pack Linker 4.5 provides deterministic, offline‑safe linking between
Knowledge Packs 4.5.

It supports:
- Cross‑pack references
- Dependency linking
- Relationship mapping
- Safe resolution of references
- Zero code execution (data‑only)
- Integration with KP Registry 4.5 and KP Metadata 4.5

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Only JSON/dict structures are processed.
- Linking is deterministic and reversible.
"""

from typing import Dict, Any, List, Optional


class PackLinker45:
    """
    Deterministic linker for Knowledge Packs 4.5.
    """

    def __init__(self, registry=None, metadata=None):
        self.registry = registry
        self.metadata = metadata

        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------------
    def _get_pack_data(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registry stores full pack dict:
        { name, version, pack_type, data, metadata }
        Linker must operate ONLY on pack["data"].
        """
        if not isinstance(pack, dict):
            return {}
        data = pack.get("data", {})
        return data if isinstance(data, dict) else {}

    def _validate_ref(self, ref: Any) -> bool:
        return isinstance(ref, str) and ":" in ref

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            if self.registry:
                res = self.registry.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "registry_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

            if self.metadata:
                res = self.metadata.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "metadata_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

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
    # RESOLVE REFERENCES FOR ONE PACK
    # ------------------------------------------------------------------
    def resolve_references(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolves cross‑pack references of the form:
        { "ref": "pack_name:key" }
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Linker disabled in safe-mode.",
                "version": "4.5",
            }

        if not self.registry:
            return {"status": "error", "code": "no_registry", "version": "4.5"}

        try:
            data = self._get_pack_data(pack)
            resolved = dict(data)

            for key, value in data.items():
                if isinstance(value, dict) and "ref" in value:
                    ref = value["ref"]

                    if not self._validate_ref(ref):
                        return {
                            "status": "error",
                            "code": "invalid_reference_format",
                            "ref": ref,
                            "version": "4.5",
                        }

                    pack_name, ref_key = ref.split(":", 1)

                    target_pack = self.registry.get(pack_name)
                    if not target_pack:
                        return {
                            "status": "error",
                            "code": "target_pack_not_found",
                            "ref": ref,
                            "version": "4.5",
                        }

                    target_data = self._get_pack_data(target_pack)
                    if ref_key not in target_data:
                        return {
                            "status": "error",
                            "code": "target_key_not_found",
                            "ref": ref,
                            "version": "4.5",
                        }

                    resolved[key] = target_data[ref_key]

            return {"status": "ok", "resolved": resolved, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "resolve_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # LINK ALL PACKS
    # ------------------------------------------------------------------
    def link_all(self) -> Dict[str, Any]:
        """
        Resolves references for all registered packs.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "linked": {},
                "failed": [],
                "version": "4.5",
            }

        if not self.registry:
            return {"status": "error", "code": "no_registry", "version": "4.5"}

        linked = {}
        failed = []

        try:
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
                "version": "4.5",
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "link_all_failed",
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
