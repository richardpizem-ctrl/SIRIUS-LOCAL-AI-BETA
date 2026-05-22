# Runtime4 Command Base Class
# Baseline module
# Version: 4.5.0

import inspect
import time
import hashlib
import json
import os


class BaseCommand:
    """
    BaseCommand 4.5
    Unified base class for all SIRIUS LOCAL AI Runtime4 commands.

    Updated in 4.5:
        - Prepared for Self‑Repair Layer 4.5
        - Deterministic metadata hashing (unchanged)
        - Integrity hooks (unchanged)
        - Health metadata (unchanged)
        - Extended audit record (unchanged)
        - Strict deterministic execution contract (unchanged)
    """

    # ---------------------------------------------------------
    # COMMAND METADATA (v4.5)
    # ---------------------------------------------------------
    name: str = "base"
    description: str = "Base command class"
    category: str = "system"

    required_identity: str = "OWNER"      # OWNER / FAMILY / STRANGER / CHILD
    risk_level: float = 0.0
    capabilities: list = []               # ["fs_write", "system_ops"]

    keywords: list = []
    examples: list = []

    # ---------------------------------------------------------
    # EXECUTION (must be overridden)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement execute().")

    # ---------------------------------------------------------
    # INTROSPECTION 4.5
    # ---------------------------------------------------------
    @classmethod
    def get_parameters(cls):
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
    # COMMAND HASH (Self‑Repair 4.5)
    # ---------------------------------------------------------
    @classmethod
    def compute_hash(cls) -> str:
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
    # INTEGRITY HOOKS (4.5)
    # ---------------------------------------------------------
    @classmethod
    def integrity_check(cls):
        """
        Loader 4.5 calls this before registration.
        Ensures metadata is valid.
        """
        try:
            cls.validate_metadata()
            return True
        except Exception:
            return False

    @classmethod
    def integrity_metadata(cls):
        """
        Returns metadata used by Integrity Engine 4.5.
        """
        return {
            "command": cls.name,
            "hash": cls.compute_hash(),
            "file_exists": os.path.exists(__file__),
        }

    # ---------------------------------------------------------
    # HEALTH METADATA (4.5)
    # ---------------------------------------------------------
    def health(self):
        return {
            "command": self.name,
            "risk_level": self.risk_level,
            "capabilities": self.capabilities,
            "integrity_ok": True,
        }

    # ---------------------------------------------------------
    # LIFECYCLE HOOKS
    # ---------------------------------------------------------
    def before_execute(self, identity="OWNER", params=None):
        self._start_time = time.time()
        self._identity_used = identity
        self._params_used = params or {}

    def after_execute(self, result=None, error=None):
        duration = time.time() - getattr(self, "_start_time", time.time())

        return {
            "command": self.name,
            "duration": duration,
            "result": result,
            "error": str(error) if error else None,
            "error_type": type(error).__name__ if error else None,
            "timestamp": time.time(),
            "command_hash": self.compute_hash(),
            "identity_used": self._identity_used,
            "risk_level": self.risk_level,
            "capabilities": self.capabilities,
            "parameters": self._params_used,
        }

    # ---------------------------------------------------------
    # SAFE EXECUTION WRAPPER (v4.5)
    # ---------------------------------------------------------
    def run(self, identity="OWNER", params=None, *args, **kwargs):
        """
        Runtime Core 4.5 calls ONLY run(), never execute().
        """
        self.before_execute(identity=identity, params=params)

        try:
            result = self.execute(*args, **kwargs)
            return self.after_execute(result=result)
        except Exception as e:
            return self.after_execute(result=None, error=e)
