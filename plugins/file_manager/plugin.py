# plugin.py
# SIRIUS LOCAL AI – File Manager Plugin 4.3.x
# Safe, deterministic, sandboxed filesystem module

from __future__ import annotations


class Plugin:
    """
    File Manager Plugin 4.3.x

    Responsibilities:
        - Provide NL commands for filesystem operations
        - Provide AI tasks for filesystem operations
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

        self.rm.logger.info("[PLUGIN:file_manager] Initialized (v4.3.x)")

    # --------------------------------------------------------
    # NL COMMANDS (4.3.x)
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "create folder": self._nl_create_folder,
            "move files": self._nl_move_files,
            "delete file": self._nl_delete_file,
            "list directory": self._nl_list_directory,
        }

    def _nl_create_folder(self, text):
        if self.safe_mode:
            return "SAFE MODE: Filesystem write disabled."

        path = text.strip()
        action = {
            "id": "fm_create_folder",
            "type": "CREATE_FOLDER",
            "identity_required": "OWNER",
            "payload": {"path": path},
        }
        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_move_files(self, text):
        if self.safe_mode:
            return "SAFE MODE: Filesystem write disabled."

        try:
            src, dst = text.split("->")
        except:
            return "Invalid format. Use: source -> destination"

        action = {
            "id": "fm_move_files",
            "type": "MOVE_FILES",
            "identity_required": "OWNER",
            "payload": {"src": src.strip(), "dst": dst.strip()},
        }
        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_delete_file(self, text):
        if self.safe_mode:
            return "SAFE MODE: Filesystem write disabled."

        path = text.strip()
        action = {
            "id": "fm_delete_file",
            "type": "DELETE_FILE",
            "identity_required": "OWNER",
            "payload": {"path": path},
        }
        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_list_directory(self, text):
        path = text.strip()
        action = {
            "id": "fm_list_directory",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": path},
        }
        result = self.agent.execute_action("OWNER", action)
        return result.message

    # --------------------------------------------------------
    # AI TASKS (4.3.x)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "create_folder": self._ai_create_folder,
            "move_files": self._ai_move_files,
            "delete_file": self._ai_delete_file,
            "list_directory": self._ai_list_directory,
        }

    def _ai_create_folder(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        action = {
            "id": "fm_ai_create_folder",
            "type": "CREATE_FOLDER",
            "identity_required": "OWNER",
            "payload": {"path": params.get("path")},
        }
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_move_files(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        action = {
            "id": "fm_ai_move_files",
            "type": "MOVE_FILES",
            "identity_required": "OWNER",
            "payload": {"src": params.get("src"), "dst": params.get("dst")},
        }
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_delete_file(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        action = {
            "id": "fm_ai_delete_file",
            "type": "DELETE_FILE",
            "identity_required": "OWNER",
            "payload": {"path": params.get("path")},
        }
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_list_directory(self, params):
        action = {
            "id": "fm_ai_list_directory",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": params.get("path")},
        }
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    # --------------------------------------------------------
    # WORKFLOWS (4.3.x)
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "auto_clean_downloads",
                "steps": [
                    {"action": "log", "message": "Cleaning Downloads folder..."},
                    {
                        "action": "task",
                        "task": "list_directory",
                        "params": {"path": "Downloads"},
                    },
                    {"action": "return", "value": "Done."},
                ],
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES (4.3.x)
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "monitor_downloads",
                "trigger": "interval",
                "interval": 60,
                "action": "list_directory",
                "params": {"path": "Downloads"},
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS (4.3.x)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Create folder",
                "action": "create_folder",
            },
            {
                "type": "button",
                "label": "Move files",
                "action": "move_files",
            },
        ]

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
