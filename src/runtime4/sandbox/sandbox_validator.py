"""
SIRIUS LOCAL AI – Runtime 4.0 Sandbox Validator

Responsible for:
- validating sandbox context
- checking capability permissions
- enforcing sandbox rules
- ensuring safe execution conditions
- preventing unsafe operations

This is the validation layer of the sandbox system.
"""

from typing import Optional


class SandboxValidator4:
    """
    Validates sandbox operations before execution.
    """

    def __init__(self, rules):
        # Basic safety check for rules object (duck-typing)
        if rules is None or not hasattr(rules, "validate_operation"):
            raise ValueError("Invalid rules object for SandboxValidator4.")
        self.rules = rules

    # ---------------------------------------------------------
    # CONTEXT VALIDATION
    # ---------------------------------------------------------

    def validate_context(self, context: Optional[dict]):
        """Checks if sandbox context is valid and active."""

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

    def validate_operation(self, module_name: str, operation: str):
        """
        Validates if a module is allowed to perform an operation.
        Delegates to SandboxRules4 with safety checks.
        """

        # Validate module_name
        if not isinstance(module_name, str) or not module_name.strip():
            return {
                "allowed": False,
                "error": "invalid_module_name"
            }

        # Validate operation
        if not isinstance(operation, str) or not operation.strip():
            return {
                "allowed": False,
                "error": "invalid_operation"
            }

        # Delegate to rules
        return self.rules.validate_operation(module_name, operation)

    # ---------------------------------------------------------
    # FULL VALIDATION
    # ---------------------------------------------------------

    def validate(self, module_name: str, context: Optional[dict], operation: str):
        """
        Performs full validation:
        - context check
        - capability check
        - forbidden operation check
        """

        # Context validation
        ctx_check = self.validate_context(context)
        if not ctx_check["allowed"]:
            return ctx_check

        # Operation validation
        op_check = self.validate_operation(module_name, operation)
        if not op_check["allowed"]:
            return op_check

        return {"allowed": True}
