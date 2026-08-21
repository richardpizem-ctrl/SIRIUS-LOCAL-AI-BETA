# ENVOY — Rules
# Pravidlá karantény SIRIUS 6.x
# Úlohy:
# - vyhodnotiť, či súbor je nebezpečný
# - definovať dôvody karantény
# - poskytnúť rozhodnutie Workflow a COLNÍK-u
# - zapisovať pravidlá do KG

import os
from kg.kg_core import KGCore
kg = KGCore()

class EnvoyRules:

    def __init__(self):
        # KG registrácia modulu
        kg.add_entity("envoy_rules", {"type": "module"})
        kg.add_relation("envoy_rules", "initialized", "envoy")

        # definícia nebezpečných prípon
        self.dangerous_extensions = {
            ".exe", ".bat", ".cmd", ".ps1", ".vbs",
            ".js", ".msi", ".scr", ".dll"
        }

        # definícia podozrivých názvov
        self.suspicious_names = {
            "virus", "trojan", "worm", "backdoor",
            "keylogger", "malware", "danger", "risk"
        }

    def evaluate_file(self, file_path):
        """
        Vyhodnotí, či súbor je nebezpečný.
        Autonómia → návrh QUARANTINE
        COLNÍK → povolenie
        Workflow → volá ENVOY
        """

        if not os.path.exists(file_path):
            return {
                "status": "ERROR",
                "message": "Súbor neexistuje."
            }

        file_name = os.path.basename(file_path)
        extension = os.path.splitext(file_name)[1].lower()

        # === 1. Nebezpečná prípona ===
        if extension in self.dangerous_extensions:
            reason = f"Nebezpečná prípona: {extension}"
            self._log_rule(file_name, reason)
            return {
                "status": "DANGEROUS",
                "reason": reason
            }

        # === 2. Podozrivý názov ===
        for suspicious in self.suspicious_names:
            if suspicious in file_name.lower():
                reason = f"Podozrivý názov obsahuje: {suspicious}"
                self._log_rule(file_name, reason)
                return {
                    "status": "SUSPICIOUS",
                    "reason": reason
                }

        # === 3. Veľkosť súboru (príliš malý alebo príliš veľký) ===
        size = os.path.getsize(file_path)

        if size == 0:
            reason = "Prázdny súbor — potenciálne nebezpečný."
            self._log_rule(file_name, reason)
            return {
                "status": "SUSPICIOUS",
                "reason": reason
            }

        if size > 500_000_000:  # 500 MB
            reason = "Extrémne veľký súbor — riziko."
            self._log_rule(file_name, reason)
            return {
                "status": "SUSPICIOUS",
                "reason": reason
            }

        # === 4. Bezpečný súbor ===
        self._log_rule(file_name, "Bezpečný súbor — karanténa sa nevyžaduje.")
        return {
            "status": "SAFE",
            "reason": "Bezpečný súbor"
        }

    def _log_rule(self, file_name, reason):
        """
        Zapíše pravidlo do KG.
        """

        rule_id = f"envoy_rule_{file_name}"

        kg.add_entity(rule_id, {
            "type": "envoy_rule",
            "file": file_name,
            "reason": reason
        })

        kg.add_relation("envoy_rules", "evaluated", rule_id)
