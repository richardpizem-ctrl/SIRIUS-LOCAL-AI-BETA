# sandbox_context.py
"""
SIRIUS LOCAL AI – Runtime 4.0 Sandbox Context

The Sandbox Context stores:
- isolated module state
- capability profile
- runtime metadata
- execution flags
- links to sandbox process

This is the contextual memory layer of the sandbox system.
"""


class SandboxContext4:
    """
    Holds isolated state and metadata for a sandboxed module.
    """

    def __init__(self, module_name: str):
        self.module_name = module_name

        # Isolated state for the module
        self.state = {}

        # Capabilities assigned to this module
        self.capabilities = []

        # Metadata (timestamps, flags, etc.)
        self.metadata = {
            "active": True,
            "initialized": False
        }

    # ---------------------------------------------------------
    # STATE MANAGEMENT
    # ---------------------------------------------------------

    def set_state(self, key: str, value):
        """Stores a value in the sandbox state."""
        self.state[key] = value

    def get_state(self, key: str):
        """Retrieves a value from the sandbox state."""
        return self.state.get(key)

    # ---------------------------------------------------------
    # CAPABILITY MANAGEMENT
    # ---------------------------------------------------------

    def set_capabilities(self, caps: list):
        """Assigns capabilities to this sandbox context."""
        self.capabilities = caps

    def has_capability(self, cap: str) -> bool:
        """Checks if the module has a specific capability."""
        return cap in self.capabilities

    # ---------------------------------------------------------
    # METADATA
    # ---------------------------------------------------------

    def set_metadata(self, key: str, value):
        """Stores metadata value."""
        self.metadata[key] = value

    def get_metadata(self, key: str):
        """Retrieves metadata value."""
        return self.metadata.get(key)
