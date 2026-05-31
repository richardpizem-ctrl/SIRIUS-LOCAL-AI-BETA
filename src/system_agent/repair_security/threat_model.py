"""
SIRIUS Runtime 5.1.0 – System Agent Security
Threat Model 1.0
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ThreatEvaluation:
    level: str  # LOW / MEDIUM / HIGH
    details: Dict[str, Any]


class ThreatModel:
    """
    Jednoduchý deterministický Threat Model.
    """

    HIGH_RISK = {"exec", "file_delete", "network_access"}
    MEDIUM_RISK = {"file_write", "modify_config"}

    def evaluate(self, operation: str) -> ThreatEvaluation:
        if operation in self.HIGH_RISK:
            return ThreatEvaluation(level="HIGH", details={"operation": operation})

        if operation in self.MEDIUM_RISK:
            return ThreatEvaluation(level="MEDIUM", details={"operation": operation})

        return ThreatEvaluation(level="LOW", details={"operation": operation})
