"""
SIRIUS Runtime 5.1.0
Repair Entrypoint – spúšťač Self‑Repair Layer 1.0

Účel:
- poskytnúť jednotný vstupný bod pre spustenie Self‑Repair cyklu
- používa sa RuntimeCore, HealthMonitor, SystemAgent alebo manuálne
"""

from typing import Dict, Any


class RepairEntrypoint:
    """
    RepairEntrypoint – jednoduchý wrapper nad RepairCore.

    Očakávané závislosti (dependency injection):
        repair_core – RepairCore (API: run_repair_cycle())
        logger      – Logging5 / RuntimeLogger
    """

    def __init__(self, repair_core, logger):
        self.repair_core = repair_core
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def run(self) -> Dict[str, Any]:
        """
        Spustí jeden Self‑Repair cyklus a vráti výsledok ako dict.
        Toto je najjednoduchší spôsob, ako spustiť opravu z Runtime5.
        """
        self.logger.info("RepairEntrypoint: triggering Self‑Repair cycle")

        result = self.repair_core.run_repair_cycle()

        output = {
            "ok": result.ok,
            "final_state": result.details.get("final_state"),
            "stages": result.stages,
        }

        self.logger.info(
            "RepairEntrypoint: repair cycle finished",
            extra={"ok": output["ok"], "final_state": output["final_state"]},
        )

        return output
