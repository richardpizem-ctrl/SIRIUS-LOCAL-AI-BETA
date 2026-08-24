# ENVOY — Manager
# Hlavný modul karantény SIRIUS 6.x
# Úlohy:
# - prijíma požiadavky z Workflow
# - presúva súbory do karantény
# - zapisuje udalosti do KG
# - nikdy nič nespúšťa, nemaže, neopravuje

import os
import shutil
from datetime import datetime

from kg.kg_core import KGCore
kg = KGCore()

class EnvoyManager:

    def __init__(self):
        # cesta ku karanténe
        self.quarantine_root = os.path.join(os.getcwd(), "envoy", "quarantine")

        # vytvor karanténny priečinok ak neexistuje
        if not os.path.exists(self.quarantine_root):
            os.makedirs(self.quarantine_root)

        # KG registrácia modulu
        kg.add_entity("envoy_manager", {"type": "module"})
        kg.add_relation("envoy_manager", "initialized", "envoy")

    def quarantine_file(self, file_path, reason="unknown"):
        """
        Presunie súbor do karantény.
        Workflow volá túto funkciu po povolení COLNÍKOM.
        """

        if not os.path.exists(file_path):
            return {
                "status": "ERROR",
                "message": f"Súbor neexistuje: {file_path}"
            }

        # názov súboru
        file_name = os.path.basename(file_path)

        # cieľová cesta v karanténe
        quarantine_path = os.path.join(self.quarantine_root, file_name)

        # presun súboru
        shutil.move(file_path, quarantine_path)

        # KG zápis
        quarantine_id = f"quarantine_{file_name}_{datetime.now().timestamp()}"

        kg.add_entity(quarantine_id, {
            "type": "quarantined_file",
            "file_name": file_name,
            "original_path": file_path,
            "quarantine_path": quarantine_path,
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        })

        kg.add_relation("envoy_manager", "quarantined", quarantine_id)

        return {
            "status": "OK",
            "file": file_name,
            "quarantine_path": quarantine_path,
            "reason": reason
        }

    def list_quarantine(self):
        """
        Vráti zoznam súborov v karanténe.
        """

        files = os.listdir(self.quarantine_root)
        return {
            "status": "OK",
            "count": len(files),
            "files": files
        }

    def get_quarantine_info(self, file_name):
        """
        Vráti informácie o konkrétnom súbore v karanténe.
        """

        path = os.path.join(self.quarantine_root, file_name)

        if not os.path.exists(path):
            return {
                "status": "ERROR",
                "message": "Súbor nie je v karanténe."
            }

        return {
            "status": "OK",
            "file": file_name,
            "path": path,
            "size": os.path.getsize(path)
        }
