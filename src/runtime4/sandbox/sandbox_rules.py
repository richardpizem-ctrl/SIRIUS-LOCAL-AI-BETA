# sandbox_rules.py
"""
SIRIUS LOCAL AI – Runtime 4.0 Sandbox Rules

Defines capability-based security rules for sandboxed modules.
Responsible for:
- allowed and forbidden operations
- capability validation
- rule enforcement
- module security profiles

This is the policy layer of the sandbox system.
"""


class SandboxRules4:
    """
    Defines and validates sandbox capability rules.
    """

    def __init__(self):
        # Capability registry:
        # { "module_name": ["cap_read", "cap_write", ...] }
        self.capabilities = {}

        # Forbidden operations (global)
        self.forbidden_ops = [
            "network_access",
            "filesystem_write_outside_scope",
            "execute_external_code",
            "spawn_untrusted_process"
        ]

    # ---------------------------------------------------------
    # CAPABILITY MANAGEMENT
    # ---------------------------------------------------------

    def set_capabilities(self, module_name: str, caps: list):
        """Assigns capabilities to a module."""
        self.capabilities[module_name] = caps

    def get_capabilities(self, module_name: str):
        """Returns capabilities assigned to a module."""
        return self.capabilities.get(module_name, [])

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def is_allowed(self, module_name: str, operation: str) -> bool:
        """
        Checks if a module is allowed to perform an operation.
        """
        # Forbidden globally
        if operation in self.forbidden_ops:
            return False

        # Must be explicitly allowed
        caps = self.capabilities.get(module_name, [])
        return operation in caps

    def validate_operation(self, module_name: str, operation: str):
        """
        Returns a structured validation result.
        """
        if self.is_allowed(module_name, operation):
            return {"allowed": True}

        return {
            "allowed": False,
            "error": "operation_not_permitted",
            "module": module_name,
            "operation": operation
        }
