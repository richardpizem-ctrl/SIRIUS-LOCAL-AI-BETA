# ENVOY — Log
# Logovanie karanténnych udalostí SIRIUS 6.x
# Úlohy:
# - zapisovať všetky ENVOY operácie
# - zapisovať chyby
# - zapisovať presuny súborov
# - zapisovať rozhodnutia pravidiel
# - zapisovať všetko do KG

import os
from datetime import datetime

from kg.kg_core import KGCore
kg = KGCore()

class EnvoyLog:

    def __init__(self):
        # cesta k log súboru
        self.log_path = os.path.join(os.getcwd(), "envoy", "envoy.log")

        # vytvor log súbor ak neexistuje
        if not os.path.exists(self.log_path):
            with open(self.log_path, "w", encoding="utf-8") as f:
                f.write("=== ENVOY LOG INITIALIZED ===\n")

        # KG registrácia modulu
        kg.add_entity("envoy_log", {"type": "module"})
        kg.add_relation("envoy_log", "initialized", "envoy")

    def write(self, message):
        """
        Zapíše správu do log súboru + KG.
        """

        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] {message}\n"

        # zapis do súboru
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(entry)

        # zapis do KG
        log_id = f"envoy_log_{timestamp}"

        kg.add_entity(log_id, {
            "type": "envoy_log_entry",
            "message": message,
            "timestamp": timestamp
        })

        kg.add_relation("envoy_log", "logged", log_id)

    def log_quarantine(self, file_name, reason):
        """
        Logovanie karantény súboru.
        """

        msg = f"Karanténa súboru '{file_name}' — dôvod: {reason}"
        self.write(msg)

    def log_rule(self, file_name, rule_reason):
        """
        Logovanie rozhodnutia pravidiel.
        """

        msg = f"Pravidlo aplikované na '{file_name}' — {rule_reason}"
        self.write(msg)

    def log_error(self, error_message):
        """
        Logovanie chyby.
        """

        msg = f"CHYBA: {error_message}"
        self.write(msg)

    def log_info(self, info_message):
        """
        Logovanie informačnej správy.
        """

        msg = f"INFO: {info_message}"
        self.write(msg)
