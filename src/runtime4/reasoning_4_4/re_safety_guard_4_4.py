"""
SIRIUS LOCAL AI – Reasoning Safety Guard 4.5.0 (PRO)

Účel:
- bezpečnostná vrstva nad Reasoning Engine 4.5
- kontroluje dotazy a kontext pred reasoningom
- vynucuje:
    - offline režim
    - žiadne volanie vonkajších služieb
    - žiadne dynamické importy, eval, exec
    - žiadne systémové príkazy
- 100 % deterministické, bez AI heuristiky
- kompatibilné so Security Family 4.5 a Self‑Repair 4.5
"""

from typing import Dict, Any, List


class ReasoningSafetyGuard45:
    """
    Deterministic safety guard pre Reasoning Engine 4.5 (PRO).
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # Zakázané patterny v dotaze (deterministické)
        self.forbidden_substrings: List[str] = [
            "import ",
            "exec(",
            "eval(",
            "__import__",
            "os.system",
            "subprocess",
            "http://",
            "https://",
            "curl ",
            "wget ",
        ]

        # Maximálna dĺžka dotazu
        self.max_query_length: int = 4000

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            self.initialized = True
            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # CHECK QUERY
    # ------------------------------------------------------------------
    def check_query(self, query: str) -> Dict[str, Any]:
        """
        Skontroluje, či je dotaz bezpečný.
        Deterministické, bez heuristiky.
        """

        if not isinstance(query, str):
            return {"status": "blocked", "code": "invalid_query_type", "version": "4.5"}

        if len(query) > self.max_query_length:
            return {
                "status": "blocked",
                "code": "query_too_long",
                "max_length": self.max_query_length,
                "actual_length": len(query),
                "version": "4.5",
            }

        lower_q = query.lower()
        for forbidden in self.forbidden_substrings:
            if forbidden in lower_q:
                return {
                    "status": "blocked",
                    "code": "forbidden_pattern",
                    "pattern": forbidden,
                    "version": "4.5",
                }

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # CHECK CONTEXT
    # ------------------------------------------------------------------
    def check_context(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Skontroluje, či kontext neobsahuje nebezpečné hodnoty.
        """

        if not isinstance(context, dict):
            return {"status": "blocked", "code": "invalid_context_type", "version": "4.5"}

        # Kontrola faktov
        for fact in context.get("facts", []):
            if not isinstance(fact, dict):
                return {"status": "blocked", "code": "invalid_fact_type", "version": "4.5"}

            value = str(fact.get("value", "")).lower()

            for forbidden in ["http://", "https://", "import ", "exec(", "eval("]:
                if forbidden in value:
                    return {
                        "status": "blocked",
                        "code": "forbidden_in_fact",
                        "pattern": forbidden,
                        "fact_key": fact.get("key"),
                        "pack": fact.get("pack"),
                        "version": "4.5",
                    }

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # GUARD REASONING CALL
    # ------------------------------------------------------------------
    def guard_reasoning(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Kombinovaná kontrola dotazu + kontextu.
        Ak čokoľvek zlyhá, reasoning sa nemá vykonať.
        """

        if self.safe_mode:
            return {"status": "blocked", "code": "safe_mode", "version": "4.5"}

        q_check = self.check_query(query)
        if q_check.get("status") != "ok":
            return {
                "status": "blocked",
                "stage": "query",
                "details": q_check,
                "version": "4.5",
            }

        c_check = self.check_context(context)
        if c_check.get("status") != "ok":
            return {
                "status": "blocked",
                "stage": "context",
                "details": c_check,
                "version": "4.5",
            }

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "max_query_length": self.max_query_length,
            "forbidden_patterns_count": len(self.forbidden_substrings),
            "version": "4.5",
        }
