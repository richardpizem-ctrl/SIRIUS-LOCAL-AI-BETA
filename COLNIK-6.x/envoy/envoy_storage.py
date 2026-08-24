# ENVOY — Storage
# Úložisko karantény SIRIUS 6.x
# Úlohy:
# - vytvoriť karanténny priečinok
# - presúvať súbory do karantény
# - evidovať metadáta
# - zapisovať všetko do KG

import os
import shutil
from datetime import datetime

from kg.kg_core import KGCore
kg = KGCore()

class EnvoyStorage:

    def __init__(self):
        # cesta ku karanténe
        self.root = os.path.join(os.getcwd(), "envoy", "quarantine")

        # vytvor karanténny priečinok ak neexistuje
        if not os.path.exists(self.root):
            os.makedirs(self.root)

        # KG registrácia modulu
        kg.add_entity("envoy_storage", {"type": "module"})
        kg.add_relation("envoy_storage", "initialized", "envoy")

    def store(self, file_path, reason="unknown"):
        """
        Presunie súbor do karantény.
        Workflow → volá túto funkciu po povolení COLNÍKOM.
        """

        if not os.path.exists(file_path):
            return {
                "status": "ERROR",
                "message": f"Súbor neexistuje: {file_path}"
            }

        file_name = os.path.basename(file_path)
        quarantine_path = os.path.join(self.root, file_name)

        # presun súboru
        shutil.move(file_path, quarantine_path)

        # KG zápis
        quarantine_id = f"envoy_quarantine_{file_name}_{datetime.now().timestamp()}"

        kg.add_entity(quarantine_id, {
            "type": "quarantined_file",
            "file_name": file_name,
            "original_path": file_path,
            "quarantine_path": quarantine_path,
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        })

        kg.add_relation("envoy_storage", "stored", quarantine_id)

        return {
            "status": "OK",
            "file": file_name,
            "quarantine_path": quarantine_path,
            "reason": reason
        }

    def list(self):
        """
        Vráti zoznam súborov v karanténe.
        """

        files = os.listdir(self.root)
        return {
            "status": "OK",
            "count": len(files),
            "files": files
        }

    def info(self, file_name):
        """
        Vráti informácie o konkrétnom súbore v karanténe.
        """

        path = os.path.join(self.root, file_name)

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
