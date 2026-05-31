"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Sandbox for safe module isolation and repair execution.

Účel:
- izolovať poškodený modul
- vytvoriť bezpečné prostredie pre opravy
- zabrániť šíreniu chyby do ostatných modulov
- povoliť iba bezpečné operácie počas opravy
"""

import os
import shutil
from typing import Dict, Any


class RepairSandbox:
    """
    RepairSandbox je ochranná vrstva medzi poškodeným modulom
    a zvyškom systému. Zabezpečuje:

    - izoláciu modulu
    - bezpečné prostredie pre opravy
    - blokovanie nebezpečných operácií
    - návrat modulu po oprave
    """

    def __init__(self, base_path: str, logger):
        """
        base_path – koreňový priečinok runtime (napr. /src)
        logger    – Logging5 / RepairLogs
        """
        self.base_path = base_path
        self.logger = logger
        self.sandbox_root = os.path.join(base_path, "_repair_sandbox")

        # vytvor sandbox ak neexistuje
        os.makedirs(self.sandbox_root, exist_ok=True)

    # ---------------------------------------------------------
    # 1) ISOLATION
    # ---------------------------------------------------------

    def isolate(self, module_name: str) -> bool:
        """
        Izoluje modul tým, že ho presunie do sandboxu.
        Runtime ho prestane používať počas opravy.
        """
        try:
            module_path = os.path.join(self.base_path, module_name)
            sandbox_path = os.path.join(self.sandbox_root, module_name)

            if not os.path.exists(module_path):
                self.logger.warning(f"RepairSandbox: module '{module_name}' not found")
                return False

            # ak už existuje starý sandbox, odstránime ho
            if os.path.exists(sandbox_path):
                shutil.rmtree(sandbox_path)

            shutil.copytree(module_path, sandbox_path)

            self.logger.info(
                "RepairSandbox: module isolated",
                extra={"module": module_name, "sandbox_path": sandbox_path}
            )
            return True

        except Exception as e:
            self.logger.exception("RepairSandbox: isolation failed", extra={"error": str(e)})
            return False

    # ---------------------------------------------------------
    # 2) SAFE EXECUTION ENVIRONMENT
    # ---------------------------------------------------------

    def run_in_sandbox(self, module_name: str, repair_fn, context: Dict[str, Any]) -> bool:
        """
        Spustí opravný proces v sandboxe.
        repair_fn – funkcia, ktorá vykoná opravu
        context   – doplnkové informácie o chybe
        """
        try:
            sandbox_path = os.path.join(self.sandbox_root, module_name)

            if not os.path.exists(sandbox_path):
                self.logger.error("RepairSandbox: sandbox missing")
                return False

            self.logger.info(
                "RepairSandbox: running repair in sandbox",
                extra={"module": module_name}
            )

            # spustíme opravu v izolovanom prostredí
            return repair_fn(sandbox_path, context)

        except Exception as e:
            self.logger.exception("RepairSandbox: repair execution failed", extra={"error": str(e)})
            return False

    # ---------------------------------------------------------
    # 3) RESTORE MODULE
    # ---------------------------------------------------------

    def restore(self, module_name: str) -> bool:
        """
        Po úspešnej oprave presunie sandboxovaný modul späť do runtime.
        """
        try:
            module_path = os.path.join(self.base_path, module_name)
            sandbox_path = os.path.join(self.sandbox_root, module_name)

            if not os.path.exists(sandbox_path):
                self.logger.error("RepairSandbox: cannot restore, sandbox missing")
                return False

            # odstránime pôvodný modul
            if os.path.exists(module_path):
                shutil.rmtree(module_path)

            shutil.copytree(sandbox_path, module_path)

            self.logger.info(
                "RepairSandbox: module restored",
                extra={"module": module_name}
            )
            return True

        except Exception as e:
            self.logger.exception("RepairSandbox: restore failed", extra={"error": str(e)})
            return False

    # ---------------------------------------------------------
    # 4) CLEANUP
    # ---------------------------------------------------------

    def cleanup(self, module_name: str) -> None:
        """
        Odstráni sandbox po úspešnej oprave.
        """
        try:
            sandbox_path = os.path.join(self.sandbox_root, module_name)
            if os.path.exists(sandbox_path):
                shutil.rmtree(sandbox_path)

            self.logger.info(
                "RepairSandbox: cleanup complete",
                extra={"module": module_name}
            )

        except Exception as e:
            self.logger.exception("RepairSandbox: cleanup failed", extra={"error": str(e)})
