# IPC – SEND TO COLNIK
# Autonómia posiela návrhy do COLNÍKA cez JSON súbor

import json
import os

class IPCSender:

    def __init__(self, out_path=r"..\IPC_DATA\proposals.json"):
        self.out_path = os.path.abspath(out_path)

    def send(self, proposals):
        """
        proposals = list of JSON-ready dicts
        """
        try:
            # Validácia vstupu
            if not isinstance(proposals, list):
                print("IPC SEND ERROR: proposals must be a list")
                return False

            # Vytvorenie priečinka ak neexistuje
            os.makedirs(os.path.dirname(self.out_path), exist_ok=True)

            # Zápis JSON – kompatibilné s COLNÍK 6.x
            payload = {
                "proposals": proposals
            }

            with open(self.out_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)

            print("[IPC] proposals.json uložený →", self.out_path)
            return True

        except Exception as e:
            print("IPC SEND ERROR:", e)
            return False
