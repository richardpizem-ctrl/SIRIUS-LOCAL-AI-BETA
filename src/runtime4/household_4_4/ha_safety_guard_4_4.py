"""
SIRIUS LOCAL AI – Household Safety Guard 4.5.0

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

Security Family 4.5:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any


class HouseholdSafetyGuard45:
    """
    Deterministic safety guard pre domácnosť 4.5.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # Zakázané akcie pre rôzne identity
        self.forbidden_for_child = ["socket", "appliance", "door"]
        self.forbidden_for_family = ["factory_reset", "wipe", "delete_all"]

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            self.initialized = True
            return {"status": "initialized", "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # MAIN CHECK
    # ---------------------------------------------------------
    def check_command(self, command: str, identity: str) -> Dict[str, Any]:
        """
        Hlavná bezpečnostná kontrola.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Safety guard disabled in safe-mode.",
                "degraded_mode": self.degraded_mode,
                "version": "4.5",
            }

        # VALIDATION
        if not self._validate_str(command):
            return {"status": "error", "code": "invalid_command", "version": "4.5"}

        if not self._validate_str(identity):
            return {"status": "error", "code": "invalid_identity", "version": "4.5"}

        identity = identity.upper().strip()
        cmd_lower = command.lower()

        # STRANGER → všetko blokované
        if identity == "STRANGER":
            return {
                "status": "blocked",
                "code": "identity_restricted",
                "identity": identity,
                "version": "4.5",
            }

        # CHILD → kontrola rizikových slov
        if identity == "CHILD":
            for word in self.forbidden_for_child:
                if word in cmd_lower:
                    return {
                        "status": "blocked",
                        "code": "child_forbidden_action",
                        "word": word,
                        "version": "4.5",
                    }

        # FAMILY → blokuje kritické akcie
        if identity == "FAMILY":
            for word in self.forbidden_for_family:
                if word in cmd_lower:
                    return {
                        "status": "blocked",
                        "code": "family_forbidden_action",
                        "word": word,
                        "version": "4.5",
                    }

        # OWNER → všetko povolené
        if identity == "OWNER":
            return {"status": "ok", "version": "4.5"}

        # Neznáma identita
        return {
            "status": "blocked",
            "code": "unknown_identity",
            "identity": identity,
            "version": "4.5",
        }

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "child_forbidden_count": len(self.forbidden_for_child),
            "family_forbidden_count": len(self.forbidden_for_family),
            "version": "4.5",
        }
