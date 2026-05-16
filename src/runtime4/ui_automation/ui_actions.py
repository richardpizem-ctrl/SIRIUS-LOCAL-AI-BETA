"""
UI Actions Module – Runtime 4.2.0

Zodpovedá za:
- vykonávanie UI akcií (klik, write, select…)
- semantické akcie (open settings, confirm, cancel…)
- bezpečné volanie cez UI Sandbox
- integráciu s UI Parser a UI Graph

Tento modul NEPRACUJE priamo s OS.
Všetky akcie idú cez bezpečnostnú vrstvu (UI Sandbox).
"""

class UIActions:
    def __init__(self, sandbox=None):
        self.sandbox = sandbox
        self.last_log = []  # jednoduchý audit trail

    # ------------------------------------------------------------
    # INTERNÝ LOGOVACÍ MECHANIZMUS
    # ------------------------------------------------------------
    def _log(self, action_type, element=None, value=None, result=True):
        entry = {
            "action": action_type,
            "element": getattr(element, "name", element),
            "value": value,
            "result": result,
        }
        self.last_log.append(entry)
        return entry

    # ------------------------------------------------------------
    # HLAVNÉ UI AKCIE
    # ------------------------------------------------------------
    def click(self, element):
        """
        Klikne na UI prvok.
        """
        if not self._allowed("click", element):
            self._log("click", element, result=False)
            return False

        # TODO: implementovať cez VYSLANEC / WinCapabilities
        self._log("click", element, result=True)
        return True

    def write(self, element, text):
        """
        Zapíše text do UI prvku.
        """
        if not self._allowed("write", element):
            self._log("write", element, value=text, result=False)
            return False

        # TODO: implementovať bezpečné zapisovanie
        self._log("write", element, value=text, result=True)
        return True

    def select(self, element, option):
        """
        Vyberie položku z menu alebo zoznamu.
        """
        if not self._allowed("select", element):
            self._log("select", element, value=option, result=False)
            return False

        # TODO: implementovať výber položky
        self._log("select", element, value=option, result=True)
        return True

    def semantic(self, action_name, context=None):
        """
        Semantické akcie typu:
        - open_settings
        - confirm
        - cancel
        - open_window
        - close_window
        """
        if not self._allowed("semantic", action_name):
            self._log("semantic", action_name, result=False)
            return False

        # TODO: implementovať mapovanie semantických akcií
        self._log("semantic", action_name, result=True)
        return True

    # ------------------------------------------------------------
    # SANDBOX CHECK
    # ------------------------------------------------------------
    def _allowed(self, action_type, target):
        """
        Overí, či je akcia povolená podľa UI Sandbox.
        """
        if self.sandbox:
            return self.sandbox.check_permission(action_type, target)
        return True
