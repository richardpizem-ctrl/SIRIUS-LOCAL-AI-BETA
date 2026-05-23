from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextInfoCommand(BaseCommand):
    """
    ContextInfoCommand 4.5
    Displays diagnostic information about the AI context:
        - short‑term memory (session)
        - long‑term memory (persistent)
        - system state
        - snapshot history
        - consistency validation

    Updated in 4.5:
        - Self‑Repair Layer 4.5 compatibility
        - Deterministic introspection structure (unchanged)
        - Stable output for Runtime4.5, GUI, and NL Router 4.5
        - Unified error model (unchanged)
        - Integrity hooks (unchanged)
        - Health metadata (unchanged)
    """

    # ---------------------------------------------------------
    # METADATA (v4.5)
    # ---------------------------------------------------------
    name = "context-info"
    description = "Displays extended diagnostic information about the AI context."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.2
    capabilities = ["context_read"]

    keywords = ["info", "context", "diagnostics", "memory", "state"]
    examples = ["context-info"]

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
        Returns structured diagnostic information about the context.
        Deterministic, safe, and audit‑friendly.
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
        session_items = (
            list(self.context.get_recent(10))
            if getattr(self.context, "session_memory", None)
            else []
        )

        persistent_items = dict(self.context.persistent_memory)
        state_items = dict(self.context.state)

        history_count = len(self.context.history)
        max_capacity = getattr(self.context, "max_history", None)

        if history_count > 0:
            last = self.context.history[-1]
            last_snapshot = {
                "session_items": len(last.get("session", [])),
                "persistent_items": len(last.get("persistent", {})),
                "state_items": len(last.get("state", {}))
            }
        else:
            last_snapshot = None

        # -----------------------------
        # STRUCTURED OUTPUT
        # -----------------------------
        return {
            "status": "success",
            "context_valid": is_valid,
            "session_memory": {
                "count": len(session_items),
                "recent_items": session_items
            },
            "persistent_memory": {
                "count": len(persistent_items),
                "items": persistent_items
            },
            "state": {
                "count": len(state_items),
                "items": state_items
            },
            "history": {
                "snapshots": history_count,
                "max_capacity": max_capacity,
                "last_snapshot": last_snapshot
            }
        }
