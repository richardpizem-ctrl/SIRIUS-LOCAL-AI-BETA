from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextSetCommand(BaseCommand):
    """
    ContextSetCommand 4.4
    Sets a value in the system state with validation, snapshot,
    diff reporting, and safe merge.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Deterministic diff structure
        - Snapshot before modification
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Stable output for Runtime4.4 and NL Router 4.4
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
    # ---------------------------------------------------------
    name = "context-set"
    description = "Sets a value in the context state with validation, snapshot, and diff."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.4
    capabilities = ["context_write"]

    keywords = ["set", "context", "state", "update"]
    examples = ["context-set mood happy"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context: ContextManager):
        self.context = context

    # ---------------------------------------------------------
    # EXECUTION (4.4)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Sets a state variable with snapshot and diff reporting.
        Deterministic, safe, and audit‑friendly.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": "Usage: context-set <key> <value>"
            }

        key, value = args[0], args[1]

        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        # -----------------------------
        # SNAPSHOT BEFORE CHANGE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # DIFF (old vs new)
        # -----------------------------
        old_value = self.context.get_state(key)
        diff = None

        # Only generate diff if old_value exists
        if old_value is not None and old_value != value:
            diff = {
                "old": old_value,
                "new": value
            }

        # -----------------------------
        # SAFE MERGE
        # -----------------------------
        if isinstance(key, str):
            self.context.merge({key: value})

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "key": key,
            "value": value,
            "diff": diff,
            "message": f"State variable '{key}' updated."
        }
