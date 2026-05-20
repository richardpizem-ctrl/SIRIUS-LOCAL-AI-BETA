# household_4_4/ha_safety_guard_4_4.py
"""
SIRIUS LOCAL AI – Household Safety Guard 4.4.0

Účel:
- bezpečnostná vrstva pre domáce príkazy
- kontrola identity (OWNER, FAMILY, CHILD, STRANGER)
- blokovanie nebezpečných akcií
- ochrana pred neplatnými alebo rizikovými príkazmi
- 100 % offline, deterministické

Pravidlá:
- STRANGER → blokuje všetky akcie
- CHILD → povolené len bezpečné akcie (žiadne zásuvky, spotrebiče, dvere)
- FAMILY → povolené všetko okrem kritických akcií (napr. reset, mazanie)
- OWNER → plný prístup
"""

from typing import Dict, Any


class HouseholdSafetyGuard44:
    """
    Deterministic safety guard pre domácnosť.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

        # Zakázané akcie pre rôzne identity
        self.forbidden_for_child = ["socket", "appliance", "door"]
        self.forbidden_for_family = ["factory_reset", "wipe", "delete_all"]

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}
        try:
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # MAIN CHECK
    # ------------------------------------------------------------------
    def check_command(self, command: str, identity: str) -> Dict[str, Any]:
        """
        Hlavná bezpečnostná kontrola.
        """

        identity = identity.upper().strip()

        # STRANGER → všetko blokované
        if identity == "STRANGER":
            return {
                "status": "blocked",
                "reason": "identity_restricted",
                "identity": identity,
            }

        # CHILD → kontrola rizikových slov
        if identity == "CHILD":
            for word in self.forbidden_for_child:
                if word in command.lower():
                    return {
                        "status": "blocked",
                        "reason": "child_forbidden_action",
                        "word": word,
                    }

        # FAMILY → blokuje kritické akcie
        if identity == "FAMILY":
            for word in self.forbidden_for_family:
                if word in command.lower():
                    return {
                        "status": "blocked",
                        "reason": "family_forbidden_action",
                        "word": word,
                    }

        # OWNER → všetko povolené
        if identity == "OWNER":
            return {"status": "ok"}

        # Neznáma identita
        return {
            "status": "blocked",
            "reason": "unknown_identity",
            "identity": identity,
        }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "child_forbidden_count": len(self.forbidden_for_child),
            "family_forbidden_count": len(self.forbidden_for_family),
        }
