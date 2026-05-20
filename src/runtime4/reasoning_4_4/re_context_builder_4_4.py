# reasoning_4_4/re_context_builder_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Context Builder 4.4.0

Účel:
- vytvára reasoning kontext pre jeden dotaz
- vyberá relevantné Knowledge Packy podľa tém
- ťahá fakty z KP Query Engine 4.4
- zapisuje všetko do Reasoning Context Memory 4.4
- 100 % offline, deterministické, bez AI heuristiky

Používa:
- KP Registry 4.4
- KP Query Engine 4.4
- Reasoning Context Memory 4.4
"""

from typing import Dict, Any, List


class ReasoningContextBuilder44:
    """
    Deterministic context builder pre Reasoning Engine 4.4.
    """

    def __init__(self, registry=None, query_engine=None, context_memory=None):
        self.registry = registry
        self.query_engine = query_engine
        self.context_memory = context_memory

        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                self.registry.initialize()
            if self.query_engine:
                self.query_engine.initialize()
            if self.context_memory:
                self.context_memory.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SELECT PACKS BY SUBJECT
    # ------------------------------------------------------------------
    def _select_packs(self, subjects: List[str]) -> List[str]:
        """
        Jednoduché deterministické mapovanie tém → packy.
        """

        mapping = {
            "math": ["math_pack"],
            "history": ["history_pack"],
            "language": ["language_pack"],
            "science": ["science_pack"],
            "geography": ["geography_pack"],
            "general": ["general_pack"],
        }

        packs = []
        for s in subjects:
            packs.extend(mapping.get(s, []))

        # odstráni duplicity
        return list(dict.fromkeys(packs))

    # ------------------------------------------------------------------
    # BUILD CONTEXT
    # ------------------------------------------------------------------
    def build_context(self, subjects: List[str]) -> Dict[str, Any]:
        """
        Hlavná funkcia:
        - vyberie packy
        - načíta fakty
        - uloží všetko do context memory
        """

        try:
            if not self.context_memory:
                return {"status": "error", "reason": "no_context_memory"}

            # 1. Vyber packy
            packs = self._select_packs(subjects)

            for p in packs:
                self.context_memory.add_pack(p)

            # 2. Načítaj fakty z packov
            for p in packs:
                keys = self.query_engine.list_keys(p)
                if keys.get("status") != "ok":
                    continue

                for key in keys["keys"]:
                    fact = self.query_engine.get(p, key)
                    if fact.get("status") == "ok":
                        self.context_memory.add_fact(
                            pack=p,
                            key=key,
                            value=fact["value"]
                        )

            # 3. Export kontextu
            return self.context_memory.export()

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
