# plugin.py
# SIRIUS LOCAL AI – File Manager Plugin 4.5.0
# Safe, deterministic, sandboxed filesystem module with integrity + health support

from __future__ import annotations

import os


class Plugin:
    """
    File Manager Plugin 4.5.0

    Responsibilities:
        - Provide NL commands for filesystem operations
        - Provide AI tasks for filesystem operations
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Delegate ALL filesystem actions to SystemAgent 4.5
        - Deterministic, safe-mode aware, degraded-mode aware
        - Plugin Integrity Hooks (4.5)
        - Health Metadata (4.5)
        - Support Self‑Repair Layer 4.5
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

        self.rm.logger.info("[PLUGIN:file_manager] Initialized (v4.5.0)")

    # --------------------------------------------------------
    # INTEGRITY HOOKS (4.5)
    # --------------------------------------------------------
    def integrity_check(self):
        """
        Called by PluginLoader 4.5.
        Must return True/False.
        """
        try:
            return os.path.exists(__file__)
        except Exception:
            return False

    def integrity_repair(self):
        """
        Called by Self‑Repair Layer 4.5.
        Plugin may reload, reset state, or fallback.
        """
        self.rm.logger.warn("[PLUGIN:file_manager] Integrity repair triggered.")
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
        return self._execute(action)

    def _nl_move_files(self, text):
        if self.safe_mode:
            return "SAFE MODE: Filesystem write disabled."

        try:
            src, dst = text.split("->")
        except Exception:
            return "Invalid format. Use: source -> destination"

        action = {
            "id": "fm_move_files",
            "type": "MOVE_FILES",
            "identity_required": "OWNER",
            "payload": {"src": src.strip(), "dst": dst.strip()},
        }
        return self._execute(action)

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
        return self._execute(action)

    def _nl_list_directory(self, text):
        path = text.strip()
        action = {
            "id": "fm_list_directory",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": path},
        }
        return self._execute(action)

    # --------------------------------------------------------
    # AI TASKS (4.5)
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
        return self._execute_ai(action)

    def _ai_move_files(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        action = {
            "id": "fm_ai_move_files",
            "type": "MOVE_FILES",
            "identity_required": "OWNER",
            "payload": {"src": params.get("src"), "dst": params.get("dst")},
        }
        return self._execute_ai(action)

    def _ai_delete_file(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        action = {
            "id": "fm_ai_delete_file",
            "type": "DELETE_FILE",
            "identity_required": "OWNER",
            "payload": {"path": params.get("path")},
        }
        return self._execute_ai(action)

    def _ai_list_directory(self, params):
        action = {
            "id": "fm_ai_list_directory",
            "type": "LIST_DIRECTORY",
            "identity_required": "OWNER",
            "payload": {"path": params.get("path")},
        }
        return self._execute_ai(action)

    # --------------------------------------------------------
    # WORKFLOWS (4.5)
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
    # AI LOOP RULES (4.5)
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
    # GUI ELEMENTS (4.5)
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
    # INTERNAL EXECUTION HELPERS (4.5)
    # --------------------------------------------------------
    def _execute(self, action):
        try:
            result = self.agent.execute_action("OWNER", action)
            return result.message
        except Exception as e:
            self._handle_error(action["id"], e)
            return "Filesystem error."

    def _execute_ai(self, action):
        try:
            result = self.agent.execute_action("OWNER", action)
            return {"success": result.success, "message": result.message}
        except Exception as e:
            self._handle_error(action["id"], e)
            return {"error": "Filesystem error"}

    # --------------------------------------------------------
    # INTERNAL ERROR HANDLER (4.5)
    # --------------------------------------------------------
    def _handle_error(self, label, exception):
        self.degraded_mode = True
        self.health_status = "DEGRADED"
        self.rm.logger.error(f"[FILE_MANAGER] {label} error: {exception}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL (4.5)
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.rm.logger.warn("[PLUGIN:file_manager] Entered SAFE MODE.")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.rm.logger.info("[PLUGIN:file_manager] Exited SAFE MODE.")
