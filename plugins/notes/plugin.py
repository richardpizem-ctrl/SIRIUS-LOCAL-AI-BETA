# plugin.py
# SIRIUS LOCAL AI – Notes Plugin 4.3.x
# Safe, deterministic, sandboxed note storage module

from __future__ import annotations

import datetime


class Plugin:
    """
    Notes Plugin 4.3.x

    Responsibilities:
        - Provide NL commands for note operations
        - Provide AI tasks for note operations
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Delegate ALL filesystem actions to SystemAgent 4.3
        - Deterministic, safe-mode aware, degraded-mode aware
        - Self‑Repair 4.4 ready
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.get_system_agent()

        self.safe_mode = False
        self.degraded_mode = False

        self.storage = "notes_storage"

        self.rm.logger.info("[PLUGIN:notes] Initialized (v4.3.x)")

    # --------------------------------------------------------
    # NL COMMANDS (4.3.x)
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

        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_list_notes(self, text):
        action = {
            "id": "notes_list",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": self.storage},
        }

        result = self.agent.execute_action("OWNER", action)
        return result.message

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

        result = self.agent.execute_action("OWNER", action)
        return result.message

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

        result = self.agent.execute_action("OWNER", action)
        return result.message

    # --------------------------------------------------------
    # AI TASKS (4.3.x)
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

        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

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

        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_list_notes(self, params):
        action = {
            "id": "notes_ai_list",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": self.storage},
        }

        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

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

        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    # --------------------------------------------------------
    # WORKFLOWS (4.3.x)
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
    # AI LOOP RULES (4.3.x)
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
    # GUI ELEMENTS (4.3.x)
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
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
