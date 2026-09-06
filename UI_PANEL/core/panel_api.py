# panel_api.py – API pre UI PANEL

class PanelAPI:
    """
    Jednoduché API pre UI PANEL.
    Orchestrátor volá:
        ui.get_user_input()
        ui.update(output)
        ui.show_error(msg)
    """

    def __init__(self):
        print("[UI_PANEL] PanelAPI initialized")

    def get_user_input(self):
        """
        Dočasná implementácia – neskôr sa prepojí s backend_bridge.
        Zatiaľ len číta input z konzoly.
        """
        try:
            return input("SIRIUS> ")
        except Exception:
            return None

    def update(self, output):
        """
        Zobrazí výsledok EXECUTE.
        """
        print(f"[UI_PANEL] OUTPUT: {output}")

    def show_error(self, msg):
        """
        Zobrazí chybu.
        """
        print(f"[UI_PANEL] ERROR: {msg}")
