"""
SIRIUS LOCAL AI – Reasoning Context Builder 4.4.0 (PRO)

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
    Deterministic context builder pre Reasoning Engine 4.4 (PRO).
    """

    def __init__(self, registry=None, query_engine=None, context_memory=None):
        self.registry = registry
        self.query_engine = query_engine
        self.context_memory = context_memory

        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                res = self.registry.initialize()
                if res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "registry_init_failed", "details": res}

            if self.query_engine:
                res = self.query_engine.initialize()
                if res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "query_engine_init_failed", "details": res}

            if self.context_memory:
                res = self.context_memory.initialize()
                if res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "context_memory_init_failed", "details": res}

            self.initialized = True
            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SELECT PACKS BY SUBJECT
    # ------------------------------------------------------------------
    def _select_packs(self, subjects: List[str]) -> List[str]:
        """
        Deterministické mapovanie tém → packy.
        Žiadne heuristiky, žiadne AI.
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
            if isinstance(s, str):
                packs.extend(mapping.get(s, []))

        # odstránenie duplicít deterministicky
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

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Context building disabled in safe-mode."}

        if not isinstance(subjects, list):
            return {"status": "error", "code": "invalid_subjects_type"}

        if not self.context_memory:
            return {"status": "error", "code": "no_context_memory"}

        try:
            # 1. Vyber packy
            packs = self._select_packs(subjects)

            # 2. Zaregistruj packy do context memory
            for p in packs:
                self.context_memory.add_pack(p)

            # 3. Načítaj fakty z packov
            for p in packs:
                keys = self.query_engine.list_keys(p)
                if keys.get("status") != "ok":
                    continue

                for key in keys.get("keys", []):
                    fact = self.query_engine.get(p, key)
                    if fact.get("status") == "ok":
                        self.context_memory.add_fact(
                            pack=p,
                            key=key,
                            value=fact["value"]
                        )

            # 4. Export kontextu
            exported = self.context_memory.export()
            exported["status"] = "ok"
            exported["degraded_mode"] = self.degraded_mode
            return exported

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "context_build_failed", "exception": str(exc)}

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
