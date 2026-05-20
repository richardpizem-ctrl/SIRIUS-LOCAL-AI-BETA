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

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any


class HouseholdSafetyGuard44:
    """
    Deterministic safety guard pre domácnosť.
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
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

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
            }

        # VALIDATION
        if not self._validate_str(command):
            return {"status": "error", "code": "invalid_command"}

        if not self._validate_str(identity):
            return {"status": "error", "code": "invalid_identity"}

        identity = identity.upper().strip()
        cmd_lower = command.lower()

        # STRANGER → všetko blokované
        if identity == "STRANGER":
            return {
                "status": "blocked",
                "code": "identity_restricted",
                "identity": identity,
            }

        # CHILD → kontrola rizikových slov
        if identity == "CHILD":
            for word in self.forbidden_for_child:
                if word in cmd_lower:
                    return {
                        "status": "blocked",
                        "code": "child_forbidden_action",
                        "word": word,
                    }

        # FAMILY → blokuje kritické akcie
        if identity == "FAMILY":
            for word in self.forbidden_for_family:
                if word in cmd_lower:
                    return {
                        "status": "blocked",
                        "code": "family_forbidden_action",
                        "word": word,
                    }

        # OWNER → všetko povolené
        if identity == "OWNER":
            return {"status": "ok"}

        # Neznáma identita
        return {
            "status": "blocked",
            "code": "unknown_identity",
            "identity": identity,
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
        }
