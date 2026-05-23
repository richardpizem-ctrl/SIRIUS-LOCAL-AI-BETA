from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextDiffCommand(BaseCommand):
    """
    ContextDiffCommand 4.5
    Compares the current context state with values stored in memory.

    Updated in 4.5:
        - Self‑Repair Layer 4.5 compatibility
        - Deterministic diff output (unchanged)
        - Stable structure for Runtime4.5 and NL Router 4.5
        - Unified error model (unchanged)
        - Integrity hooks (unchanged)
        - Health metadata (unchanged)
    """

    # ---------------------------------------------------------
    # METADATA (v4.5)
    # ---------------------------------------------------------
    name = "context-diff"
    description = "Shows differences between the current state and stored memory."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.2
    capabilities = ["context_read"]

    keywords = ["diff", "context", "compare", "memory", "state"]
    examples = ["context-diff", "context-diff mood"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context: ContextManager):
        self.context = context

    # ---------------------------------------------------------
    # EXECUTION (v4.5)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Compares context state with memory values.
        Deterministic, safe, and audit‑friendly.
        """

        # -----------------------------
        # VALIDATE CONTEXT
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        # -----------------------------
        # DIFF FOR SPECIFIC KEY
        # -----------------------------
        key = args[0] if args else None

        if key is not None:
            mem_value = self.context.recall(key)
            state_value = self.context.get_state(key)

            if mem_value is None and state_value is None:
                return {
                    "status": "not_found",
                    "key": key,
                    "message": f"No data exists for key '{key}'."
                }

            if mem_value == state_value:
                return {
                    "status": "equal",
                    "key": key,
                    "value": mem_value,
                    "message": f"No difference for '{key}'. Values are identical."
                }

            return {
                "status": "diff",
                "key": key,
                "memory": mem_value,
                "state": state_value,
                "message": f"Difference found for '{key}'."
            }

        # -----------------------------
        # DIFF FOR ENTIRE STATE
        # -----------------------------
        diff = self.context.diff(self.context.state)

        if not diff:
            return {
                "status": "equal",
                "message": "State and memory are fully consistent."
            }

        formatted = {
            k: {
                "current": info["current"],
                "memory": info["incoming"]
            }
            for k, info in diff.items()
        }

        return {
            "status": "diff",
            "message": "Differences found between state and memory.",
            "diff": formatted
        }
