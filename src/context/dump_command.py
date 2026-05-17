from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextDumpCommand(BaseCommand):
    """
    ContextDumpCommand 4.3
    Dumps the entire context: session memory, persistent memory, state,
    snapshot history, and last snapshot diagnostics.

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
    name = "context-dump"
    description = "Dumps all context data: session, persistent, state, history."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.2
    capabilities = ["context_read"]

    keywords = ["dump", "context", "memory", "state", "history"]
    examples = ["context-dump"]

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
        Dumps the entire context in a structured format.
        """

        # -----------------------------
        # VALIDATE CONTEXT
        # -----------------------------
        is_valid = (
            self.context.validate()
            if hasattr(self.context, "validate")
            else True
        )

        # -----------------------------
        # COLLECT DATA
        # -----------------------------
        session = list(self.context.session_memory)
        persistent = dict(self.context.persistent_memory)
        state = dict(self.context.state)
        history = list(self.context.history)

        # Last snapshot diagnostics
        if history:
            last = history[-1]
            last_snapshot_info = {
                "session_items": len(last.get("session", [])),
                "persistent_items": len(last.get("persistent", {})),
                "state_items": len(last.get("state", {})),
            }
        else:
            last_snapshot_info = None

        # -----------------------------
        # STRUCTURED OUTPUT
        # -----------------------------
        return {
            "status": "success",
            "context_valid": is_valid,
            "session": {
                "count": len(session),
                "items": session
            },
            "persistent": {
                "count": len(persistent),
                "items": persistent
            },
            "state": {
                "count": len(state),
                "items": state
            },
            "history": {
                "snapshots": len(history),
                "max_capacity": getattr(self.context, "max_history", None),
                "last_snapshot": last_snapshot_info
            }
        }
