from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextClearCommand(BaseCommand):
    """
    ContextClearCommand 4.3
    Clears the short‑term (session) memory with validation, snapshot creation,
    and state logging.

    Improvements in 4.3:
    - unified metadata contract
    - deterministic behavior for Runtime4
    - safe error handling (via BaseCommand.run)
    - consistent return structure
    - Self‑Repair 4.4 compatible
    """

    # ---------------------------------------------------------
    # METADATA (v4.3)
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
    # EXECUTION (v4.3)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Clears the session memory with validation, snapshot, and state logging.
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
