# plugin.py
# SIRIUS LOCAL AI – Translator Plugin 4.3.x
# Safe, deterministic translation module using ContextManager.translate()

from __future__ import annotations


class Plugin:
    """
    Translator Plugin 4.3.x

    Responsibilities:
        - Provide NL commands for translation
        - Provide AI tasks for translation
        - Provide workflows
        - Provide AI Loop rules
        - Provide GUI elements
        - Deterministic, safe-mode aware, degraded-mode aware
        - Self‑Repair 4.4 ready
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.ctx = runtime_manager.context

        self.safe_mode = False
        self.degraded_mode = False

        self.rm.logger.info("[PLUGIN:translator] Initialized (v4.3.x)")

    # --------------------------------------------------------
    # NL COMMANDS (4.3.x)
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

        try:
            result = self.ctx.translate(sentence, lang)
            return f"Translation ({lang}): {result}"
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"[TRANSLATOR] Error: {e}")
            return "Translation error."

    # --------------------------------------------------------
    # AI TASKS (4.3.x)
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

        try:
            result = self.ctx.translate(text, lang)
            return {
                "status": "OK",
                "translated": result,
                "target_lang": lang,
            }
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"[TRANSLATOR] AI error: {e}")
            return {"error": "Translation failed"}

    # --------------------------------------------------------
    # WORKFLOWS (4.3.x)
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
    # AI LOOP RULES (4.3.x)
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
    # GUI ELEMENTS (4.3.x)
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
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
