from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextHistoryCommand(BaseCommand):
    """
    ContextHistoryCommand 4.4
    Displays the snapshot history of the context with optional limit.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic ordering
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Safe execution via BaseCommand.run()
        - Stable output for Runtime4.4 and NL Router 4.4
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
    # ---------------------------------------------------------
    name = "context-history"
    description = "Displays the snapshot history of the context."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.2
    capabilities = ["context_read"]

    keywords = ["history", "context", "snapshots", "memory"]
    examples = ["context-history", "context-history 5"]

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
        Displays snapshot history with optional limit.
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
        # HISTORY SIZE
        # -----------------------------
        total = len(self.context.history)

        if total == 0:
            return {
                "status": "empty",
                "message": "Snapshot history is empty."
            }

        # -----------------------------
        # LIMIT (optional)
        # -----------------------------
        limit = args[0] if args else None

        if limit is not None:
            try:
                limit = int(limit)
                if limit <= 0:
                    return {
                        "status": "error",
                        "message": "Limit must be greater than 0."
                    }
            except ValueError:
                return {
                    "status": "error",
                    "message": "Limit must be a number."
                }
        else:
            limit = total

        limit = min(limit, total)

        # -----------------------------
        # SELECT SNAPSHOTS
        # -----------------------------
        start_index = total - limit
        snapshots = self.context.history[start_index:]

        formatted = []
        for snap in snapshots:
            formatted.append({
                "session_items": len(snap.get("session", [])),
                "persistent_items": len(snap.get("persistent", {})),
                "state_items": len(snap.get("state", {}))
            })

        # -----------------------------
        # STRUCTURED OUTPUT
        # -----------------------------
        return {
            "status": "success",
            "total_snapshots": total,
            "showing_last": limit,
            "snapshots": formatted
        }
