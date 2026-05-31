"""
SIRIUS Runtime 5.1.0 – System Agent 5.1
Sandbox Enforcement 1.0

Účel:
- presadzovať bezpečnostné pravidlá pre Self‑Repair Layer
- blokovať rizikové operácie v sandboxe
- validovať operácie podľa ThreatModel a IsolationRules
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class EnforcementResult:
    allowed: bool
    reason: str
    details: Dict[str, Any]


class SandboxEnforcement:
    """
    Enforcement vrstva pre sandboxované opravy.

    Spolupracuje s:
    - RepairPermissions
    - IsolationRules
    - ThreatModel
    """

    def __init__(self, permissions, isolation_rules, threat_model, logger):
        """
        permissions      – RepairPermissions
        isolation_rules  – IsolationRules
        threat_model     – ThreatModel
        logger           – Logging5 / RepairLogger
        """
        self.permissions = permissions
        self.isolation = isolation_rules
        self.threat = threat_model
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def validate_operation(self, module: str, operation: str, context: Dict[str, Any]) -> EnforcementResult:
        """
        Overí, či Self‑Repair môže vykonať danú operáciu.

        Kontroluje:
        1) oprávnenia identity
        2) izoláciu modulu
        3) rizikovosť operácie (ThreatModel)
        """
        self.logger.info(
            "SandboxEnforcement: validating operation",
            extra={"module": module, "operation": operation}
        )

        # 1) identity permissions
        perm = self.permissions.can_repair(module, context)
        if not perm.allowed:
            return EnforcementResult(
                allowed=False,
                reason="permission_denied",
                details={"module": module, "operation": operation, "perm_reason": perm.reason}
            )

        # 2) isolation rules
        if not self.isolation.is_operation_allowed(module, operation):
            return EnforcementResult(
                allowed=False,
                reason="blocked_by_isolation_rules",
                details={"module": module, "operation": operation}
            )

        # 3) threat model
        threat = self.threat.evaluate(operation)
        if threat.level == "HIGH":
            return EnforcementResult(
                allowed=False,
                reason="high_risk_operation",
                details={"operation": operation, "threat": threat.details}
            )

        return EnforcementResult(
            allowed=True,
            reason="allowed",
            details={"module": module, "operation": operation}
        )

    # ---------------------------------------------------------
    # SPECIALIZED CHECKS
    # ---------------------------------------------------------

    def validate_file_write(self, module: str, path: str, context: Dict[str, Any]) -> EnforcementResult:
        """
        Overí, či Self‑Repair môže zapisovať do súboru.
        """
        self.logger.info(
            "SandboxEnforcement: validating file write",
            extra={"module": module, "path": path}
        )

        # identity permissions
        if not self.permissions.can_modify_files(module):
            return EnforcementResult(
                allowed=False,
                reason="file_write_not_allowed_for_role",
                details={"module": module, "path": path}
            )

        # isolation rules
        if not self.isolation.is_path_allowed(path):
            return EnforcementResult(
                allowed=False,
                reason="path_blocked_by_isolation",
                details={"path": path}
            )

        # threat model
        threat = self.threat.evaluate("file_write")
        if threat.level == "HIGH":
            return EnforcementResult(
                allowed=False,
                reason="high_risk_file_write",
                details={"path": path, "threat": threat.details}
            )

        return EnforcementResult(
            allowed=True,
            reason="allowed",
            details={"path": path}
        )

    def validate_exec(self, module: str, command: str, context: Dict[str, Any]) -> EnforcementResult:
        """
        Overí, či Self‑Repair môže spustiť externý príkaz.
        """
        self.logger.warning(
            "SandboxEnforcement: exec operation requested",
            extra={"module": module, "command": command}
        )

        # exec je extrémne riziková operácia
        threat = self.threat.evaluate("exec")

        if threat.level != "LOW":
            return EnforcementResult(
                allowed=False,
                reason="exec_blocked",
                details={"command": command, "threat": threat.details}
            )

        return EnforcementResult(
            allowed=True,
            reason="allowed_low_risk_exec",
            details={"command": command}
        )
