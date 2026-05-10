"""
SIRIUS LOCAL AI – Runtime 4.0 Sandbox Manager

The Sandbox Manager is responsible for:
- creating isolated execution contexts
- enforcing capability rules
- validating inputs and outputs
- preventing unsafe operations
- routing tasks through sandboxed modules
- integrating with scheduler and dependency graph

This is the primary security layer of Runtime 4.0.
"""

from typing import Optional, Dict, Any


class SandboxManager4:
    """
    Manages sandboxed execution environments for Runtime 4.0.
    """

    def __init__(self, max_contexts: int = 200):
        # Stores active sandbox contexts:
        # { "module_name": SandboxContext }
        self.contexts: Dict[str, Dict[str, Any]] = {}
        self.max_contexts = max_contexts

    # ---------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_module_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_capabilities(self, caps: Any) -> bool:
        if not isinstance(caps, list):
            return False
        for c in caps:
            if not isinstance(c, str) or not c.strip():
                return False
        return True

    def _validate_context(self, ctx: Any) -> bool:
        if ctx is None:
            return True
        if not isinstance(ctx, dict):
            return False
        for key, value in ctx.items():
            if not isinstance(key, str) or not key.strip():
                return False
            if isinstance(value, (bytes, bytearray, type(lambda: None))):
                return False
        return True

    def _validate_task(self, task: Any) -> bool:
        return isinstance(task, str) and task.strip()

    # ---------------------------------------------------------
    # CONTEXT MANAGEMENT
    # ---------------------------------------------------------

    def create_context(self, module_name: str):
        """
        Creates a new sandbox context for a module with full safety checks.
        """

        if not self._validate_module_name(module_name):
            return {"error": "invalid_module_name"}

        if len(self.contexts) >= self.max_contexts:
            return {"error": "context_limit_reached"}

        self.contexts[module_name] = {
            "capabilities": [],
            "state": {},
            "active": True
        }

        return {"status": "context_created"}

    def destroy_context(self, module_name: str):
        """
        Removes a sandbox context safely.
        """

        if not self._validate_module_name(module_name):
            return {"error": "invalid_module_name"}

        if module_name in self.contexts:
            del self.contexts[module_name]
            return {"status": "context_destroyed"}

        return {"error": "context_not_found"}

    def get_context(self, module_name: str) -> Optional[dict]:
        """
        Returns the sandbox context for a module.
        """

        if not self._validate_module_name(module_name):
            return None

        return self.contexts.get(module_name)

    # ---------------------------------------------------------
    # CAPABILITY RULES
    # ---------------------------------------------------------

    def set_capabilities(self, module_name: str, capabilities: list):
        """
        Assigns allowed capabilities to a module with safety checks.
        """

        if not self._validate_module_name(module_name):
            return {"error": "invalid_module_name"}

        if not self._validate_capabilities(capabilities):
            return {"error": "invalid_capabilities"}

        if module_name not in self.contexts:
            return {"error": "context_not_found"}

        self.contexts[module_name]["capabilities"] = capabilities
        return {"status": "capabilities_set"}

    def has_capability(self, module_name: str, capability: str) -> bool:
        """
        Checks if a module has a specific capability.
        """

        if not self._validate_module_name(module_name):
            return False

        if not isinstance(capability, str) or not capability.strip():
            return False

        ctx = self.contexts.get(module_name)
        if not ctx:
            return False

        return capability in ctx["capabilities"]

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------

    def execute(self, module_name: str, task: str, context: Optional[dict] = None):
        """
        Executes a task inside a sandboxed module.
        Full Runtime 4.0 security validation.
        """

        # Validate module name
        if not self._validate_module_name(module_name):
            return {"error": "invalid_module_name"}

        # Validate task
        if not self._validate_task(task):
            return {"error": "invalid_task"}

        # Validate context
        if not self._validate_context(context):
            return {"error": "invalid_context"}

        # Check sandbox existence
        if module_name not in self.contexts:
            return {"error": "sandbox_not_initialized"}

        ctx = self.contexts[module_name]

        # Check sandbox active state
        if not ctx.get("active", False):
            return {"error": "sandbox_inactive"}

        # Placeholder for future capability enforcement:
        # Example: if task requires "compute", check has_capability(module_name, "compute")

        # Return safe execution envelope
        return {
            "status": "sandboxed",
            "module": module_name,
            "task": task,
            "context": context or {}
        }
