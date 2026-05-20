"""
SIRIUS LOCAL AI – Knowledge Pack Query Engine 4.4.0 (PRO)

KP Query Engine 4.4 provides deterministic, offline‑safe search and lookup
capabilities across all registered Knowledge Packs.

Features:
- Exact key lookup
- Prefix search
- Substring search
- Cross‑pack search
- Deterministic fuzzy‑like matching (no heuristics)
- Integration with KP Registry 4.4
- Zero code execution

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Only JSON/dict structures are processed.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any, List, Optional


class KnowledgePackQueryEngine44:
    """
    Deterministic query engine for Knowledge Packs 4.4.
    """

    def __init__(self, registry=None):
        self.registry = registry
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL VALIDATION
    # ------------------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_registry(self) -> bool:
        return self.registry is not None

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                res = self.registry.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "registry_init_failed"}

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # EXACT LOOKUP
    # ------------------------------------------------------------------
    def get(self, pack_name: str, key: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Query engine disabled in safe-mode."}

        if not self._validate_registry():
            return {"status": "error", "code": "no_registry"}

        if not self._validate_str(pack_name):
            return {"status": "error", "code": "invalid_pack_name"}

        if not self._validate_str(key):
            return {"status": "error", "code": "invalid_key"}

        try:
            pack = self.registry.get(pack_name)
            if not pack:
                return {"status": "error", "code": "pack_not_found"}

            data = pack.get("data", {})
            if key not in data:
                return {"status": "error", "code": "key_not_found"}

            return {"status": "ok", "value": data[key]}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "lookup_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # PREFIX SEARCH
    # ------------------------------------------------------------------
    def prefix_search(self, prefix: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Query engine disabled in safe-mode."}

        if not self._validate_registry():
            return {"status": "error", "code": "no_registry"}

        if not self._validate_str(prefix):
            return {"status": "error", "code": "invalid_prefix"}

        try:
            results = []
            all_packs = self.registry.get_all()

            for pack_name, pack in all_packs.items():
                for key, value in pack.get("data", {}).items():
                    if key.startswith(prefix):
                        results.append({
                            "pack": pack_name,
                            "key": key,
                            "value": value,
                        })

            return {"status": "ok", "results": results}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "prefix_search_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # FULL SEARCH (substring)
    # ------------------------------------------------------------------
    def search(self, text: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Query engine disabled in safe-mode."}

        if not self._validate_registry():
            return {"status": "error", "code": "no_registry"}

        if not self._validate_str(text):
            return {"status": "error", "code": "invalid_search_text"}

        try:
            text_lower = text.lower()
            results = []

            for pack_name, pack in self.registry.get_all().items():
                for key, value in pack.get("data", {}).items():
                    key_match = text_lower in key.lower()
                    value_match = isinstance(value, str) and text_lower in value.lower()

                    if key_match or value_match:
                        results.append({
                            "pack": pack_name,
                            "key": key,
                            "value": value,
                        })

            return {"status": "ok", "results": results}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "search_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SAFE DETERMINISTIC "FUZZY" MATCH
    # ------------------------------------------------------------------
    def fuzzy(self, text: str) -> Dict[str, Any]:
        """
        Deterministic fuzzy-like matching:
        - substring match
        - prefix match
        - case-insensitive
        - no heuristics, no scoring, no AI
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Query engine disabled in safe-mode."}

        if not self._validate_str(text):
            return {"status": "error", "code": "invalid_fuzzy_text"}

        try:
            prefix = self.prefix_search(text)
            substring = self.search(text)

            combined = prefix.get("results", []) + substring.get("results", [])

            # Deduplicate
            unique = []
            seen = set()

            for item in combined:
                key = (item["pack"], item["key"])
                if key not in seen:
                    seen.add(key)
                    unique.append(item)

            return {"status": "ok", "results": unique}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "fuzzy_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # LIST KEYS
    # ------------------------------------------------------------------
    def list_keys(self, pack_name: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Query engine disabled in safe-mode."}

        if not self._validate_registry():
            return {"status": "error", "code": "no_registry"}

        if not self._validate_str(pack_name):
            return {"status": "error", "code": "invalid_pack_name"}

        try:
            pack = self.registry.get(pack_name)
            if not pack:
                return {"status": "error", "code": "pack_not_found"}

            return {"status": "ok", "keys": list(pack.get("data", {}).keys())}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "list_keys_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
