knowledge_packs_4_4/kp_query_engine_4_4.py
"""
SIRIUS LOCAL AI – Knowledge Pack Query Engine 4.4.0

KP Query Engine 4.4 provides deterministic, offline‑safe search and lookup
capabilities across all registered Knowledge Packs.

Features:
- Exact key lookup
- Prefix search
- Full‑pack search
- Cross‑pack search
- Safe fuzzy‑like matching (no AI, no heuristics)
- Integration with KP Registry 4.4
- Zero code execution

Security Notes:
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

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                self.registry.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # EXACT LOOKUP
    # ------------------------------------------------------------------
    def get(self, pack_name: str, key: str) -> Dict[str, Any]:
        """
        Returns a single value from a specific pack.
        """

        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

        pack = self.registry.get(pack_name)
        if not pack:
            return {"status": "error", "reason": "pack_not_found"}

        data = pack.get("data", {})
        if key not in data:
            return {"status": "error", "reason": "key_not_found"}

        return {"status": "ok", "value": data[key]}

    # ------------------------------------------------------------------
    # PREFIX SEARCH
    # ------------------------------------------------------------------
    def prefix_search(self, prefix: str) -> Dict[str, Any]:
        """
        Returns all entries whose keys start with the given prefix.
        """

        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

        results = []

        for pack_name, pack in self.registry.get_all().items():
            for key, value in pack.get("data", {}).items():
                if key.startswith(prefix):
                    results.append({
                        "pack": pack_name,
                        "key": key,
                        "value": value,
                    })

        return {"status": "ok", "results": results}

    # ------------------------------------------------------------------
    # FULL SEARCH (substring)
    # ------------------------------------------------------------------
    def search(self, text: str) -> Dict[str, Any]:
        """
        Searches all packs for keys or values containing the given text.
        """

        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

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

    # ------------------------------------------------------------------
    # SAFE "FUZZY" MATCH (deterministic)
    # ------------------------------------------------------------------
    def fuzzy(self, text: str) -> Dict[str, Any]:
        """
        Safe fuzzy-like matching:
        - substring match
        - prefix match
        - case-insensitive
        - no heuristics, no AI
        """

        prefix = self.prefix_search(text)
        substring = self.search(text)

        combined = prefix.get("results", []) + substring.get("results", [])

        # Remove duplicates
        unique = []
        seen = set()

        for item in combined:
            key = (item["pack"], item["key"])
            if key not in seen:
                seen.add(key)
                unique.append(item)

        return {"status": "ok", "results": unique}

    # ------------------------------------------------------------------
    # GET ALL KEYS FROM PACK
    # ------------------------------------------------------------------
    def list_keys(self, pack_name: str) -> Dict[str, Any]:
        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

        pack = self.registry.get(pack_name)
        if not pack:
            return {"status": "error", "reason": "pack_not_found"}

        return {"status": "ok", "keys": list(pack.get("data", {}).keys())}

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
