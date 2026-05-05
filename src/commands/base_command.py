import inspect
import time


class BaseCommand:
    """
    Base class for all commands in the SIRIUS LOCAL AI 4.0 system.
    Every command must implement the `execute()` method.

    New in version 4.0:
    - introspection 4.0 (parameters, types, default values)
    - metadata for NL Router 4.0
    - security capability flags
    - risk-aware execution hooks
    - audit trail for Runtime Core 4.0
    - unified command lifecycle
    """

    # ---------------------------------------------------------
    # COMMAND METADATA (v4.0)
    # ---------------------------------------------------------
    name: str = "base"
    description: str = "Base command class"
    category: str = "system"

    # SECURITY FAMILY integration
    required_identity: str = "OWNER"      # OWNER / FAMILY / STRANGER
    risk_level: float = 0.0               # 0.0 = safe, 1.0 = dangerous

    # Capability flags (WIN-CAP, FS-AGENT, etc.)
    capabilities: list = []               # ["fs_write", "system_ops", "network_ops"]

    # NL Router 4.0 routing hints
    keywords: list = []                   # ["move", "copy", "delete"]
    examples: list = []                   # ["move file X to Y"]

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Method that must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement execute().")

    # ---------------------------------------------------------
    # INTROSPECTION 4.0
    # ---------------------------------------------------------
    @classmethod
    def get_parameters(cls):
        """
        Returns a list of __init__ parameters for introspection.
        Used in HelpCommand, CLI, and NL Router 4.0.
        """
        signature = inspect.signature(cls.__init__)
        params = []

        for name, param in signature.parameters.items():
            if name == "self":
                continue

            params.append({
                "name": name,
                "type": str(param.annotation),
                "default": None if param.default is inspect._empty else param.default
            })

        return params

    # ---------------------------------------------------------
    # COMMAND LIFECYCLE (v4.0)
    # ---------------------------------------------------------
    def before_execute(self):
        """
        Hook before command execution.
        Runtime Core 4.0 will insert:
        - identity check
        - risk check
        - capability enforcement
        - audit logging
        """
        self._start_time = time.time()

    def after_execute(self, result=None):
        """
        Hook after command execution.
        Runtime Core 4.0 will insert:
        - audit trail
        - performance metrics
        - anomaly detection
        """
        duration = time.time() - self._start_time
        return {
            "command": self.name,
            "duration": duration,
            "result": result
        }

    # ---------------------------------------------------------
    # SAFE EXECUTION WRAPPER (v4.0)
    # ---------------------------------------------------------
    def run(self, *args, **kwargs):
        """
        Safe wrapper around execute().
        Runtime Core 4.0 will call only run(), not execute().
        """
        self.before_execute()
        result = self.execute(*args, **kwargs)
        return self.after_execute(result)
