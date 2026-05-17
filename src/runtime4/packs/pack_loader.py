"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Loader (Runtime 4.3)

Responsible for:
- loading knowledge packs from disk or memory
- validating basic structure
- registering packs into runtime
- preparing packs for graph/linker stages
- enforcing Security Family 4.4 rules
- supporting Self‑Repair 4.4 diagnostics

This is the entry point for Knowledge Packs 2.0 (Runtime 4.3).
"""

from typing import Optional, Dict, Any


class PackLoader4:
    """
    Loads and registers Knowledge Packs 2.0.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, max_packs: int = 500):
        self.packs: Dict[str, Dict[str, Any]] = {}
        self.max_packs = max_packs
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_data(self, data: Any) -> bool:
        return isinstance(data, dict)

    def _validate_meta(self, meta: Any) -> bool:
        return meta is None or isinstance(meta, dict)

    # ---------------------------------------------------------
    # LOADING
    # ---------------------------------------------------------

    def load_pack(self, name: str, data: dict, meta: Optional[dict] = None) -> Dict[str, Any]:
        """
        Loads a pack into memory.
        In real implementation, this will load from disk.
        Includes full Runtime 4.3 safety validation.
        """

        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Pack loading disabled in safe-mode."
            }

        # Validate name
        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_pack_name"}

        # Validate data
        if not self._validate_data(data):
            return {"status": "error", "code": "invalid_pack_data"}

        # Validate meta
        if not self._validate_meta(meta):
            return {"status": "error", "code": "invalid_pack_meta"}

        # Prevent overwriting
        if name in self.packs:
            return {"status": "error", "code": "pack_already_loaded"}

        # Pack limit
        if len(self.packs) >= self.max_packs:
            return {"status": "error", "code": "pack_limit_reached"}

        try:
            self.packs[name] = {
                "data": data,
                "meta": meta or {}
            }

            return {
                "status": "success",
                "pack": name,
                "degraded_mode": self.degraded_mode
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "pack_load_failed",
                "exception": str(exc)
            }

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get_pack(self, name: str) -> Optional[Dict[str, Any]]:
        if not self._validate_name(name):
            return None
        return self.packs.get(name)

    def list_packs(self):
        return list(self.packs.keys())
