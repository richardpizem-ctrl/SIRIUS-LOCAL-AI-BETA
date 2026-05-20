from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextClearCommand(BaseCommand):
    """
    ContextClearCommand 4.4
    Clears the short‑term (session) memory with validation, snapshot creation,
    and state logging.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic execution contract
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Safe execution via BaseCommand.run()
        - Stable structure for Runtime4.4
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
    # ---------------------------------------------------------
    name = "context-clear"
    description = "Clears the short‑term session memory with validation and snapshot."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.4
    capabilities = ["context_write"]

    keywords = ["clear", "context", "session", "memory"]
    examples = ["context-clear"]

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
        Clears the session memory with validation, snapshot, and state logging.
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
        # SNAPSHOT BEFORE CLEARING
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # CLEAR SESSION MEMORY
        # -----------------------------
        count = len(self.context.session_memory)
        self.context.session_memory.clear()

        # -----------------------------
        # LOG STATE
        # -----------------------------
        self.context.set_state("last_clear_count", str(count))
        self.context.set_state("last_clear_action", "session_memory")

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "cleared_items": count,
            "message": f"Session memory cleared. Removed items: {count}"
        }
