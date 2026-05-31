"""
SIRIUS Runtime 5.1.0 – KG Repair Layer
KG Repair Validator 1.0

Wrapper nad Integrity Validator 3.1.
"""

from dataclasses import dataclass
from typing import Dict, Any
from kg.integrity.integrity_3_1 import IntegrityValidator31


@dataclass
class KGRepairValidationResult:
    ok: bool
    issues: list
    details: Dict[str, Any]


class KGRepairValidator:
    """
    Jednoduchý wrapper, ktorý spúšťa Integrity 3.1
    a poskytuje výsledky pre opravné moduly.
    """

    def __init__(self, logger):
        self.logger = logger
        self.validator = IntegrityValidator31(logger)

    def validate(self, kg) -> KGRepairValidationResult:
        result = self.validator.validate(kg)

        return KGRepairValidationResult(
            ok=result.ok,
            issues=result.issues,
            details=result.details
        )
