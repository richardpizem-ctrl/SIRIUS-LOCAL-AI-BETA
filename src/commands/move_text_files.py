"""
MoveTextFilesCommand 4.5
High-level filesystem automation command for moving all .txt files
from a source folder into a target folder using FS-Agent.

Updated in 4.5:
- Self‑Repair Layer 4.5 compatibility
- Deterministic execution contract (unchanged)
- Integrity Hooks (unchanged)
- Health Metadata (unchanged)
- Extended audit (unchanged)
- Safe execution via BaseCommand.run()
- WorkflowLogger 4.5 integration
"""

from typing import List
from commands.base_command import BaseCommand
from ui.confirm import ConfirmDialog
from filesystem.fs_agent import FSAgent
from workflow.logger import WorkflowLogger


class MoveTextFilesCommand(BaseCommand):
    """
    High-level command for moving all .txt files from a source folder
    into a newly created or existing target folder.
    """

    # ---------------------------------------------------------
    # METADATA (v4.5)
    # ---------------------------------------------------------
    name = "move_text_files"
    description = "Moves all .txt files from source to target folder."
    category = "filesystem"

    required_identity = "OWNER"       # FAMILY cannot move files
    risk_level = 0.4                  # medium risk (file operations)
    capabilities = ["fs_write", "fs_move"]

    keywords = ["move", "text files", "txt", "folder", "transfer"]
    examples = ["move_text_files <source> <target>"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, source_path: str, target_path: str):
        self.source_path = source_path
        self.target_path = target_path
        self.logger = WorkflowLogger()

    # ---------------------------------------------------------
    # VALIDATION (4.5)
    # ---------------------------------------------------------
    def validate(self) -> bool:
        """
        Validate input paths before execution.
        Deterministic and audit-friendly.
        """
        if not FSAgent.path_exists(self.source_path):
            self.logger.error(f"validate_path – source not found: {self.source_path}")
            return False

        return True

    # ---------------------------------------------------------
    # EXECUTION (4.5)
    # ---------------------------------------------------------
    def execute(self) -> dict:
        """
        Main execution logic:
        1. Create target folder if missing.
        2. Find .txt files in source.
        3. Ask for confirmation.
        4. Move files using FS-Agent.
        """

        self.logger.info("MoveTextFilesCommand – start")

        # -----------------------------
        # VALIDATE INPUT
        # -----------------------------
        if not self.validate():
            return {"status": "error", "message": "Source folder does not exist."}

        self.logger.info(f"Source: {self.source_path}")
        self.logger.info(f"Target: {self.target_path}")

        # -----------------------------
        # SNAPSHOT BEFORE MUTATION
        # -----------------------------
        if hasattr(self, "context") and hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # ENSURE TARGET FOLDER EXISTS
        # -----------------------------
        FSAgent.ensure_folder(self.target_path)
        self.logger.info(f"ensure_folder – {self.target_path}")

        # -----------------------------
        # FIND .TXT FILES
        # -----------------------------
        txt_files: List[str] = FSAgent.list_files(self.source_path, extension=".txt")

        if not txt_files:
            self.logger.info("no .txt files found – abort")
            return {"status": "no_files", "message": "No .txt files found."}

        # -----------------------------
        # CONFIRMATION DIALOG
        # -----------------------------
        confirm = ConfirmDialog(
            title="Move Text Files",
            message=(
                f"Move {len(txt_files)} text files?\n\n"
                f"From: {self.source_path}\n"
                f"To:   {self.target_path}"
            )
        )

        if not confirm.get_user_confirmation():
            self.logger.info("user cancelled")
            return {"status": "cancelled", "message": "Operation cancelled by user."}

        # -----------------------------
        # MOVE FILES
        # -----------------------------
        try:
            success = FSAgent.move_files(txt_files, self.target_path)
        except Exception as e:
            self.logger.error(f"move_files – exception: {e}")
            return {"status": "error", "exception": str(e)}

        if success:
            self.logger.info(f"move_files – {len(txt_files)} items moved")
            self.logger.info("completed")
            return {
                "status": "success",
                "moved": len(txt_files),
                "source": self.source_path,
                "target": self.target_path
            }

        else:
            self.logger.error("move_files – operation failed")
            return {"status": "failed", "message": "Move operation failed."}
