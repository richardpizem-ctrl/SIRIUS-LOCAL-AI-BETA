# plugin.py
# SIRIUS LOCAL AI – Example Plugin 4.3.x
# Reference implementation for all SIRIUS plugins

from __future__ import annotations


class Plugin:
    """
    Example Plugin 4.3.x

    Demonstrates:
        - NL commands
        - AI tasks
        - Workflows
        - AI Loop rules
        - GUI elements
        - Safe-mode + degraded-mode support
        - Deterministic behavior
        - Self‑Repair 4.4 readiness
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.safe_mode = False
        self.degraded_mode = False

        self.rm.logger.info("[PLUGIN:example] Initialized (v4.3.x)")

    # --------------------------------------------------------
    # NL COMMANDS (4.3.x)
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "hello plugin": self._nl_hello,
            "test plugin": self._nl_test,
            "plugin workflow": self._nl_run_workflow,
        }

    def _nl_hello(self, text):
        return "Hello! The Example Plugin 4.3.x is active and responding."

    def _nl_test(self, text):
        return "Example Plugin 4.3.x — NL command executed successfully."

    def _nl_run_workflow(self, text):
        try:
            return self.rm.run_workflow("plugin_demo_workflow")
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"[EXAMPLE] Workflow error: {e}")
            return "Workflow error."

    # --------------------------------------------------------
    # AI TASKS (4.3.x)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "plugin_test_task": self._ai_test_task,
            "plugin_status": self._ai_status,
        }

    def _ai_test_task(self, params):
        return {
            "status": "OK",
            "message": "Example Plugin 4.3.x — AI task executed successfully.",
        }

    def _ai_status(self, params):
        return {
            "plugin": "example",
            "state": "running",
            "info": "Example Plugin 4.3.x is operating normally.",
        }

    # --------------------------------------------------------
    # WORKFLOWS (4.3.x)
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "plugin_demo_workflow",
                "steps": [
                    {"action": "log", "message": "Example workflow started."},
                    {"action": "task", "task": "plugin_test_task"},
                    {"action": "return", "value": "Example workflow completed."},
                ],
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES (4.3.x)
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "plugin_auto_log",
                "trigger": "interval",
                "interval": 30,
                "action": "plugin_status",
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS (4.3.x)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Plugin Test",
                "action": "plugin_test_task",
            },
            {
                "type": "button",
                "label": "Run workflow",
                "action": "plugin_demo_workflow",
            },
        ]

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
