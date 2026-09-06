import time

class TriagePanel:
    """
    UI PANEL – TRIAGE PANEL
    Spracováva akcie:
    - triage_folder
    - move_folder
    """

    def __init__(self):
        pass

    def handle(self, req: dict) -> dict:
        """
        Spracuje triage/move folder request.
        Zatiaľ len simulácia vykonania.
        """

        rid = req.get("request_id", "UNKNOWN_ID")
        action = req.get("action", "UNKNOWN_ACTION")
        target = req.get("target", "UNKNOWN_TARGET")
        payload = req.get("payload", {})

        print(f"[TRIAGE_PANEL] Spracovávam triage: {rid}")
        print(f"  Action: {action}")
        print(f"  Target: {target}")
        print(f"  Payload: {payload}")

        # Simulácia reálneho presunu
        time.sleep(0.5)

        print(f"[TRIAGE_PANEL] Triage {rid} spracovaný OK.")

        return {
            "request_id": rid,
            "success": True,
            "module": "triage",
            "action": action,
            "target": target
        }
