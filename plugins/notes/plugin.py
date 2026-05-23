# plugin.py
# SIRIUS LOCAL AI – Notes Plugin 4.5.0
# Safe, deterministic, sandboxed note storage module with integrity + health support

from __future__ import annotations

import os
import datetime


class Plugin:
    """
    Notes Plugin 4.5.0

    Responsibilities:
        - Provide NL commands for note operations
        - Provide AI tasks for note operations
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Delegate ALL filesystem actions to SystemAgent 4.5
        - Deterministic, safe-mode aware, degraded-mode aware
        - Plugin Integrity Hooks (4.5)
        - Health Metadata (4.5)
        - Self‑Repair Layer 4.5 compatibility
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.get_system_agent()

        # Runtime 4.5 modes
        self.safe_mode = False
        self.degraded_mode = False

        # 4.5 integrity + health
        self.integrity_ok = True
        self.health_status = "OK"

        self.storage = "notes_storage"

        self.rm.logger.info("[PLUGIN:notes] Initialized (v4.5.0)")

    # --------------------------------------------------------
    # INTEGRITY HOOKS (4.5)
    # --------------------------------------------------------
    def integrity_check(self):
        try:
            return os.path.exists(__file__)
        except Exception:
            return False

    def integrity_repair(self):
        self.rm.logger.warn("[PLUGIN:notes] Integrity repair triggered.")
        self.integrity_ok = False
        self.degraded_mode = True
        return True

    # --------------------------------------------------------
    # HEALTH METADATA (4.5)
    # --------------------------------------------------------
    def health(self):
        return {
            "status": self.health_status,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "integrity_ok": self.integrity_ok,
        }

    # --------------------------------------------------------
    # NL COMMANDS (4.5)
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "write note": self._nl_write_note,
            "show notes": self._nl_list_notes,
            "read note": self._nl_read_note,
            "delete note": self._nl_delete_note,
        }

    def _nl_write_note(self, text):
        if self.safe_mode:
            return "SAFE MODE: Note writing disabled."

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"note_{timestamp}.txt"

        action = {
            "id": "notes_write",
            "type": "WRITE_FILE",
            "identity_required": "OWNER",
            "payload": {
                "folder": self.storage,
                "filename": filename,
                "content": text,
            },
        }
        return self._execute(action)

    def _nl_list_notes(self, text):
        action = {
            "id": "notes_list",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": self.storage},
        }
        return self._execute(action)

    def _nl_read_note(self, text):
        filename = text.strip()
        action = {
            "id": "notes_read",
            "type": "READ_FILE",
            "identity_required": "OWNER",
            "payload": {
                "folder": self.storage,
                "filename": filename,
            },
        }
        return self._execute(action)

    def _nl_delete_note(self, text):
        if self.safe_mode:
            return "SAFE MODE: Note deletion disabled."

        filename = text.strip()
        action = {
            "id": "notes_delete",
            "type": "DELETE_FILE",
            "identity_required": "OWNER",
            "payload": {
                "folder": self.storage,
                "filename": filename,
            },
        }
        return self._execute(action)

    # --------------------------------------------------------
    # AI TASKS (4.5)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "write_note": self._ai_write_note,
            "read_note": self._ai_read_note,
            "list_notes": self._ai_list_notes,
            "delete_note": self._ai_delete_note,
        }

    def _ai_write_note(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        text = params.get("text", "")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"note_{timestamp}.txt"

        action = {
            "id": "notes_ai_write",
            "type": "WRITE_FILE",
            "identity_required": "OWNER",
            "payload": {
                "folder": self.storage,
                "filename": filename,
                "content": text,
            },
        }
        return self._execute_ai(action)

    def _ai_read_note(self, params):
        filename = params.get("name")
        action = {
            "id": "notes_ai_read",
            "type": "READ_FILE",
            "identity_required": "OWNER",
            "payload": {
                "folder": self.storage,
                "filename": filename,
            },
        }
        return self._execute_ai(action)

    def _ai_list_notes(self, params):
        action = {
            "id": "notes_ai_list",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": self.storage},
        }
        return self._execute_ai(action)

    def _ai_delete_note(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        filename = params.get("name")
        action = {
            "id": "notes_ai_delete",
            "type": "DELETE_FILE",
            "identity_required": "OWNER",
            "payload": {
                "folder": self.storage,
                "filename": filename,
            },
        }
        return self._execute_ai(action)

    # --------------------------------------------------------
    # WORKFLOWS (4.5)
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "daily_note",
                "steps": [
                    {"action": "log", "message": "Writing daily note..."},
                    {
                        "action": "task",
                        "task": "write_note",
                        "params": {"text": "Daily entry."},
                    },
                    {"action": "return", "value": "Daily note saved."},
                ],
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES (4.5)
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "notes_heartbeat",
                "trigger": "interval",
                "interval": 300,
                "action": "list_notes",
                "params": {},
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS (4.5)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Show notes",
                "action": "list_notes",
            },
            {
                "type": "button",
                "label": "Write quick note",
                "action": "write_note",
                "params": {"text": "Quick note."},
            },
        ]

    # --------------------------------------------------------
    # INTERNAL EXECUTION HELPERS (4.5)
    # --------------------------------------------------------
    def _execute(self, action):
        try:
            result = self.agent.execute_action("OWNER", action)
            return result.message
        except Exception as e:
            self._handle_error(action["id"], e)
            return "Notes error."

    def _execute_ai(self, action):
        try:
            result = self.agent.execute_action("OWNER", action)
            return {"success": result.success, "message": result.message}
        except Exception as e:
            self._handle_error(action["id"], e)
            return {"error": "Notes error"}

    # --------------------------------------------------------
    # INTERNAL ERROR HANDLER (4.5)
    # --------------------------------------------------------
    def _handle_error(self, label, exception):
        self.degraded_mode = True
        self.health_status = "DEGRADED"
        self.rm.logger.error(f"[NOTES] {label} error: {exception}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL (4.5)
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.rm.logger.warn("[PLUGIN:notes] Entered SAFE MODE.")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.rm.logger.info("[PLUGIN:notes] Exited SAFE MODE.")
