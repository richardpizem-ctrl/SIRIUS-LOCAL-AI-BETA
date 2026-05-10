"""
SIRIUS LOCAL AI – Runtime 4.0 Sandbox Process

The Sandbox Process simulates an isolated execution environment.
It is responsible for:
- holding execution context
- processing inputs and outputs
- enforcing isolation boundaries
- communicating with the Sandbox Manager
- preparing for capability-based restrictions

This is the low-level execution layer of the sandbox system.
"""

from typing import Optional


class SandboxProcess4:
    """
    Represents a single sandboxed execution process.
    """

    def __init__(self, module_name: str):
        # Validate module name
        if not isinstance(module_name, str) or not module_name.strip():
            raise ValueError("Invalid module_name: must be a non-empty string.")

        self.module_name = module_name
        self.context = {}
        self.active = True

    # ---------------------------------------------------------
    # CONTEXT MANAGEMENT
    # ---------------------------------------------------------

    def set_context(self, key: str, value):
        """Stores a value inside the sandbox context with safety checks."""

        # Validate key
        if not isinstance(key, str) or not key.strip():
            return {"error": "invalid_context_key"}

        # Prevent storing dangerous types (optional hardening)
        if isinstance(value, (type(lambda: None), type(self.set_context))):
            return {"error": "invalid_context_value_type"}

        self.context[key] = value
        return {"status": "ok"}

    def get_context(self, key: str):
        """Retrieves a value from the sandbox context."""
        if not isinstance(key, str):
            return None
        return self.context.get(key)

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------

    def execute(self, task: str, payload: Optional[dict] = None):
        """
        Executes a task inside the sandbox.
        This is only a placeholder — logic will be added later.
        """

        # Sandbox must be active
        if not self.active:
            return {"error": "sandbox_inactive"}

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"error": "invalid_task"}

        # Validate payload
        if payload is not None and not isinstance(payload, dict):
            return {"error": "invalid_payload_type"}

        return {
            "status": "executed_in_sandbox",
            "module": self.module_name,
            "task": task,
            "payload": payload or {}
        }

    # ---------------------------------------------------------
    # LIFECYCLE
    # ---------------------------------------------------------

    def shutdown(self):
        """Shuts down the sandbox process."""
        self.active = False
        return {"status": "sandbox_shutdown"}
