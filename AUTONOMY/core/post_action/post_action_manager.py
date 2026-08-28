import os
import json

IPC_RESPONSES = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\responses.json"
IPC_CONFIRM = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\confirm.json"
POST_ACTION_LOG = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\post_action_log.json"


class PostActionManager:

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

    def _save_post_action_log(self, processed):
        try:
            with open(POST_ACTION_LOG, "w", encoding="utf-8") as f:
                json.dump(processed, f, indent=2)
        except Exception as e:
            print("[POST-ACTION] ERROR pri ukladaní logu:", e)

    def _clear_ipc_files(self):
        """Vymaže responses.json a post_action_log.json po spracovaní."""
        try:
            # Vymaž responses.json
            if os.path.exists(IPC_RESPONSES):
                with open(IPC_RESPONSES, "w", encoding="utf-8") as f:
                    json.dump([], f)

            # Vymaž post_action_log.json
            if os.path.exists(POST_ACTION_LOG):
                with open(POST_ACTION_LOG, "w", encoding="utf-8") as f:
                    json.dump([], f)

            print("[POST-ACTION] IPC súbory vymazané.")
        except Exception as e:
            print("[POST-ACTION] ERROR pri mazaní IPC súborov:", e)

    def process_responses(self):
        print("[POST-ACTION] Spúšťam spracovanie výsledkov COLNÍKA...")

        responses = self._load_responses()
        if not responses:
            print("[POST-ACTION] Žiadne responses – nič nespracovávam.")
            return

        processed = []

        for r in responses:
            decision = r.get("decision")
            req_id = r.get("request_id")
            action = r.get("action")
            reason = r.get("reason", "")

            entry = {
                "request_id": req_id,
                "decision": decision,
                "action": action,
                "reason": reason
            }

            print(f"[POST-ACTION] Spracovávam: {entry}")
            processed.append(entry)

        # uložiť log
        self._save_post_action_log(processed)

        # vyčistiť responses.json + post_action_log.json
        self._clear_ipc_files()

        print("[POST-ACTION] Spracovanie dokončené.")
