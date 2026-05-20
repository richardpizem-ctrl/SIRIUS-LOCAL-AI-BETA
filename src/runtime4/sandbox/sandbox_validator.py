"""
SIRIUS LOCAL AI – Runtime 4.4 Sandbox Validator (PRO)

Responsible for:
- validating sandbox context
- checking capability permissions
- enforcing sandbox rules
- ensuring safe execution conditions
- preventing unsafe operations

Security Family 4.4 Compliance:
- No eval, exec, reflection, dynamic imports
- Strict input validation
- Deterministic behavior
- Self‑Repair 4.4 ready
"""

from typing import Optional, Dict, Any


class SandboxValidator4:
    """
    Validates sandbox operations before execution (PRO).
    """

    def __init__(self, rules):
        # Basic safety check for rules object (duck-typing)
        if rules is None or not hasattr(rules, "validate_operation"):
            raise ValueError("Invalid rules object for SandboxValidator4.")

        self.rules = rules
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # CONTEXT VALIDATION
    # ---------------------------------------------------------

    def validate_context(self, context: Optional[dict]) -> Dict[str, Any]:
        """Checks if sandbox context is valid and active."""

        if self.safe_mode:
            return {"allowed": False, "error": "safe_mode"}

        # Context must exist
        if context is None:
            return {"allowed": False, "error": "context_missing"}

        # Context must be a dict
        if not isinstance(context, dict):
            return {"allowed": False, "error": "invalid_context_type"}

        # Active flag
        active = context.get("active", True)
        if not isinstance(active, bool):
            return {"allowed": False, "error": "invalid_active_flag"}

        if not active:
            return {"allowed": False, "error": "context_inactive"}

        return {"allowed": True}

    # ---------------------------------------------------------
    # OPERATION VALIDATION
    # ---------------------------------------------------------

    def validate_operation(self, module_name: str, operation: str) -> Dict[str, Any]:
        """
        Validates if a module is allowed to perform an operation.
        Delegates to SandboxRules4 with safety checks.
        """

        if self.safe_mode:
            return {"allowed": False, "error": "safe_mode"}

        # Validate module_name
        if not isinstance(module_name, str) or not module_name.strip():
            return {"allowed": False, "error": "invalid_module_name"}

        # Validate operation
        if not isinstance(operation, str) or not operation.strip():
            return {"allowed": False, "error": "invalid_operation"}

        # Delegate to rules
        try:
            return self.rules.validate_operation(module_name, operation)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "allowed": False,
                "error": "rule_validation_failed",
                "exception": str(exc),
            }

    # ---------------------------------------------------------
    # FULL VALIDATION
    # ---------------------------------------------------------

    def validate(self, module_name: str, context: Optional[dict], operation: str) -> Dict[str, Any]:
        """
        Performs full validation:
        - context check
        - capability check
        - forbidden operation check
        """

        if self.safe_mode:
            return {"allowed": False, "error": "safe_mode"}

        # Context validation
        ctx_check = self.validate_context(context)
        if not ctx_check.get("allowed", False):
            return ctx_check

        # Operation validation
        op_check = self.validate_operation(module_name, operation)
        if not op_check.get("allowed", False):
            return op_check

        return {
            "allowed": True,
            "degraded_mode": self.degraded_mode,
        }
