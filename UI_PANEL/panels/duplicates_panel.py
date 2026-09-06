import time

class DuplicatesPanel:
    """
    UI PANEL – DUPLICATES PANEL
    Spracováva akcie:
    - delete_duplicate
    - resolve_duplicate
    """

    def __init__(self):
        pass

    def handle(self, req: dict) -> dict:
        """
        Spracuje duplicitu.
        Zatiaľ len simulácia vykonania.
        """

        rid = req.get("request_id", "UNKNOWN_ID")
        action = req.get("action", "UNKNOWN_ACTION")
        target = req.get("target", "UNKNOWN_TARGET")
        payload = req.get("payload", {})

        print(f"[DUPLICATES_PANEL] Spracovávam duplicitu: {rid}")
        print(f"  Action: {action}")
        print(f"  Target: {target}")
        print(f"  Payload: {payload}")

        # Simulácia reálneho vykonania
        time.sleep(0.5)

        print(f"[DUPLICATES_PANEL] Duplicita {rid} spracovaná OK.")

        # Výsledok pre Execution Core
        return {
            "request_id": rid,
            "success": True,
            "module": "duplicates",
            "action": action,
            "target": target
        }
