"""
SIRIUS LOCAL AI – Runtime 4.3 Sandbox Context

The Sandbox Context stores:
- isolated module state
- capability profile
- runtime metadata
- execution flags
- links to sandbox process
- safe-mode and degraded-mode indicators

This is the contextual memory layer of the sandbox system.
"""


class SandboxContext4:
    """
    Holds isolated state and metadata for a sandboxed module.
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
            raise ValueError("Invalid module name for SandboxContext4.")

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
            return {"status": "error", "code": "invalid_state_key"}

        try:
            self.state[key] = value
            return {"status": "success"}
        except Exception as exc:
            self.metadata["degraded_mode"] = True
            return {"status": "error", "code": "state_set_failed", "exception": str(exc)}

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
            return {"status": "error", "code": "invalid_capability_list"}

        self.capabilities = caps
        return {"status": "success"}

    def has_capability(self, cap: str) -> bool:
        """Checks if the module has a specific capability."""
        return isinstance(cap, str) and cap in self.capabilities

    # ---------------------------------------------------------
    # METADATA
    # ---------------------------------------------------------

    def set_metadata(self, key: str, value):
        """Stores metadata value."""
        if not isinstance(key, str) or not key.strip():
            return {"status": "error", "code": "invalid_metadata_key"}

        try:
            self.metadata[key] = value
            return {"status": "success"}
        except Exception as exc:
            self.metadata["degraded_mode"] = True
            return {"status": "error", "code": "metadata_set_failed", "exception": str(exc)}

    def get_metadata(self, key: str):
        """Retrieves metadata value."""
        if not isinstance(key, str):
            return None
        return self.metadata.get(key)
