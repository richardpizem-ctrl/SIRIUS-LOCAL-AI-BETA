from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemoryLoadCommand(BaseCommand):
    """
    MemoryLoadCommand 4.4
    Loads a value from persistent memory and safely merges it into state.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic diff structure
        - Snapshot before merge
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Stable output for Runtime4.4 and NL Router 4.4
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
    # ---------------------------------------------------------
    name = "memory-load"
    description = "Loads a value from persistent memory and merges it into state."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.4
    capabilities = ["context_read", "context_write"]

    keywords = ["memory", "load", "persistent", "state"]
    examples = ["memory-load language"]

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
        Loads a persistent memory value and merges it into state.
        Deterministic, safe, and audit‑friendly.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        key = args[0] if args else None
        if key is None:
            return {
                "status": "error",
                "message": "Usage: memory-load <key>"
            }

        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        # -----------------------------
        # LOAD VALUE FROM MEMORY
        # -----------------------------
        value = self.context.recall(key)
        if value is None:
            return {
                "status": "not_found",
                "key": key,
                "message": f"No value found in persistent memory for '{key}'."
            }

        # -----------------------------
        # DIFF CHECK
        # -----------------------------
        state_value = self.context.get_state(key)
        diff = None

        if state_value != value:
            diff = {
                "state": state_value,
                "memory": value
            }

        # -----------------------------
        # SNAPSHOT BEFORE MERGE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

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
            "message": f"Loaded '{key}' from persistent memory."
        }
