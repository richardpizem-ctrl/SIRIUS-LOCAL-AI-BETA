# plugin.py
# SIRIUS LOCAL AI – Clipboard Plugin 4.4.0
# Safe, deterministic, sandboxed clipboard module with integrity + health support

from __future__ import annotations

import pyperclip
import os


class Plugin:
    """
    Clipboard Plugin 4.4.0

    Responsibilities:
        - Provide NL commands for clipboard operations
        - Provide AI tasks for clipboard operations
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Deterministic, safe-mode aware, degraded-mode aware
        - Provide integrity hooks (4.4)
        - Provide health metadata (4.4)
        - Support Self‑Repair Layer 4.4
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

        # Runtime 4.4 modes
        self.safe_mode = False
        self.degraded_mode = False

        # 4.4 integrity + health
        self.integrity_ok = True
        self.health_status = "OK"

        self.rm.logger.info("[PLUGIN:clipboard] Initialized (v4.4.0)")

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
        self.rm.logger.warn("[PLUGIN:clipboard] Integrity repair triggered.")
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
            "copy": self._nl_copy,
            "paste": self._nl_paste,
            "clipboard": self._nl_read,
        }

    def _nl_copy(self, text):
        if self.safe_mode:
            return "SAFE MODE: Clipboard write disabled."

        try:
            pyperclip.copy(text)
            return f"Copied to clipboard: {text}"
        except Exception as e:
            self._handle_error("Copy", e)
            return "Clipboard error."

    def _nl_paste(self, text):
        try:
            content = pyperclip.paste()
            return f"From clipboard: {content}"
        except Exception as e:
            self._handle_error("Paste", e)
            return "Clipboard error."

    def _nl_read(self, text):
        try:
            content = pyperclip.paste()
            return f"Clipboard contains: {content}"
        except Exception as e:
            self._handle_error("Read", e)
            return "Clipboard error."

    # --------------------------------------------------------
    # AI TASKS (4.4)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "clipboard_copy": self._ai_copy,
            "clipboard_paste": self._ai_paste,
            "clipboard_read": self._ai_read,
        }

    def _ai_copy(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        text = params.get("text", "")
        try:
            pyperclip.copy(text)
            return {"status": "OK", "copied": text}
        except Exception as e:
            self._handle_error("AI copy", e)
            return {"error": "Clipboard error"}

    def _ai_paste(self, params):
        try:
            content = pyperclip.paste()
            return {"status": "OK", "content": content}
        except Exception as e:
            self._handle_error("AI paste", e)
            return {"error": "Clipboard error"}

    def _ai_read(self, params):
        try:
            content = pyperclip.paste()
            return {"clipboard": content}
        except Exception as e:
            self._handle_error("AI read", e)
            return {"error": "Clipboard error"}

    # --------------------------------------------------------
    # WORKFLOWS (4.4)
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "clipboard_log",
                "steps": [
                    {"action": "log", "message": "Reading clipboard content..."},
                    {"action": "task", "task": "clipboard_read"},
                    {"action": "return", "value": "Done."},
                ],
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES (4.4)
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "clipboard_monitor",
                "trigger": "interval",
                "interval": 90,
                "action": "clipboard_read",
                "params": {},
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS (4.4)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Copy text",
                "action": "clipboard_copy",
                "params": {"text": "Hello world"},
            },
            {
                "type": "button",
                "label": "Paste from clipboard",
                "action": "clipboard_paste",
            },
            {
                "type": "button",
                "label": "Show clipboard",
                "action": "clipboard_read",
            },
        ]

    # --------------------------------------------------------
    # INTERNAL ERROR HANDLER (4.4)
    # --------------------------------------------------------
    def _handle_error(self, label, exception):
        self.degraded_mode = True
        self.health_status = "DEGRADED"
        self.rm.logger.error(f"[CLIPBOARD] {label} error: {exception}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL (4.4)
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.rm.logger.warn("[PLUGIN:clipboard] Entered SAFE MODE.")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.rm.logger.info("[PLUGIN:clipboard] Exited SAFE MODE.")
