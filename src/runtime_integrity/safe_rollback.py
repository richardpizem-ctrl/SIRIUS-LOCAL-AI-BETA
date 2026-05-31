"""
SIRIUS Runtime 5.1.0 – Runtime Integrity Engine 1.0
Safe Rollback 1.0

Účel:
- bezpečný návrat k poslednej zdravej verzii modulu
- používa sa pri zlyhanej oprave alebo neplatnej integrite
- spolupracuje so Self‑Repair Layer a Integrity Engine
"""

import os
import shutil
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class RollbackResult:
    ok: bool
    reason: str
    details: Dict[str, Any]


class SafeRollback:
    """
    Bezpečný rollback pre runtime moduly.

    Pracuje s jednoduchým modelom:
    - každý modul môže mať uloženú "healthy" verziu v backup priečinku
    - rollback = nahradenie aktuálnej verzie tou z backupu
    """

    def __init__(self, base_path: str, backup_root: str, logger):
        """
        base_path   – koreň runtime (napr. /src)
        backup_root – priečinok, kde sú uložené zdravé verzie modulov
        logger      – Logging5 / RepairLogger
        """
        self.base_path = base_path
        self.backup_root = backup_root
        self.logger = logger

        os.makedirs(self.backup_root, exist_ok=True)

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def create_backup(self, module_rel_path: str) -> RollbackResult:
        """
        Vytvorí backup aktuálnej verzie modulu.
        Volá sa pri:
        - nasadení novej verzie
        - úspešnej oprave
        """
        module_path = os.path.join(self.base_path, module_rel_path)
        backup_path = os.path.join(self.backup_root, module_rel_path)

        if not os.path.exists(module_path):
            return RollbackResult(
                ok=False,
                reason="module_not_found",
                details={"module": module_rel_path}
            )

        try:
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)

            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            shutil.copytree(module_path, backup_path)

            self.logger.info(
                "SafeRollback: backup created",
                extra={"module": module_rel_path, "backup_path": backup_path}
            )

            return RollbackResult(
                ok=True,
                reason="backup_created",
                details={"module": module_rel_path, "backup_path": backup_path}
            )

        except Exception as e:
            self.logger.exception(
                "SafeRollback: backup failed",
                extra={"module": module_rel_path, "error": str(e)}
            )
            return RollbackResult(
                ok=False,
                reason="backup_failed",
                details={"module": module_rel_path, "error": str(e)}
            )

    def rollback(self, module_rel_path: str) -> RollbackResult:
        """
        Vykoná rollback modulu na poslednú zdravú verziu.
        Použitie:
        - po zlyhanej oprave
        - po neúspešnej verifikácii integrity
        """
        module_path = os.path.join(self.base_path, module_rel_path)
        backup_path = os.path.join(self.backup_root, module_rel_path)

        if not os.path.exists(backup_path):
            self.logger.error(
                "SafeRollback: no backup available",
                extra={"module": module_rel_path}
            )
            return RollbackResult(
                ok=False,
                reason="no_backup",
                details={"module": module_rel_path}
            )

        try:
            # odstránime aktuálny (potenciálne poškodený) modul
            if os.path.exists(module_path):
                shutil.rmtree(module_path)

            # obnovíme z backupu
            os.makedirs(os.path.dirname(module_path), exist_ok=True)
            shutil.copytree(backup_path, module_path)

            self.logger.info(
                "SafeRollback: rollback completed",
                extra={"module": module_rel_path}
            )

            return RollbackResult(
                ok=True,
                reason="rollback_success",
                details={"module": module_rel_path}
            )

        except Exception as e:
            self.logger.exception(
                "SafeRollback: rollback failed",
                extra={"module": module_rel_path, "error": str(e)}
            )
            return RollbackResult(
                ok=False,
                reason="rollback_failed",
                details={"module": module_rel_path, "error": str(e)}
            )
