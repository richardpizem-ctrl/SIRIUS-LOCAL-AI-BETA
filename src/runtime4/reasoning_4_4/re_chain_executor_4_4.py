"""
SIRIUS LOCAL AI – Reasoning Chain Executor 4.5.0 (PRO)

Deterministic chain executor pre Reasoning Engine 4.5.

Účel:
- vykonáva sekvenčné reasoning kroky (chains)
- každý krok je čistá funkcia nad kontextom
- žiadne AI, žiadne heuristiky, žiadny eval/exec
- 100 % offline, deterministické
- kompatibilné so Security Family 4.5 a Self‑Repair 4.5
"""

from typing import Dict, Any, List, Callable


ChainStep45 = Callable[[Dict[str, Any]], Dict[str, Any]]


class ReasoningChainExecutor45:
    """
    Deterministic chain executor (PRO).
    """

    def __init__(self, rule_engine=None, symbolic_solver=None):
        self.rule_engine = rule_engine
        self.symbolic_solver = symbolic_solver

        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # Preddefinované chainy podľa typu dotazu
        self.named_chains: Dict[str, List[ChainStep45]] = {}

        # Registrácia default chainu
        self._register_default_chains()

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            if self.rule_engine:
                res = self.rule_engine.initialize()
                if res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "rule_engine_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

            if self.symbolic_solver:
                res = self.symbolic_solver.initialize()
                if res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "symbolic_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

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
    # DEFAULT CHAINS
    # ------------------------------------------------------------------
    def _register_default_chains(self) -> None:
        """
        Zaregistruje základné chainy.
        """

        self.named_chains["general"] = [
            self._step_collect_facts,
            self._step_apply_rules,
            self._step_aggregate,
        ]

        self.named_chains["math"] = [
            self._step_collect_facts,
            self._step_symbolic_if_present,
            self._step_aggregate,
        ]

    # ------------------------------------------------------------------
    # PUBLIC API – EXECUTE
    # ------------------------------------------------------------------
    def execute(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Vykoná chain podľa tém v kontexte.
        Deterministické, bezpečné, PRO.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Chain execution disabled in safe-mode.",
                "version": "4.5",
            }

        if not isinstance(query, str):
            return {"status": "error", "code": "invalid_query_type", "version": "4.5"}

        if not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type", "version": "4.5"}

        try:
            subjects = context.get("subjects", ["general"])
            chain_name = "math" if "math" in subjects else "general"
            steps = self.named_chains.get(chain_name, [])

            # Validate steps
            for step in steps:
                if not callable(step):
                    return {
                        "status": "error",
                        "code": "invalid_chain_step",
                        "step": str(step),
                        "version": "4.5",
                    }

            state: Dict[str, Any] = {
                "query": query,
                "subjects": subjects,
                "context": context,
                "facts": context.get("facts", []),
                "rules": context.get("rules", []),
                "symbolic": context.get("symbolic", []),
                "intermediate": [],
                "result": None,
            }

            for step in steps:
                state = step(state)
                if not isinstance(state, dict):
                    return {
                        "status": "error",
                        "code": "invalid_step_return",
                        "step": step.__name__,
                        "version": "4.5",
                    }

            return {
                "status": "ok",
                "chain": chain_name,
                "state": state,
                "degraded_mode": self.degraded_mode,
                "version": "4.5",
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "execution_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # STEP: COLLECT FACTS
    # ------------------------------------------------------------------
    def _step_collect_facts(self, state: Dict[str, Any]) -> Dict[str, Any]:
        state["intermediate"].append({
            "step": "collect_facts",
            "facts_count": len(state.get("facts", [])),
        })
        return state

    # ------------------------------------------------------------------
    # STEP: APPLY RULES
    # ------------------------------------------------------------------
    def _step_apply_rules(self, state: Dict[str, Any]) -> Dict[str, Any]:
        if not self.rule_engine:
            state["intermediate"].append({
                "step": "apply_rules",
                "status": "skipped_no_rule_engine",
            })
            return state

        rules_result = self.rule_engine.apply_rules(
            state["query"],
            state["context"],
        )

        state["intermediate"].append({
            "step": "apply_rules",
            "status": rules_result.get("status"),
        })
        state["result"] = rules_result
        return state

    # ------------------------------------------------------------------
    # STEP: SYMBOLIC
    # ------------------------------------------------------------------
    def _step_symbolic_if_present(self, state: Dict[str, Any]) -> Dict[str, Any]:
        if not self.symbolic_solver or not state.get("symbolic"):
            state["intermediate"].append({
                "step": "symbolic",
                "status": "skipped_no_symbolic_or_empty",
            })
            return state

        expr = state["symbolic"][0]
        simplified = self.symbolic_solver.simplify(expr)

        state["intermediate"].append({
            "step": "symbolic",
            "expr": expr,
            "status": simplified.get("status"),
        })
        state["result"] = simplified
        return state

    # ------------------------------------------------------------------
    # STEP: AGGREGATE
    # ------------------------------------------------------------------
    def _step_aggregate(self, state: Dict[str, Any]) -> Dict[str, Any]:
        state["intermediate"].append({
            "step": "aggregate",
            "status": "done",
        })
        return state

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "chains": list(self.named_chains.keys()),
            "version": "4.5",
        }
