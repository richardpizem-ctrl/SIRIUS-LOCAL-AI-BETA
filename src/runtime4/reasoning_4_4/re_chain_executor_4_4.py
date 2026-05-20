# reasoning_4_4/re_chain_executor_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Chain Executor 4.4.0

Deterministic chain executor pre Reasoning Engine 4.4.

Účel:
- vykonáva sekvenčné reasoning kroky (chains)
- každý krok je čistá funkcia nad kontextom
- žiadne AI, žiadne heuristiky, žiadny eval/exec
- 100 % offline, deterministické

Typický chain:
1. výber relevantných faktov
2. aplikácia pravidiel
3. voliteľne symbolické výpočty
4. agregácia výsledkov
"""

from typing import Dict, Any, List, Callable


ChainStep44 = Callable[[Dict[str, Any]], Dict[str, Any]]


class ReasoningChainExecutor44:
    """
    Deterministic chain executor.
    """

    def __init__(self, rule_engine=None, symbolic_solver=None):
        self.rule_engine = rule_engine
        self.symbolic_solver = symbolic_solver

        self.initialized = False
        self.degraded_mode = False

        # Preddefinované chainy podľa typu dotazu
        self.named_chains: Dict[str, List[ChainStep44]] = {}

        # Registrácia default chainu
        self._register_default_chains()

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.rule_engine:
                self.rule_engine.initialize()
            if self.symbolic_solver:
                self.symbolic_solver.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # DEFAULT CHAINS
    # ------------------------------------------------------------------
    def _register_default_chains(self) -> None:
        """
        Zaregistruje základné chainy.
        """

        # General chain – fakty + pravidlá
        self.named_chains["general"] = [
            self._step_collect_facts,
            self._step_apply_rules,
            self._step_aggregate,
        ]

        # Math chain – fakty + symbolika
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
        """

        try:
            subjects = context.get("subjects", ["general"])
            chain_name = "math" if "math" in subjects else "general"
            steps = self.named_chains.get(chain_name, [])

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

            return {
                "status": "ok",
                "chain": chain_name,
                "state": state,
            }

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STEP: COLLECT FACTS (tu už sú v kontexte, len ich môžeme filtrovať)
    # ------------------------------------------------------------------
    def _step_collect_facts(self, state: Dict[str, Any]) -> Dict[str, Any]:
        # Tu môžeš neskôr pridať filtráciu podľa query/subjects
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
    # STEP: SYMBOLIC (ak je prítomný výraz)
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
        """
        Jednoduchá agregácia – v tejto verzii len nechá posledný result.
        Neskôr môžeš pridať kombináciu viacerých zdrojov.
        """

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
            "degraded_mode": self.degraded_mode,
            "chains": list(self.named_chains.keys()),
        }
