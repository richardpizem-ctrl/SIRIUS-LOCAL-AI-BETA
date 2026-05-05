from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
from datetime import datetime


class ContextBackupCommand(BaseCommand):
    """
    ContextBackupCommand 4.0
    Creates a timestamped backup of the entire context into the backups/ folder.

    New in version 4.0:
    - metadata for NL Router 4.0
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (filesystem write)
    - audit trail via BaseCommand lifecycle
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-backup"
    description = "Creates a timestamped backup of the entire context into the backups/ folder."
    category = "context"

    required_identity = "OWNER"     # only OWNER may create backups
    risk_level = 0.3                # moderate risk (file operations)
    capabilities = ["fs_write"]

    keywords = ["backup", "context", "save", "export"]
    examples = ["context-backup", "context-backup my_backup.json"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context: ContextManager, backup_dir="backups"):
        self.context = context
        self.backup_dir = backup_dir

    # ---------------------------------------------------------
    # EXECUTION (v4.0)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Creates a timestamped context backup.
        """
        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate"):
            if not self.context.validate():
                return {
                    "status": "invalid",
                    "message": "Context is not in a consistent state. Backup cancelled."
                }

        # -----------------------------
        # GENERATE FILENAME
        # -----------------------------
        filename = args[0] if args else None

        if filename is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"backup_{timestamp}.json"

        # -----------------------------
        # ENSURE DIRECTORY EXISTS
        # -----------------------------
        os.makedirs(self.backup_dir, exist_ok=True)
        filepath = os.path.join(self.backup_dir, filename)

        # -----------------------------
        # PREPARE DATA FOR BACKUP
        # -----------------------------
        data = {
            "timestamp": datetime.now().isoformat(),
            "session": self.context.session_memory,
            "persistent": self.context.persistent_memory,
            "state": self.context.state,
            "history": self.context.history,
        }

        # -----------------------------
        # WRITE FILE
        # -----------------------------
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            return {
                "status": "error",
                "message": "Error while creating backup.",
                "exception": str(e)
            }

        return {
            "status": "success",
            "file": filepath,
            "message": "Backup created successfully."
        }
