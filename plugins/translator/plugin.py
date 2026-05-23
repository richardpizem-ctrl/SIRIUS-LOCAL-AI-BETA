# plugin.py
# SIRIUS LOCAL AI – Translator Plugin 4.5.0
# Safe, deterministic translation module using ContextManager.translate()
# with integrity + health support

from __future__ import annotations

import os


class Plugin:
    """
    Translator Plugin 4.5.0

    Responsibilities:
        - Provide NL commands for translation
        - Provide AI tasks for translation
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Deterministic, safe-mode aware, degraded-mode aware
        - Plugin Integrity Hooks (4.5)
        - Health Metadata (4.5)
        - Self‑Repair Layer 4.5 compatibility
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.ctx = runtime_manager.context

        # Runtime 4.5 modes
        self.safe_mode = False
        self.degraded_mode = False

        # 4.5 integrity + health
        self.integrity_ok = True
        self.health_status = "OK"

        self.rm.logger.info("[PLUGIN:translator] Initialized (v4.5.0)")

    # --------------------------------------------------------
    # INTEGRITY HOOKS (4.5)
    # --------------------------------------------------------
    def integrity_check(self):
        try:
            return os.path.exists(__file__)
        except Exception:
            return False

    def integrity_repair(self):
        self.rm.logger.warn("[PLUGIN:translator] Integrity repair triggered.")
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
            "translate to": self._nl_translate,
            "preloz do": self._nl_translate,
        }

    def _nl_translate(self, text):
        """
        Format:
            translate to en Hello world
            preloz do sk Hello world
        """
        if self.safe_mode:
            return "SAFE MODE: Translation disabled."

        parts = text.split(" ", 1)
        if len(parts) < 2:
            return "Usage: translate to <lang> <text>"

        lang = parts[0].strip()
        sentence = parts[1].strip()

        action_id = f"translator_nl_{lang}"

        try:
            result = self.ctx.translate(sentence, lang)
            return f"Translation ({lang}): {result}"
        except Exception as e:
            self._handle_error(action_id, e)
            return "Translation error."

    # --------------------------------------------------------
    # AI TASKS (4.5)
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "translate_text": self._ai_translate_text,
        }

    def _ai_translate_text(self, params):
        if self.safe_mode:
            return {"error": "SAFE MODE"}

        text = params.get("text")
        lang = params.get("lang")

        if not text or not lang:
            return {"error": "Missing 'text' or 'lang' parameter."}

        action_id = f"translator_ai_{lang}"

        try:
            result = self.ctx.translate(text, lang)
            return {
                "status": "OK",
                "translated": result,
                "target_lang": lang,
            }
        except Exception as e:
            self._handle_error(action_id, e)
            return {"error": "Translation failed"}

    # --------------------------------------------------------
    # WORKFLOWS (4.5)
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "auto_translate_log",
                "steps": [
                    {"action": "log", "message": "Automatic text translation..."},
                    {
                        "action": "task",
                        "task": "translate_text",
                        "params": {"text": "Hello world", "lang": "sk"},
                    },
                    {"action": "return", "value": "Translation workflow completed."},
                ],
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES (4.5)
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "translator_heartbeat",
                "trigger": "interval",
                "interval": 120,
                "action": "translate_text",
                "params": {"text": "System check", "lang": "sk"},
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS (4.5)
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Translate to EN",
                "action": "translate_text",
                "params": {"lang": "en", "text": "Ahoj svet"},
            },
            {
                "type": "button",
                "label": "Translate to DE",
                "action": "translate_text",
                "params": {"lang": "de", "text": "Ahoj svet"},
            },
        ]

    # --------------------------------------------------------
    # INTERNAL ERROR HANDLER (4.5)
    # --------------------------------------------------------
    def _handle_error(self, label, exception):
        self.degraded_mode = True
        self.health_status = "DEGRADED"
        self.rm.logger.error(f"[TRANSLATOR] {label} error: {exception}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL (4.5)
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.rm.logger.warn("[PLUGIN:translator] Entered SAFE MODE.")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.rm.logger.info("[PLUGIN:translator] Exited SAFE MODE.")
