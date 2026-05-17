"""
SIRIUS LOCAL AI – Runtime 4.3 Sandbox Process

The Sandbox Process simulates an isolated execution environment.
It is responsible for:
- holding execution context
- processing inputs and outputs
- enforcing isolation boundaries
- communicating with the Sandbox Manager
- preparing for capability-based restrictions
- supporting safe-mode and degraded-mode behavior

This is the low-level execution layer of the sandbox system.
"""

from typing import Optional, Dict, Any


class SandboxProcess4:
    """
    Represents a single sandboxed execution process.
    Provides:
    - strict isolation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, module_name: str):
        # Validate module name
        if not isinstance(module_name, str) or not module_name.strip():
            raise ValueError("Invalid module_name: must be a non-empty string.")

        self.module_name = module_name
        self.context: Dict[str, Any] = {}
        self.active = True
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # CONTEXT MANAGEMENT
    # ---------------------------------------------------------

    def set_context(self, key: str, value):
        """Stores a value inside the sandbox context with safety checks."""

        if not isinstance(key, str) or not key.strip():
            return {"status": "error", "code": "invalid_context_key"}

        # Prevent storing dangerous types
        if isinstance(value, (type(lambda: None), type(self.set_context))):
            return {"status": "error", "code": "invalid_context_value_type"}

        try:
            self.context[key] = value
            return {"status": "success"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "context_set_failed",
                "exception": str(exc)
            }

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
        This is a placeholder — real logic is injected by the runtime.
        """

        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Sandbox execution disabled in safe-mode."
            }

        # Sandbox must be active
        if not self.active:
            return {"status": "error", "code": "sandbox_inactive"}

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"status": "error", "code": "invalid_task"}

        # Validate payload
        if payload is not None and not isinstance(payload, dict):
            return {"status": "error", "code": "invalid_payload_type"}

        try:
            return {
                "status": "executed_in_sandbox",
                "module": self.module_name,
                "task": task,
                "payload": payload or {},
                "degraded_mode": self.degraded_mode
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "execution_failed",
                "exception": str(exc)
            }

    # ---------------------------------------------------------
    # LIFECYCLE
    # ---------------------------------------------------------

    def shutdown(self):
        """Shuts down the sandbox process."""
        self.active = False
        return {"status": "sandbox_shutdown"}
