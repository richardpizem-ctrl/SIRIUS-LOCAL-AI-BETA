"""
SIRIUS Runtime 5.1.0 – System Agent 5.1
Repair Permissions 1.0

Účel:
- kontrola oprávnení pre Self‑Repair Layer
- ochrana pred neautorizovanými opravami
- integrácia s identity modelom System Agent 5.1
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class PermissionCheckResult:
    allowed: bool
    reason: str
    details: Dict[str, Any]


class RepairPermissions:
    """
    Bezpečnostná brána pre Self‑Repair Layer.

    Identity model (System Agent 5.1):
    - OWNER      → plný prístup
    - FAMILY     → obmedzené opravy (bez zásahu do kritických modulov)
    - STRANGER   → žiadne opravy
    """

    CRITICAL_MODULES = {
        "runtime_core",
        "system_agent",
        "security_layer",
        "self_repair",
    }

    def __init__(self, identity_provider, logger):
        """
        identity_provider – poskytuje identity.current_role()
        logger            – Logging5 / RepairLogger
        """
        self.identity = identity_provider
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def can_repair(self, module: str, context: Dict[str, Any]) -> PermissionCheckResult:
        """
        Overí, či aktuálna identita môže opravovať daný modul.
        """
        role = self.identity.current_role()

        self.logger.info(
            "RepairPermissions: checking permissions",
            extra={"role": role, "module": module}
        )

        # OWNER → všetko povolené
        if role == "OWNER":
            return PermissionCheckResult(
                allowed=True,
                reason="owner_full_access",
                details={"role": role, "module": module}
            )

        # STRANGER → nič nepovolené
        if role == "STRANGER":
            return PermissionCheckResult(
                allowed=False,
                reason="stranger_no_access",
                details={"role": role, "module": module}
            )

        # FAMILY → obmedzené opravy
        if role == "FAMILY":
            if module in self.CRITICAL_MODULES:
                return PermissionCheckResult(
                    allowed=False,
                    reason="family_blocked_critical_module",
                    details={"role": role, "module": module}
                )
            return PermissionCheckResult(
                allowed=True,
                reason="family_limited_access",
                details={"role": role, "module": module}
            )

        # fallback – neznáma rola
        return PermissionCheckResult(
            allowed=False,
            reason="unknown_role",
            details={"role": role, "module": module}
        )

    # ---------------------------------------------------------
    # SPECIAL RULES
    # ---------------------------------------------------------

    def can_modify_files(self, module: str) -> bool:
        """
        Opravy, ktoré menia súbory, sú povolené iba OWNERovi.
        """
        role = self.identity.current_role()

        if role == "OWNER":
            return True

        if role == "FAMILY":
            # FAMILY môže opravovať iba nekritické moduly bez zásahu do súborov
            return module not in self.CRITICAL_MODULES

        return False

    def can_trigger_global_repair(self) -> bool:
        """
        Globálna oprava (celý runtime) je extrémne citlivá.
        Povolené iba OWNERovi.
        """
        return self.identity.current_role() == "OWNER"
