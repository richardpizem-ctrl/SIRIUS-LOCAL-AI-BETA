"""
SIRIUS LOCAL AI – Runtime 4.5 Sandbox Context (PRO)

The Sandbox Context stores:
- isolated module state
- capability profile
- runtime metadata
- execution flags
- safe-mode and degraded-mode indicators
- deterministic, offline-only behavior

Security Family 4.5 Compliance:
- No eval, exec, reflection, or dynamic imports
- Strict input validation
- Deterministic state transitions
- Self‑Repair 4.5 ready
"""


class SandboxContext45:
    """
    Deterministic sandbox context for isolated module execution.
    Provides:
    - strict state isolation
    - capability enforcement
    - structured metadata
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, module_name: str):
        # Validate module name
        if not isinstance(module_name, str) or not module_name.strip():
            raise ValueError("Invalid module name for SandboxContext45.")

        self.module_name = module_name

        # Isolated state for the module
        self.state = {}

        # Capabilities assigned to this module
        self.capabilities = []

        # Metadata (timestamps, flags, etc.)
        self.metadata = {
            "active": True,
            "initialized": False,
            "safe_mode": False,
            "degraded_mode": False,
        }

    # ---------------------------------------------------------
    # STATE MANAGEMENT
    # ---------------------------------------------------------

    def set_state(self, key: str, value):
        """Stores a value in the sandbox state."""
        if not isinstance(key, str) or not key.strip():
            return {"status": "error", "code": "invalid_state_key", "version": "4.5"}

        try:
            self.state[key] = value
            return {"status": "ok", "version": "4.5"}
        except Exception as exc:
            self.metadata["degraded_mode"] = True
            return {
                "status": "error",
                "code": "state_set_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    def get_state(self, key: str):
        """Retrieves a value from the sandbox state."""
        if not isinstance(key, str):
            return None
        return self.state.get(key)

    # ---------------------------------------------------------
    # CAPABILITY MANAGEMENT
    # ---------------------------------------------------------

    def set_capabilities(self, caps: list):
        """Assigns capabilities to this sandbox context."""
        if not isinstance(caps, list):
            return {"status": "error", "code": "invalid_capability_list", "version": "4.5"}

        self.capabilities = caps
        return {"status": "ok", "version": "4.5"}

    def has_capability(self, cap: str) -> bool:
        """Checks if the module has a specific capability."""
        return isinstance(cap, str) and cap in self.capabilities

    # ---------------------------------------------------------
    # METADATA
    # ---------------------------------------------------------

    def set_metadata(self, key: str, value):
        """Stores metadata value."""
        if not isinstance(key, str) or not key.strip():
            return {"status": "error", "code": "invalid_metadata_key", "version": "4.5"}

        try:
            self.metadata[key] = value
            return {"status": "ok", "version": "4.5"}
        except Exception as exc:
            self.metadata["degraded_mode"] = True
            return {
                "status": "error",
                "code": "metadata_set_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    def get_metadata(self, key: str):
        """Retrieves metadata value."""
        if not isinstance(key, str):
            return None
        return self.metadata.get(key)

    # ---------------------------------------------------------
    # EXPORT (DETERMINISTIC SNAPSHOT)
    # ---------------------------------------------------------

    def export(self):
        """Returns a deterministic snapshot of the sandbox context."""
        return {
            "module_name": self.module_name,
            "state": dict(self.state),
            "capabilities": list(self.capabilities),
            "metadata": dict(self.metadata),
            "version": "4.5",
        }

