# plugin.py
# SIRIUS LOCAL AI – System Tools Plugin 4.4.0
# Safe, deterministic, sandboxed system diagnostics module with integrity + health support

from __future__ import annotations

import os


class Plugin:
    """
    System Tools Plugin 4.4.0

    Responsibilities:
        - Provide NL commands for system diagnostics
        - Provide AI tasks for system diagnostics
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Delegate ALL system actions to SystemAgent 4.4
        - Deterministic, safe-mode aware, degraded-mode aware
        - Plugin Integrity Hooks (4.4)
        - Health Metadata (4.4)
        - Self‑Repair Layer 4.4 compatibility
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.get_system_agent()

        # Runtime 4.4 modes
        self.safe_mode = False
        self.degraded_mode = False

        # 4.4 integrity + health
        self.integrity_ok = True
        self.health_status = "OK"

        self.rm.logger.info("[PLUGIN:system_tools] Initialized (v4.4.0)")

    # --------------------------------------------------------
    # INTEGRITY HOOKS (4.4)
    # --------------------------------------------------------
    def integrity_check(self):
        try:
            return os.path.exists(__file__)
        except Exception:
            return False

    def integrity_repair(self):
        self.rm.logger.warn("[PLUGIN:system_tools] Integrity repair triggered.")
        self.integrity_ok = False
        self.degraded_mode = True
        return True

    # --------------------------------------------------------
    # HEALTH METADATA (4.4)
    # --------------------------------------------------------
    def health(self):
        return {
            "status": self.health_status,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "integrity_ok": self.integrity_ok,
        }

    # --------------------------------------------------------
    # NL COMMANDS (4.4)
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "system info": self._nl_system_info,
            "cpu info": self._nl_cpu_info,
            "ram info": self._nl_ram_info,
            "disk info": self._nl_disk_info,
        }

    def _nl_system_info(self, text):
        action = {
            "id": "sys_info",
            "type": "SYSTEM_INFO",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute(action)

    def _nl_cpu_info(self, text):
        action = {
            "id": "cpu_info",
            "type": "CPU_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute(action)

    def _nl_ram_info(self, text):
        action = {
            "id": "ram_info",
            "type": "RAM_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute(action)

    def _nl_disk_info(self, text):
        action = {
            "id": "disk_info",
            "type": "DISK_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute(action)

    # --------------------------------------------------------
    # AI TASKS (4.4)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "system_info": self._ai_system_info,
            "cpu_usage": self._ai_cpu_usage,
            "ram_usage": self._ai_ram_usage,
            "disk_usage": self._ai_disk_usage,
        }

    def _ai_system_info(self, params):
        action = {
            "id": "ai_sys_info",
            "type": "SYSTEM_INFO",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute_ai(action)

    def _ai_cpu_usage(self, params):
        action = {
            "id": "ai_cpu_usage",
            "type": "CPU_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute_ai(action)

    def _ai_ram_usage(self, params):
        action = {
            "id": "ai_ram_usage",
            "type": "RAM_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute_ai(action)

    def _ai_disk_usage(self, params):
        action = {
            "id": "ai_disk_usage",
            "type": "DISK_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        return self._execute_ai(action)

    # --------------------------------------------------------
    # WORKFLOWS (4.4)
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "system_diagnostics",
                "steps": [
                    {"action": "log", "message": "Running system diagnostics..."},
                    {"action": "task", "task": "system_info"},
                    {"action": "return", "value": "Diagnostics completed."},
                ],
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES (4.4)
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "system_heartbeat",
                "trigger": "interval",
                "interval": 180,
                "action": "system_info",
                "params": {},
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS (4.4)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {"type": "button", "label": "System Info", "action": "system_info"},
            {"type": "button", "label": "CPU", "action": "cpu_usage"},
            {"type": "button", "label": "RAM", "action": "ram_usage"},
            {"type": "button", "label": "Disk", "action": "disk_usage"},
        ]

    # --------------------------------------------------------
    # INTERNAL EXECUTION HELPERS (4.4)
    # --------------------------------------------------------
    def _execute(self, action):
        try:
            result = self.agent.execute_action("OWNER", action)
            return result.message
        except Exception as e:
            self._handle_error(action["id"], e)
            return "System diagnostics error."

    def _execute_ai(self, action):
        try:
            result = self.agent.execute_action("OWNER", action)
            return {"success": result.success, "message": result.message}
        except Exception as e:
            self._handle_error(action["id"], e)
            return {"error": "System diagnostics error"}

    # --------------------------------------------------------
    # INTERNAL ERROR HANDLER (4.4)
    # --------------------------------------------------------
    def _handle_error(self, label, exception):
        self.degraded_mode = True
        self.health_status = "DEGRADED"
        self.rm.logger.error(f"[SYSTEM_TOOLS] {label} error: {exception}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL (4.4)
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.rm.logger.warn("[PLUGIN:system_tools] Entered SAFE MODE.")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.rm.logger.info("[PLUGIN:system_tools] Exited SAFE MODE.")
