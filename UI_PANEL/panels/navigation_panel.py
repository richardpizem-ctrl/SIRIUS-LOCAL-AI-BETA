import time

class NavigationPanel:
    """
    UI PANEL – NAVIGATION PANEL
    Spracováva akcie:
    - navigate
    - open_folder
    - open_file
    """

    def __init__(self):
        pass

    def handle(self, req: dict) -> dict:
        """
        Spracuje navigačný request.
        Zatiaľ len simulácia vykonania.
        """

        rid = req.get("request_id", "UNKNOWN_ID")
        action = req.get("action", "UNKNOWN_ACTION")
        target = req.get("target", "UNKNOWN_TARGET")
        payload = req.get("payload", {})

        print(f"[NAVIGATION_PANEL] Navigujem: {rid}")
        print(f"  Action: {action}")
        print(f"  Target: {target}")
        print(f"  Payload: {payload}")

        # Simulácia navigácie
        time.sleep(0.5)

        print(f"[NAVIGATION_PANEL] Navigácia {rid} spracovaná OK.")

        return {
            "request_id": rid,
            "success": True,
            "module": "navigation",
            "action": action,
            "target": target
        }
