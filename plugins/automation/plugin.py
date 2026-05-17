# plugin.py
# SIRIUS LOCAL AI – Automation Plugin 4.3.x
# Safe, deterministic, sandboxed automation module

from __future__ import annotations

import os
import sys
from dataclasses import dataclass


class Plugin:
    """
    Automation Plugin 4.3.x

    Responsibilities:
        - Provide NL commands for automation
        - Provide AI tasks for automation
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Delegate ALL system actions to SystemAgent 4.3
        - Deterministic, safe-mode aware, degraded-mode aware
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.get_system_agent()

        self.safe_mode = False
        self.degraded_mode = False

        self.rm.logger.info("[PLUGIN:automation] Initialized (v4.3.x)")

    # --------------------------------------------------------
    # NL COMMANDS (4.3.x)
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "run command": self._nl_run_command,
            "run script": self._nl_run_script,
        }

    def _nl_run_command(self, text):
        if self.safe_mode:
            return "SAFE MODE: Command execution disabled."

        cmd = text.strip()
        if not cmd:
            return "Missing command."

        action = {
            "id": "automation_run_command",
            "type": "KILL_PROCESS",   # placeholder type, replaced below
            "label": "Run Shell Command",
            "description": "Execute shell command via SystemAgent",
            "identity_required": "OWNER",
            "payload": {"cmd": cmd},
        }

        # In 4.3.x, shell commands use a dedicated action type:
        action["type"] = "RUN_SHELL_COMMAND"

        result = self.agent.execute_action("OWNER", action)
        return result.message

    def _nl_run_script(self, text):
        if self.safe_mode:
            return "SAFE MODE: Script execution disabled."

        script = text.strip()
        if not os.path.exists(script):
            return "Script not found."

        action = {
            "id": "automation_run_script",
            "type": "RUN_SCRIPT",
            "label": "Run Python Script",
            "description": "Execute Python script via SystemAgent",
            "identity_required": "OWNER",
            "payload": {"script": script},
        }

        result = self.agent.execute_action("OWNER", action)
        return result.message

    # --------------------------------------------------------
    # AI TASKS (4.3.x)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "run_command": self._ai_run_command,
            "run_script": self._ai_run_script,
        }

    def _ai_run_command(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        cmd = params.get("cmd")
        if not cmd:
            return {"error": "Missing 'cmd' parameter."}

        action = {
            "id": "automation_ai_run_command",
            "type": "RUN_SHELL_COMMAND",
            "label": "Run Shell Command",
            "description": "Execute shell command via SystemAgent",
            "identity_required": "OWNER",
            "payload": {"cmd": cmd},
        }

        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    def _ai_run_script(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        script = params.get("script")
        if not script or not os.path.exists(script):
            return {"error": "Script not found."}

        action = {
            "id": "automation_ai_run_script",
            "type": "RUN_SCRIPT",
            "label": "Run Python Script",
            "description": "Execute Python script via SystemAgent",
            "identity_required": "OWNER",
            "payload": {"script": script},
        }

        result = self.agent.execute_action("OWNER", action)
        return {"success": result.success, "message": result.message}

    # --------------------------------------------------------
    # WORKFLOWS (4.3.x)
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "automation_cleanup",
                "steps": [
                    {"action": "log", "message": "Automation cleanup started..."},
                    {
                        "action": "task",
                        "task": "run_command",
                        "params": {"cmd": "echo Cleanup OK"},
                    },
                    {"action": "return", "value": "Automation completed."},
                ],
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES (4.3.x)
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "automation_heartbeat",
                "trigger": "interval",
                "interval": 240,
                "action": "run_command",
                "params": {"cmd": "echo Heartbeat OK"},
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS (4.3.x)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Run test command",
                "action": "run_command",
                "params": {"cmd": "echo Test OK"},
            },
            {
                "type": "button",
                "label": "Run script",
                "action": "run_script",
                "params": {"script": "test.py"},
            },
        ]

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
