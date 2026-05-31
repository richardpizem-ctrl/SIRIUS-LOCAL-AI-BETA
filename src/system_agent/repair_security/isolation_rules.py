"""
SIRIUS Runtime 5.1.0 – System Agent Security
Isolation Rules 1.0
"""

class IsolationRules:
    """
    Pravidlá izolácie pre sandboxované opravy.
    """

    ALLOWED_PATHS = [
        "data/kg/",
        "data/cache/",
        "runtime/tmp/",
    ]

    BLOCKED_OPERATIONS = {
        "delete_system_file",
        "modify_runtime_core",
        "network_access",
    }

    def is_operation_allowed(self, module: str, operation: str) -> bool:
        return operation not in self.BLOCKED_OPERATIONS

    def is_path_allowed(self, path: str) -> bool:
        return any(path.startswith(p) for p in self.ALLOWED_PATHS)
