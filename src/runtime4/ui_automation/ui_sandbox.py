"""
UI Sandbox Module – Runtime 4.2.0

Zodpovedá za:
- bezpečnostné pravidlá pre UI akcie
- kontrolu identity (OWNER / FAMILY / STRANGER / CHILD)
- auditovanie UI operácií
- povolenia pre kliky, zápisy, výbery a semantické akcie

UI Sandbox je jediná vrstva, ktorá rozhoduje,
či UI akcia môže byť vykonaná.
"""

class UISandbox:
    def __init__(self, identity="OWNER"):
        """
        identity: aktuálna identita používateľa
        - OWNER   = plné práva
        - FAMILY  = obmedzené UI akcie
        - STRANGER = minimálne UI akcie
        - CHILD   = veľmi obmedzené akcie
        """
        self.identity = identity

    def check_permission(self, action_type, target):
        """
        Overí, či je akcia povolená podľa identity.
        action_type: "click", "write", "select", "semantic"
        target: UI prvok alebo názov akcie
        """
        # OWNER má plný prístup
        if self.identity == "OWNER":
            return True

        # FAMILY – povolené len neškodné akcie
        if self.identity == "FAMILY":
            return self._family_rules(action_type, target)

        # STRANGER – extrémne obmedzené akcie
        if self.identity == "STRANGER":
            return self._stranger_rules(action_type, target)

        # CHILD – iba bezpečné akcie
        if self.identity == "CHILD":
            return self._child_rules(action_type, target)

        return False

    def _family_rules(self, action_type, target):
        """
        FAMILY môže:
        - kliknúť na neškodné prvky
        - písať len do bezpečných polí
        - nemôže meniť systémové nastavenia
        """
        if action_type == "semantic":
            # zakázať systémové akcie
            if isinstance(target, str) and "settings" in target.lower():
                return False
        return True

    def _stranger_rules(self, action_type, target):
        """
        STRANGER môže:
        - len čítať UI (žiadne akcie)
        """
        return False

    def _child_rules(self, action_type, target):
        """
        CHILD môže:
        - kliknúť len na UI prvky označené ako bezpečné
        - nesmie písať text
        - nesmie otvárať nové okná
        """
        if action_type in ("write", "semantic"):
            return False
        return True

    def audit(self, action_type, target, allowed):
        """
        Audit log pre UI akcie.
        (Zatiaľ len placeholder – neskôr sa napojí na EventBus.)
        """
        pass
