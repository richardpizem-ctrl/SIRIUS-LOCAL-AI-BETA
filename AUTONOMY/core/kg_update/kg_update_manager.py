import os
import json

IPC_RESPONSES = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json"
KG_UPDATE_LOG = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\kg_update_log.json"


class KGUpdateManager:

    def __init__(self):
        pass

    def _load_responses(self):
        if not os.path.exists(IPC_RESPONSES):
            return []

        try:
            with open(IPC_RESPONSES, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            return []

        if isinstance(data, dict):
            return data.get("responses", [])
        elif isinstance(data, list):
            return data
        return []

    def _save_update_log(self, updates):
        try:
            with open(KG_UPDATE_LOG, "w", encoding="utf-8") as f:
                json.dump(updates, f, indent=2)
        except Exception as e:
            print("[KG UPDATE] ERROR pri ukladaní logu:", e)

    def apply_updates(self):
        print("[KG UPDATE] Spúšťam aktualizáciu KG...")

        responses = self._load_responses()
        if not responses:
            print("[KG UPDATE] Žiadne responses – KG sa nemení.")
            return

        updates = []

        for r in responses:
            req_id = r.get("request_id")
            decision = r.get("decision")
            action = r.get("action")
            reason = r.get("reason", "")

            entry = {
                "request_id": req_id,
                "decision": decision,
                "action": action,
                "reason": reason
            }

            print(f"[KG UPDATE] Aktualizujem KG pre: {entry}")
            updates.append(entry)

        self._save_update_log(updates)

        print("[KG UPDATE] Aktualizácia KG dokončená.")
