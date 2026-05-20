"""
SIRIUS LOCAL AI – Runtime 4.3 Sandbox Rules (PRO)

Defines capability-based security rules for sandboxed modules.
Responsible for:
- allowed and forbidden operations
- capability validation
- rule enforcement
- module security profiles
- safe-mode and degraded-mode behavior
- compatibility with Security Family 4.4

This is the policy layer of the sandbox system.
"""


class SandboxRules4:
    """
    Deterministic capability rule engine (PRO).
    Provides:
    - strict capability validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
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
            "spawn_untrusted_process",
        ]

        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # CAPABILITY MANAGEMENT
    # ---------------------------------------------------------

    def set_capabilities(self, module_name: str, caps: list):
        """Assigns capabilities to a module with full safety checks."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Capability assignment disabled in safe-mode.",
            }

        # Validate module name
        if not isinstance(module_name, str) or not module_name.strip():
            return {"status": "error", "code": "invalid_module_name"}

        # Validate caps list
        if not isinstance(caps, list):
            return {"status": "error", "code": "invalid_capability_list"}

        # Validate each capability
        for cap in caps:
            if not isinstance(cap, str) or not cap.strip():
                return {"status": "error", "code": "invalid_capability_value"}

        try:
            self.capabilities[module_name] = caps
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "capability_assignment_failed",
                "exception": str(exc),
            }

    def get_capabilities(self, module_name: str):
        """Returns capabilities assigned to a module."""
        if not isinstance(module_name, str):
            return []
        return self.capabilities.get(module_name, [])

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def is_allowed(self, module_name: str, operation: str) -> bool:
        """
        Checks if a module is allowed to perform an operation.
        Includes full validation and safety checks.
        """

        # Validate module name
        if not isinstance(module_name, str) or not module_name.strip():
            return False

        # Validate operation
        if not isinstance(operation, str) or not operation.strip():
            return False

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

        # SAFE MODE
        if self.safe_mode:
            return {
                "allowed": False,
                "error": "safe_mode",
                "message": "Operation validation disabled in safe-mode.",
            }

        # Validate module name
        if not isinstance(module_name, str) or not module_name.strip():
            return {"allowed": False, "error": "invalid_module_name"}

        # Validate operation
        if not isinstance(operation, str) or not operation.strip():
            return {"allowed": False, "error": "invalid_operation"}

        # Check permission
        if self.is_allowed(module_name, operation):
            return {
                "allowed": True,
                "degraded_mode": self.degraded_mode,
            }

        return {
            "allowed": False,
            "error": "operation_not_permitted",
            "module": module_name,
            "operation": operation,
            "degraded_mode": self.degraded_mode,
        }
