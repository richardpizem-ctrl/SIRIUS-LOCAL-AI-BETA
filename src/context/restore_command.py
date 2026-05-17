from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
import copy


class RestoreCommand(BaseCommand):
    """
    RestoreCommand 4.3
    Restores the entire context from a backup JSON file created by context-backup.

    Improvements in 4.3:
    - unified metadata contract
    - deterministic behavior for Runtime4
    - strict backup validation
    - deep-copy restoration
    - snapshot after restore
    - consistent return structure
    - Self‑Repair 4.4 compatible
    """

    # ---------------------------------------------------------
    # METADATA (v4.3)
    # ---------------------------------------------------------
    name = "context-restore"
    description = "Restores the entire context from a backup JSON file."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.9
    capabilities = ["context_write", "fs_read"]

    keywords = ["restore", "backup", "context", "load"]
    examples = ["context-restore backup_2026-04-24_11-25-55.json"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context: ContextManager, backup_dir="backups"):
        self.context = context
        self.backup_dir = backup_dir

    # ---------------------------------------------------------
    # EXECUTION (v4.3)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Restores the entire context from a backup JSON file.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        filename = args[0] if args else None

        if filename is None:
            return {
                "status": "error",
                "message": (
                    "Usage:\n"
                    "  context-restore <filename>\n\n"
                    "Example:\n"
                    "  context-restore backup_2026-04-24_11-25-55.json"
                )
            }

        filepath = filename

        # If only filename is given, try backups/ directory
        if not os.path.isfile(filepath):
            candidate = os.path.join(self.backup_dir, filename)
            if os.path.isfile(candidate):
                filepath = candidate
            else:
                return {
                    "status": "error",
                    "message": (
                        f"File '{filename}' does not exist in current directory "
                        f"or '{self.backup_dir}/'."
                    )
                }

        # -----------------------------
        # LOAD JSON
        # -----------------------------
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            return {
                "status": "error",
                "message": "Failed to load backup file.",
                "exception": str(e)
            }

        # -----------------------------
        # VALIDATE BACKUP STRUCTURE
        # -----------------------------
        required_keys = ["session", "persistent", "state", "history"]

        if not isinstance(data, dict) or not all(k in data for k in required_keys):
            return {
                "status": "error",
                "message": (
                    "Backup file has invalid structure. Required keys: "
                    "session, persistent, state, history."
                )
            }

        if not isinstance(data["session"], list):
            return {"status": "error", "message": "Backup 'session' must be a list."}
        if not isinstance(data["persistent"], dict):
            return {"status": "error", "message": "Backup 'persistent' must be an object."}
        if not isinstance(data["state"], dict):
            return {"status": "error", "message": "Backup 'state' must be an object."}
        if not isinstance(data["history"], list):
            return {"status": "error", "message": "Backup 'history' must be a list of snapshots."}

        # -----------------------------
        # RESTORE CONTEXT (deep copy)
        # -----------------------------
        self.context.session_memory = copy.deepcopy(data["session"])
        self.context.persistent_memory = copy.deepcopy(data["persistent"])
        self.context.state = copy.deepcopy(data["state"])

        # Enforce max_history
        self.context.history = copy.deepcopy(
            data["history"][-self.context.max_history:]
        )

        # -----------------------------
        # SNAPSHOT AFTER RESTORE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # VALIDATE AFTER RESTORE
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "warning",
                "message": "Context restored, but validation failed."
            }

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "file": filepath,
            "message": f"Context restored successfully from '{filepath}'."
        }
