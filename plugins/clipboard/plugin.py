# plugin.py
# SIRIUS LOCAL AI – Clipboard Plugin 4.3.x
# Safe, deterministic, sandboxed clipboard module

from __future__ import annotations

import pyperclip


class Plugin:
    """
    Clipboard Plugin 4.3.x

    Responsibilities:
        - Provide NL commands for clipboard operations
        - Provide AI tasks for clipboard operations
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Deterministic, safe-mode aware, degraded-mode aware
        - Self‑Repair 4.4 ready
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.safe_mode = False
        self.degraded_mode = False

        self.rm.logger.info("[PLUGIN:clipboard] Initialized (v4.3.x)")

    # --------------------------------------------------------
    # NL COMMANDS (4.3.x)
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
            self.degraded_mode = True
            self.rm.logger.error(f"[CLIPBOARD] Copy error: {e}")
            return "Clipboard error."

    def _nl_paste(self, text):
        try:
            content = pyperclip.paste()
            return f"From clipboard: {content}"
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"[CLIPBOARD] Paste error: {e}")
            return "Clipboard error."

    def _nl_read(self, text):
        try:
            content = pyperclip.paste()
            return f"Clipboard contains: {content}"
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"[CLIPBOARD] Read error: {e}")
            return "Clipboard error."

    # --------------------------------------------------------
    # AI TASKS (4.3.x)
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
            self.degraded_mode = True
            self.rm.logger.error(f"[CLIPBOARD] AI copy error: {e}")
            return {"error": "Clipboard error"}

    def _ai_paste(self, params):
        try:
            content = pyperclip.paste()
            return {"status": "OK", "content": content}
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"[CLIPBOARD] AI paste error: {e}")
            return {"error": "Clipboard error"}

    def _ai_read(self, params):
        try:
            content = pyperclip.paste()
            return {"clipboard": content}
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"[CLIPBOARD] AI read error: {e}")
            return {"error": "Clipboard error"}

    # --------------------------------------------------------
    # WORKFLOWS (4.3.x)
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
    # AI LOOP RULES (4.3.x)
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
    # GUI ELEMENTS (4.3.x)
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
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
