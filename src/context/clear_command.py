from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextClearCommand(BaseCommand):
    """
    ContextClearCommand 4.5
    Clears the short‑term (session) memory with validation, snapshot creation,
    and state logging.

    Updated in 4.5:
        - Self‑Repair Layer 4.5 compatibility
        - Deterministic execution contract (unchanged)
        - Stable structure for Runtime4.5
        - Unified audit model (unchanged)
        - Integrity hooks (unchanged)
        - Health metadata (unchanged)
    """

    # ---------------------------------------------------------
    # METADATA (v4.5)
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
    # EXECUTION (v4.5)
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
