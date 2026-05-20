# plugin.py
# SIRIUS LOCAL AI – Example Plugin 4.4.0
# Reference implementation for all SIRIUS plugins (Phase‑4.4)

from __future__ import annotations

import os


class Plugin:
    """
    Example Plugin 4.4.0

    Demonstrates:
        - NL commands
        - AI tasks
        - Workflows
        - AI Loop rules
        - GUI elements
        - Deterministic behavior
        - Safe-mode + degraded-mode support
        - Plugin Integrity Hooks (4.4)
        - Health Metadata (4.4)
        - Self‑Repair Layer 4.4 compatibility
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

        # Runtime 4.4 modes
        self.safe_mode = False
        self.degraded_mode = False

        # 4.4 integrity + health
        self.integrity_ok = True
        self.health_status = "OK"

        self.rm.logger.info("[PLUGIN:example] Initialized (v4.4.0)")

    # --------------------------------------------------------
    # INTEGRITY HOOKS (4.4)
    # --------------------------------------------------------
    def integrity_check(self):
        """
        Called by PluginLoader 4.4.
        Must return True/False.
        """
        try:
            return os.path.exists(__file__)
        except Exception:
            return False

    def integrity_repair(self):
        """
        Called by Self‑Repair Layer 4.4.
        Plugin may reload, reset state, or fallback.
        """
        self.rm.logger.warn("[PLUGIN:example] Integrity repair triggered.")
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
            "hello plugin": self._nl_hello,
            "test plugin": self._nl_test,
            "plugin workflow": self._nl_run_workflow,
        }

    def _nl_hello(self, text):
        return "Hello! The Example Plugin 4.4.0 is active and responding."

    def _nl_test(self, text):
        return "Example Plugin 4.4.0 — NL command executed successfully."

    def _nl_run_workflow(self, text):
        try:
            return self.rm.run_workflow("plugin_demo_workflow")
        except Exception as e:
            self._handle_error("Workflow", e)
            return "Workflow error."

    # --------------------------------------------------------
    # AI TASKS (4.4)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "plugin_test_task": self._ai_test_task,
            "plugin_status": self._ai_status,
        }

    def _ai_test_task(self, params):
        return {
            "status": "OK",
            "message": "Example Plugin 4.4.0 — AI task executed successfully.",
        }

    def _ai_status(self, params):
        return {
            "plugin": "example",
            "state": "running",
            "info": "Example Plugin 4.4.0 is operating normally.",
        }

    # --------------------------------------------------------
    # WORKFLOWS (4.4)
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
    # AI LOOP RULES (4.4)
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
    # GUI ELEMENTS (4.4)
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
    # INTERNAL ERROR HANDLER (4.4)
    # --------------------------------------------------------
    def _handle_error(self, label, exception):
        self.degraded_mode = True
        self.health_status = "DEGRADED"
        self.rm.logger.error(f"[EXAMPLE] {label} error: {exception}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL (4.4)
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.rm.logger.warn("[PLUGIN:example] Entered SAFE MODE.")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.rm.logger.info("[PLUGIN:example] Exited SAFE MODE.")
