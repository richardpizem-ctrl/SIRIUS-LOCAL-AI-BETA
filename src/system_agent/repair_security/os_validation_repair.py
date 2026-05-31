"""
SIRIUS Runtime 5.1.0 – System Agent 5.1
OS Validation Repair 1.0

Účel:
- validovať OS prostredie pre SIRIUS Runtime
- detegovať poškodené alebo nebezpečné systémové nastavenia
- vykonať bezpečné, reverzibilné opravy (bez zásahu do OS jadra)
- poskytovať Self‑Repair Layeru diagnostiku a návrhy opráv
"""

from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class OSRepairResult:
    ok: bool
    repaired: List[str]
    warnings: List[str]
    details: Dict[str, Any]


class OSValidationRepair:
    """
    Opravný modul pre OS-level validáciu.

    Kontroluje:
    - PATH integritu
    - prístupové práva k runtime priečinkom
    - dostupnosť systémových knižníc
    - bezpečnostné obmedzenia (sandbox, permissions)
    """

    REQUIRED_PATHS = [
        "/usr/bin",
        "/usr/local/bin",
    ]

    REQUIRED_LIBS = [
        "libc",
        "libm",
    ]

    def __init__(self, os_api, logger):
        """
        os_api – abstrakcia nad OS (filesystem, permissions, env)
        logger – Logging5 / RepairLogger
        """
        self.os = os_api
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def validate_and_repair(self) -> OSRepairResult:
        """
        Hlavná funkcia:
        - validuje OS prostredie
        - pokúsi sa opraviť drobné problémy
        - vráti diagnostiku pre Self‑Repair Layer
        """
        repaired = []
        warnings = []

        self.logger.info("OSValidationRepair: starting OS validation")

        # 1) PATH integrity
        path_ok, missing_paths = self._check_path_integrity()
        if not path_ok:
            fixed = self._repair_path(missing_paths)
            if fixed:
                repaired.append("PATH")
            else:
                warnings.append("PATH_unrepairable")

        # 2) library availability
        libs_ok, missing_libs = self._check_required_libs()
        if not libs_ok:
            warnings.append(f"missing_libs: {missing_libs}")

        # 3) permissions
        perm_ok, perm_issues = self._check_permissions()
        if not perm_ok:
            fixed = self._repair_permissions(perm_issues)
            if fixed:
                repaired.append("permissions")
            else:
                warnings.append("permissions_unrepairable")

        # výsledok
        ok = not warnings

        self.logger.info(
            "OSValidationRepair: validation finished",
            extra={"ok": ok, "repaired": repaired, "warnings": warnings}
        )

        return OSRepairResult(
            ok=ok,
            repaired=repaired,
            warnings=warnings,
            details={
                "missing_paths": missing_paths,
                "missing_libs": missing_libs,
                "permission_issues": perm_issues,
            }
        )

    # ---------------------------------------------------------
    # INTERNAL CHECKS
    # ---------------------------------------------------------

    def _check_path_integrity(self):
        missing = []
        for p in self.REQUIRED_PATHS:
            if not self.os.path_exists(p):
                missing.append(p)
        return (len(missing) == 0, missing)

    def _check_required_libs(self):
        missing = []
        for lib in self.REQUIRED_LIBS:
            if not self.os.library_available(lib):
                missing.append(lib)
        return (len(missing) == 0, missing)

    def _check_permissions(self):
        issues = self.os.check_runtime_permissions()
        return (len(issues) == 0, issues)

    # ---------------------------------------------------------
    # INTERNAL REPAIRS
    # ---------------------------------------------------------

    def _repair_path(self, missing_paths: List[str]) -> bool:
        """
        Pokus o doplnenie chýbajúcich PATH položiek.
        """
        try:
            for p in missing_paths:
                self.os.add_to_path(p)
            return True
        except Exception as e:
            self.logger.exception(
                "OSValidationRepair: failed to repair PATH",
                extra={"error": str(e)}
            )
            return False

    def _repair_permissions(self, issues: List[str]) -> bool:
        """
        Pokus o opravu prístupových práv.
        """
        try:
            for issue in issues:
                self.os.fix_permission(issue)
            return True
        except Exception as e:
            self.logger.exception(
                "OSValidationRepair: failed to repair permissions",
                extra={"error": str(e)}
            )
            return False
