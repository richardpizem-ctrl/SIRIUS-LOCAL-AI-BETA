class Dispatcher:
    """
    UI PANEL – ACTION DISPATCHER
    Rozhoduje, ktorý modul vykoná akciu podľa typu requestu.
    """

    def __init__(self):
        pass

    def dispatch(self, req: dict) -> str:
        """
        Vráti názov modulu, ktorý má spracovať request.
        UI PANEL zatiaľ nemá implementované moduly,
        takže len mapujeme typy.
        """

        action = req.get("action", "").lower()

        if action in ("delete_duplicate", "resolve_duplicate"):
            return "duplicates"

        if action in ("triage_folder", "move_folder"):
            return "triage"

        if action in ("navigate", "open_folder", "open_file"):
            return "navigation"

        if action in ("run_terminal", "execute_command"):
            return "terminal"

        if action in ("update_config", "set_config"):
            return "config"

        # fallback
        return "unknown"
