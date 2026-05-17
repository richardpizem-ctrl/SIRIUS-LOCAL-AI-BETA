# plugin.py
# SIRIUS LOCAL AI – System Tools Plugin 4.3.x
# Safe, deterministic, sandboxed system diagnostics module

from __future__ import annotations


class Plugin:
    """
    System Tools Plugin 4.3.x

    Responsibilities:
        - Provide NL commands for system diagnostics
        - Provide AI tasks for system diagnostics
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Delegate ALL system actions to SystemAgent 4.3
        - Deterministic, safe-mode aware, degraded-mode aware
        - Self‑Repair 4.4 ready
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.get_system_agent()

        self.safe_mode = False
        self.degraded_mode = False

        self.rm.logger.info("[PLUGIN:system_tools] Initialized (v4.3.x)")

    # --------------------------------------------------------
    # NL COMMANDS (4.3.x)
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
        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_cpu_info(self, text):
        action = {
            "id": "cpu_info",
            "type": "CPU_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_ram_info(self, text):
        action = {
            "id": "ram_info",
            "type": "RAM_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_disk_info(self, text):
        action = {
            "id": "disk_info",
            "type": "DISK_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        result = self.agent.execute_action("OWNER", action)
        return result.message

    # --------------------------------------------------------
    # AI TASKS (4.3.x)
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
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_cpu_usage(self, params):
        action = {
            "id": "ai_cpu_usage",
            "type": "CPU_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_ram_usage(self, params):
        action = {
            "id": "ai_ram_usage",
            "type": "RAM_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_disk_usage(self, params):
        action = {
            "id": "ai_disk_usage",
            "type": "DISK_USAGE",
            "identity_required": "OWNER",
            "payload": {},
        }
        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    # --------------------------------------------------------
    # WORKFLOWS (4.3.x)
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
    # AI LOOP RULES (4.3.x)
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
    # GUI ELEMENTS (4.3.x)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {"type": "button", "label": "System Info", "action": "system_info"},
            {"type": "button", "label": "CPU", "action": "cpu_usage"},
            {"type": "button", "label": "RAM", "action": "ram_usage"},
            {"type": "button", "label": "Disk", "action": "disk_usage"},
        ]

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
