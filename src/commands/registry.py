from commands.base_command import BaseCommand


class CommandRegistry:
    """
    CommandRegistry 4.4
    Central registration of command CLASSES for SIRIUS LOCAL AI Runtime4.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic ordering for NL Router 4.4
        - Strict metadata validation
        - Duplicate name protection
        - Stable registry hashing
        - Safe dynamic instantiation
        - Runtime4.4‑ready command lifecycle
    """

    def __init__(self, context):
        self._commands: dict[str, type[BaseCommand]] = {}
        self.context = context

    # ---------------------------------------------------------
    # REGISTRATION (4.4)
    # ---------------------------------------------------------
    def register(self, command_cls: type[BaseCommand]):
        """
        Registers a command CLASS by its name.
        Performs metadata validation, integrity check,
        and duplicate protection.
        """
        if not issubclass(command_cls, BaseCommand):
            raise TypeError(f"Command {command_cls} must inherit from BaseCommand.")

        # Validate metadata
        command_cls.validate_metadata()

        # Integrity check (Self‑Repair Layer 4.4)
        if not command_cls.integrity_check():
            raise ValueError(f"Integrity check failed for command: {command_cls.name}")

        # Prevent duplicate names
        if command_cls.name in self._commands:
            raise ValueError(f"Duplicate command name detected: {command_cls.name}")

        self._commands[command_cls.name] = command_cls

    # ---------------------------------------------------------
    # LOOKUP
    # ---------------------------------------------------------
    def get(self, name: str) -> type[BaseCommand] | None:
        """
        Returns a command CLASS by name.
        """
        return self._commands.get(name)

    def all(self) -> dict[str, type[BaseCommand]]:
        """
        Returns all registered command classes.
        Deterministic ordering for NL Router 4.4.
        """
        return dict(sorted(self._commands.items()))

    # ---------------------------------------------------------
    # DYNAMIC INSTANTIATION (4.4)
    # ---------------------------------------------------------
    def create_instance(self, name: str, *args, **kwargs) -> BaseCommand | None:
        """
        Creates an instance of a command by name.
        Runtime4 uses only this method.
        """
        cmd_cls = self.get(name)
        if not cmd_cls:
            return None

        return cmd_cls(*args, **kwargs)

    # ---------------------------------------------------------
    # SELF‑REPAIR SUPPORT (4.4)
    # ---------------------------------------------------------
    def compute_registry_hash(self) -> str:
        """
        Computes a deterministic hash of all registered commands.
        Used by Self‑Repair 4.4 to detect tampering.
        """
        import hashlib
        import json

        payload = {
            name: cmd.compute_hash()
            for name, cmd in self.all().items()
        }

        serialized = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    # ---------------------------------------------------------
    # HEALTH METADATA (4.4)
    # ---------------------------------------------------------
    def health(self):
        """
        Returns registry health metadata for System Health Engine 4.4.
        """
        return {
            "command_count": len(self._commands),
            "integrity_ok": all(cmd.integrity_check() for cmd in self._commands.values()),
            "registry_hash": self.compute_registry_hash(),
        }


# ---------------------------------------------------------
# DEFAULT REGISTRY (4.4)
# ---------------------------------------------------------
def create_default_registry(context) -> CommandRegistry:
    """
    Creates the default registry with core commands.
    Registers CLASSES, not instances.
    """
    registry = CommandRegistry(context)

    # Core commands
    registry.register(HelpCommand)
    registry.register(RunCommand)
    registry.register(SystemInfoCommand)

    # Context commands
    registry.register(ContextInfoCommand)
    registry.register(ContextSetCommand)
    registry.register(ContextClearCommand)
    registry.register(MemorySaveCommand)
    registry.register(MemoryLoadCommand)
    registry.register(ContextDumpCommand)
    registry.register(TranslateCommand)

    # AITE test command
    registry.register(TriageTestCommand)

    # FS-AGENT command
    registry.register(MoveTextFilesCommand)

    return registry
