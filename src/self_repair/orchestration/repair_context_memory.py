"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Context Memory 1.0

Účel:
- uchovávať stav a výsledky posledných opráv
- poskytovať RepairCore konzistentný kontext
- umožniť spätnú diagnostiku a audit
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional


@dataclass
class RepairMemorySnapshot:
    state: str
    last_plan: Optional[Dict[str, Any]] = None
    last_result: Optional[Dict[str, Any]] = None
    last_error: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class RepairContextMemory:
    """
    Pamäťová vrstva pre Self‑Repair.

    Uchováva:
    - posledný stav stavového automatu
    - posledný plán opráv
    - posledný výsledok opravy
    - poslednú chybu
    """

    def __init__(self, logger):
        self.logger = logger
        self.memory = RepairMemorySnapshot(state="IDLE")

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def update_state(self, new_state: str):
        self.logger.info(
            "RepairContextMemory: updating state",
            extra={"from": self.memory.state, "to": new_state}
        )
        self.memory.state = new_state

    def store_plan(self, plan: Dict[str, Any]):
        self.logger.info(
            "RepairContextMemory: storing repair plan",
            extra={"steps": len(plan.get("steps", []))}
        )
        self.memory.last_plan = plan

    def store_result(self, result: Dict[str, Any]):
        self.logger.info(
            "RepairContextMemory: storing repair result",
            extra={"ok": result.get("ok")}
        )
        self.memory.last_result = result

    def store_error(self, error: Dict[str, Any]):
        self.logger.warning(
            "RepairContextMemory: storing repair error",
            extra={"error": error}
        )
        self.memory.last_error = error

    def add_metadata(self, key: str, value: Any):
        self.memory.metadata[key] = value

    # ---------------------------------------------------------
    # RETRIEVAL
    # ---------------------------------------------------------

    def snapshot(self) -> RepairMemorySnapshot:
        """
        Vráti kompletný snapshot pamäte.
        """
        return self.memory

    def clear(self):
        """
        Resetuje pamäť do pôvodného stavu.
        """
        self.logger.info("RepairContextMemory: clearing memory")
        self.memory = RepairMemorySnapshot(state="IDLE")
