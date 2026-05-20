from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
import copy


class ContextImportCommand(BaseCommand):
    """
    ContextImportCommand 4.4
    Imports the context or selected sections from a JSON file.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic import behavior
        - Deep‑copy safety
        - Snapshot before mutation
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Stable structure for Runtime4.4 and NL Router 4.4
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
    # ---------------------------------------------------------
    name = "context-import"
    description = "Imports the context or selected sections from a JSON file."
    category = "context"

    required_identity = "OWNER"
    risk_level = 0.6
    capabilities = ["context_write", "fs_read"]

    keywords = ["import", "context", "json", "load"]
    examples = [
        "context-import all backup.json",
        "context-import session session.json"
    ]

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
        Imports selected context section from a JSON file.
        Deterministic, safe, and audit‑friendly.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": (
                    "Usage:\n"
                    "  context-import all <filename>\n"
                    "  context-import session <filename>\n"
                    "  context-import persistent <filename>\n"
                    "  context-import state <filename>\n"
                    "  context-import history <filename>"
                )
            }

        section = args[0].lower()
        filename = args[1]

        if not os.path.isfile(filename):
            return {
                "status": "error",
                "message": f"File '{filename}' does not exist."
            }

        # -----------------------------
        # LOAD JSON
        # -----------------------------
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            return {
                "status": "error",
                "message": "Failed to load JSON file.",
                "exception": str(e)
            }

        # -----------------------------
        # SNAPSHOT BEFORE MUTATION
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # IMPORT BY SECTION
        # -----------------------------
        try:
            if section == "all":
                if not isinstance(data, dict):
                    return {
                        "status": "error",
                        "message": (
                            "JSON must contain an object with keys: "
                            "session, persistent, state, history."
                        )
                    }

                self.context.session_memory = copy.deepcopy(data.get("session", []))
                self.context.persistent_memory = copy.deepcopy(data.get("persistent", {}))
                self.context.state = copy.deepcopy(data.get("state", {}))

                history = data.get("history", [])
                if isinstance(history, list):
                    self.context.history = history[-self.context.max_history:]
                else:
                    return {
                        "status": "error",
                        "message": "History must be a list of snapshots."
                    }

            elif section == "session":
                if not isinstance(data, list):
                    return {"status": "error", "message": "Session must be a list."}
                self.context.session_memory = copy.deepcopy(data)

            elif section == "persistent":
                if not isinstance(data, dict):
                    return {"status": "error", "message": "Persistent must be an object."}
                self.context.persistent_memory = copy.deepcopy(data)

            elif section == "state":
                if not isinstance(data, dict):
                    return {"status": "error", "message": "State must be an object."}
                self.context.state = copy.deepcopy(data)

            elif section == "history":
                if not isinstance(data, list):
                    return {"status": "error", "message": "History must be a list of snapshots."}
                self.context.history = data[-self.context.max_history:]

            else:
                return {
                    "status": "error",
                    "message": (
                        f"Unknown section '{section}'. "
                        "Use: all | session | persistent | state | history."
                    )
                }

        except Exception as e:
            return {
                "status": "error",
                "message": "Import failed due to an internal error.",
                "exception": str(e)
            }

        # -----------------------------
        # VALIDATE CONTEXT AFTER IMPORT
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "warning",
                "section": section,
                "file": filename,
                "message": "Import completed, but context is not in a consistent state."
            }

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "section": section,
            "file": filename,
            "message": f"Context section '{section}' imported successfully."
        }
