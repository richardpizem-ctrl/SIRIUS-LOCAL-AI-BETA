import inspect
import time
import hashlib
import json


class BaseCommand:
    """
    BaseCommand 4.3
    Unified base class for all SIRIUS LOCAL AI Runtime4 commands.

    Version 4.3:
    - stable metadata contract for all commands
    - deterministic command hash (for Self‑Repair 4.4)
    - extended audit info (duration, error, hash, timestamp)
    - safe execution wrapper (no uncaught exceptions)
    - consistent introspection output for NL Router 4.x
    """

    # ---------------------------------------------------------
    # COMMAND METADATA (v4.3)
    # ---------------------------------------------------------
    name: str = "base"
    description: str = "Base command class"
    category: str = "system"

    # SECURITY FAMILY integration
    required_identity: str = "OWNER"      # OWNER / FAMILY / STRANGER / CHILD
    risk_level: float = 0.0               # 0.0 = safe, 1.0 = dangerous
    capabilities: list = []               # ["fs_write", "system_ops", "network_ops"]

    # NL Router 4.x routing hints
    keywords: list = []                   # ["move", "copy", "delete"]
    examples: list = []                   # ["move file X to Y"]

    # ---------------------------------------------------------
    # EXECUTION (must be overridden)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Subclasses MUST override this.
        """
        raise NotImplementedError("Subclasses must implement execute().")

    # ---------------------------------------------------------
    # INTROSPECTION 4.3
    # ---------------------------------------------------------
    @classmethod
    def get_parameters(cls):
        """
        Return a list of __init__ parameters for introspection.
        Used by HelpCommand, CLI, NL Router 4.x.
        """
        signature = inspect.signature(cls.__init__)
        params = []

        for name, param in signature.parameters.items():
            if name == "self":
                continue

            params.append({
                "name": name,
                "type": str(param.annotation),
                "default": None if param.default is inspect._empty else param.default,
                "required": param.default is inspect._empty,
            })

        return params

    # ---------------------------------------------------------
    # METADATA VALIDATION
    # ---------------------------------------------------------
    @classmethod
    def validate_metadata(cls):
        """
        Ensure that command metadata is valid and consistent.
        Runtime4 uses this during command registration.
        """
        if not isinstance(cls.name, str) or not cls.name:
            raise ValueError(f"Command {cls} has invalid name.")

        if not isinstance(cls.description, str):
            raise ValueError(f"Command {cls.name} has invalid description.")

        if not isinstance(cls.category, str):
            raise ValueError(f"Command {cls.name} has invalid category.")

        if not isinstance(cls.required_identity, str):
            raise ValueError(f"Command {cls.name} has invalid required_identity.")

        if not isinstance(cls.risk_level, float):
            raise ValueError(f"Command {cls.name} has invalid risk_level.")

    # ---------------------------------------------------------
    # COMMAND HASH (Self‑Repair 4.4)
    # ---------------------------------------------------------
    @classmethod
    def compute_hash(cls) -> str:
        """
        Deterministic hash of command metadata.
        Used by Self‑Repair Engine to detect tampering.
        """
        payload = {
            "name": cls.name,
            "description": cls.description,
            "category": cls.category,
            "required_identity": cls.required_identity,
            "risk_level": cls.risk_level,
            "capabilities": cls.capabilities,
            "keywords": cls.keywords,
            "examples": cls.examples,
        }
        serialized = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    # ---------------------------------------------------------
    # LIFECYCLE HOOKS
    # ---------------------------------------------------------
    def before_execute(self):
        """
        Hook before execution.
        Runtime4 can inject:
        - identity check
        - risk check
        - capability enforcement
        - audit logging
        """
        self._start_time = time.time()

    def after_execute(self, result=None, error=None):
        """
        Hook after execution.
        Returns a unified audit record.
        """
        duration = time.time() - getattr(self, "_start_time", time.time())

        return {
            "command": self.name,
            "duration": duration,
            "result": result,
            "error": str(error) if error else None,
            "timestamp": time.time(),
            "hash": self.compute_hash(),
        }

    # ---------------------------------------------------------
    # SAFE EXECUTION WRAPPER (v4.3)
    # ---------------------------------------------------------
    def run(self, *args, **kwargs):
        """
        Safe wrapper around execute().
        Runtime Core 4.x calls ONLY run(), never execute().
        """
        self.before_execute()

        try:
            result = self.execute(*args, **kwargs)
            return self.after_execute(result=result)
        except Exception as e:
            # Runtime4 will log this in audit trail
            return self.after_execute(result=None, error=e)
