from typing import Dict, Any
import logging
import re

log = logging.getLogger(__name__)


class NaturalLanguageRouter:
    """
    NL Router 4.0
    - Plugin dynamic NL commands
    - Pattern matching with parameters
    - Command Registry integration
    - Security Family enforcement
    - AITE fallback
    - SiriusAgent interpret fallback
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.agent
        self.dynamic_commands = {}   # phrase -> fn

    # --------------------------------------------------------
    # REGISTER PLUGIN COMMAND
    # --------------------------------------------------------
    def register(self, phrase: str, fn):
        """
        Register NL command from plugin.
        Supports pattern matching.
        """
        self.dynamic_commands[phrase.lower()] = fn
        log.info("NL Router registered plugin command: '%s'", phrase)

    # --------------------------------------------------------
    # MAIN HANDLER
    # --------------------------------------------------------
    def handle(self, text: str) -> Dict[str, Any]:
        text = text.lower().strip()
        log.info("NL Router received: %s", text)

        # ----------------------------------------------------
        # 1) Plugin NL commands (pattern match)
        # ----------------------------------------------------
        for phrase, fn in self.dynamic_commands.items():
            if phrase in text:
                try:
                    result = fn(text, self.rm)
                    return {
                        "status": "plugin",
                        "command": phrase,
                        "result": result
                    }
                except Exception as e:
                    return {
                        "status": "error",
                        "source": "plugin",
                        "message": str(e)
                    }

        # ----------------------------------------------------
        # 2) Rule-based NL commands (Password Vault + future logic)
        # ----------------------------------------------------
        rb = self._handle_rule_based(text)
        if rb is not None:
            return {
                "status": "rule_based",
                "result": rb
            }

        # ----------------------------------------------------
        # 3) AITE fallback
        # ----------------------------------------------------
        try:
            aite_result = self.rm.aite.process(text)
            if aite_result is not None:
                return {
                    "status": "aite",
                    "result": aite_result
                }
        except Exception as e:
            log.exception("AITE error: %s", e)

        # ----------------------------------------------------
        # 4) SiriusAgent interpret fallback
        # ----------------------------------------------------
        try:
            agent_result = self.agent.run_task("interpret", {"text": text})
            if agent_result is not None:
                return {
                    "status": "agent",
                    "result": agent_result
                }
        except Exception as e:
            log.exception("Agent interpret error: %s", e)

        # ----------------------------------------------------
        # 5) Final fallback
        # ----------------------------------------------------
        return {
            "status": "error",
            "message": "I do not understand the command."
        }

    # --------------------------------------------------------
    # RULE-BASED COMMANDS (PASSWORD VAULT 4.0)
    # --------------------------------------------------------
    def _handle_rule_based(self, text: str):
        """
        Rule-based NL commands for Password Vault 4.0
        """

        # ----------------------------------------------------
        # SAVE PASSWORD
        # ----------------------------------------------------
        # Example: "uloz heslo pre github je 12345"
        if "uloz heslo" in text or "save password" in text:
            try:
                # extract domain
                match = re.search(r"pre ([a-z0-9\.\-]+)", text)
                domain = match.group(1) if match else None

                # extract password
                match = re.search(r"je ([^\s]+)$", text)
                password = match.group(1) if match else None

                if domain and password:
                    from security_family.password_vault.vault_api import save_password
                    save_password(domain, "default", password)
                    return f"Heslo pre {domain} bolo uložené."
                else:
                    return "Nepodarilo sa extrahovať doménu alebo heslo."
            except Exception as e:
                return f"Chyba pri ukladaní hesla: {e}"

        # ----------------------------------------------------
        # RETRIEVE PASSWORD
        # ----------------------------------------------------
        # Example: "ake je heslo pre github"
        if "ake je heslo" in text or "what is the password" in text:
            try:
                match = re.search(r"pre ([a-z0-9\.\-]+)", text)
                domain = match.group(1) if match else None

                if domain:
                    from security_family.password_vault.vault_api import retrieve_password
                    entry = retrieve_password(domain)
                    if entry:
                        return f"Heslo pre {domain} je: {entry['password']}"
                    else:
                        return f"Nemám uložené heslo pre {domain}."
                else:
                    return "Nepodarilo sa extrahovať doménu."
            except Exception as e:
                return f"Chyba pri načítaní hesla: {e}"

        # ----------------------------------------------------
        # AUTOFILL PASSWORD (PC)
        # ----------------------------------------------------
        # Example: "vypln heslo pre github"
        if "vypln heslo" in text or "autofill password" in text:
            try:
                match = re.search(r"pre ([a-z0-9\.\-]+)", text)
                domain = match.group(1) if match else None

                if domain:
                    from security_family.password_vault.vault_api import retrieve_password
                    entry = retrieve_password(domain)
                    if entry:
                        # TODO: integrate with Windows UI Automation
                        return f"Heslo pre {domain} je pripravené na autofill."
                    else:
                        return f"Nemám uložené heslo pre {domain}."
                else:
                    return "Nepodarilo sa extrahovať doménu."
            except Exception as e:
                return f"Chyba pri autofill operácii: {e}"

        # ----------------------------------------------------
        # No match
        # ----------------------------------------------------
        return None
