# sandbox_validator.py
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
        # rules = instance of SandboxRules4
        self.rules = rules

    # ---------------------------------------------------------
    # CONTEXT VALIDATION
    # ---------------------------------------------------------

    def validate_context(self, context: Optional[dict]):
        """Checks if sandbox context is valid and active."""
        if context is None:
            return {"allowed": False, "error": "context_missing"}

        if not context.get("active", True):
            return {"allowed": False, "error": "context_inactive"}

        return {"allowed": True}

    # ---------------------------------------------------------
    # OPERATION VALIDATION
    # ---------------------------------------------------------

    def validate_operation(self, module_name: str, operation: str):
        """
        Validates if a module is allowed to perform an operation.
        Delegates to SandboxRules4.
        """
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
        ctx_check = self.validate_context(context)
        if not ctx_check["allowed"]:
            return ctx_check

        op_check = self.validate_operation(module_name, operation)
        if not op_check["allowed"]:
            return op_check

        return {"allowed": True}
