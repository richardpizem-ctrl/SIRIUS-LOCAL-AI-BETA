"""
SIRIUS Runtime 5.1.0 – Knowledge Graph Repair Layer 1.0
KG Fallback Minimal Pack 1.0

Účel:
- poskytnúť minimálny, konzistentný KG balík pre fallback režim
- použiť pri:
  - neopraviteľnom poškodení KG
  - zlyhaní globálnej opravy
  - prvotnom štarte po kritickej chybe
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class FallbackPackResult:
    ok: bool
    reason: str
    details: Dict[str, Any]


class KGRepairFallback:
    """
    Fallback vrstva pre Knowledge Graph.

    Poskytuje:
    - minimálny, konzistentný KG balík
    - deterministickú štruktúru
    - žiadne dynamické generovanie obsahu
    """

    def __init__(self, kg_saver, logger):
        """
        kg_saver – komponent, ktorý vie uložiť KG objekt
        logger   – Logging5 / RepairLogger
        """
        self.kg_saver = kg_saver
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def apply_minimal_pack(self) -> FallbackPackResult:
        """
        Nahradí aktuálny KG minimálnym balíkom.
        Používa sa pri:
        - kritickom zlyhaní opravy
        - nevalidnom KG po viacerých pokusoch o opravu
        """
        self.logger.warning("KGRepairFallback: applying minimal KG pack")

        minimal_kg = self._build_minimal_kg()

        try:
            self.kg_saver.save(minimal_kg)
        except Exception as e:
            self.logger.exception(
                "KGRepairFallback: failed to save minimal KG pack",
                extra={"error": str(e)}
            )
            return FallbackPackResult(
                ok=False,
                reason="save_failed",
                details={"error": str(e)}
            )

        return FallbackPackResult(
            ok=True,
            reason="minimal_pack_applied",
            details={"entities": list(minimal_kg.entities.keys())}
        )

    # ---------------------------------------------------------
    # INTERNAL BUILDERS
    # ---------------------------------------------------------

    def _build_minimal_kg(self):
        """
        Vytvorí minimálny, konzistentný KG objekt.

        Očakávané rozhranie:
        - objekt s atribútom .entities (dict)
        - žiadne externé závislosti
        """

        class MinimalKG:
            def __init__(self):
                self.entities: Dict[str, Dict[str, Any]] = {}

        kg = MinimalKG()

        # Minimálna sada entít – len to, čo runtime potrebuje na základný chod.
        kg.entities["core:root"] = {
            "id": "core:root",
            "type": "system_root",
            "relations": [],
        }

        kg.entities["core:health"] = {
            "id": "core:health",
            "type": "system_health",
            "relations": [
                {"target": "core:root", "type": "depends_on"},
            ],
        }

        kg.entities["core:self_repair"] = {
            "id": "core:self_repair",
            "type": "self_repair",
            "relations": [
                {"target": "core:root", "type": "depends_on"},
                {"target": "core:health", "type": "monitors"},
            ],
        }

        return kg
