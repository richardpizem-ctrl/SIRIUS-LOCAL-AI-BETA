"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Context Memory 1.0

Účel:
- držať všetky informácie o opravnom procese
- poskytovať jednotný zdroj pravdy pre RepairCore, Planner, StateMachine
- ukladať metadáta o module, chybe, severity, runtime stave
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import time


@dataclass
class RepairContext:
    """
    Centrálna pamäť pre jeden opravný cyklus.
    """
    module: str
    error_code: str
    severity: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    # automaticky doplnené
    timestamp_start: float = field(default_factory=time.time)
    timestamp_end: Optional[float] = None
    repair_attempts: int = 0
    degraded_mode: bool = False
    repair_notes: Dict[str, Any] = field(default_factory=dict)

    def add_note(self, key: str, value: Any) -> None:
        """
        Uloží doplnkovú informáciu počas opravy.
        """
        self.repair_notes[key] = value

    def mark_degraded(self) -> None:
        """
        Označí, že systém prešiel do degradovaného režimu.
        """
        self.degraded_mode = True

    def finish(self) -> None:
        """
        Označí koniec opravného procesu.
        """
        self.timestamp_end = time.time()

    def duration(self) -> float:
        """
        Trvanie opravného procesu v sekundách.
        """
        if self.timestamp_end is None:
            return time.time() - self.timestamp_start
        return self.timestamp_end - self.timestamp_start


class RepairContextMemory:
    """
    Správca kontextov pre Self‑Repair Layer.

    - vytvára nový kontext
    - ukladá ho počas celého procesu
    - poskytuje ho ostatným modulom
    """

    def __init__(self, logger):
        self.logger = logger
        self.current_context: Optional[RepairContext] = None

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def create(self, module: str, error_code: str, severity: str, metadata: Dict[str, Any]) -> RepairContext:
        """
        Vytvorí nový opravný kontext.
        """
        ctx = RepairContext(
            module=module,
            error_code=error_code,
            severity=severity,
            metadata=metadata
        )
        self.current_context = ctx

        self.logger.info(
            "RepairContextMemory: new context created",
            extra={"module": module, "error_code": error_code, "severity": severity}
        )

        return ctx

    def get(self) -> Optional[RepairContext]:
        """
        Vráti aktuálny kontext.
        """
        return self.current_context

    def clear(self) -> None:
        """
        Vymaže kontext po dokončení opravy.
        """
        if self.current_context:
            self.logger.info(
                "RepairContextMemory: clearing context",
                extra={"module": self.current_context.module}
            )
        self.current_context = None
