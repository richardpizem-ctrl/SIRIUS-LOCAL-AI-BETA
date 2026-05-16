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

    def click(self, element):
        """
        Klikne na UI prvok.
        """
        if not self._allowed("click", element):
            return False

        # TODO: implementovať cez VYSLANEC / WinCapabilities
        return True

    def write(self, element, text):
        """
        Zapíše text do UI prvku.
        """
        if not self._allowed("write", element):
            return False

        # TODO: implementovať bezpečné zapisovanie
        return True

    def select(self, element, option):
        """
        Vyberie položku z menu alebo zoznamu.
        """
        if not self._allowed("select", element):
            return False

        # TODO: implementovať výber položky
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
            return False

        # TODO: implementovať mapovanie semantických akcií
        return True

    def _allowed(self, action_type, target):
        """
        Overí, či je akcia povolená podľa UI Sandbox.
        """
        if self.sandbox:
            return self.sandbox.check_permission(action_type, target)
        return True
