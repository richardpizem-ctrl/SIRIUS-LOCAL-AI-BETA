from commands.base_command import BaseCommand
from commands.help_command import HelpCommand
from commands.run_command import RunCommand
from commands.system_info_command import SystemInfoCommand

from context.context_info_command import ContextInfoCommand
from context.context_set_command import ContextSetCommand
from context.context_clear_command import ContextClearCommand
from context.memory_save_command import MemorySaveCommand
from context.memory_load_command import MemoryLoadCommand
from context.context_dump_command import ContextDumpCommand
from context.translate_command import TranslateCommand

from commands.triage_test_command import TriageTestCommand
from commands.move_text_files import MoveTextFilesCommand


class CommandRegistry:
    """
    CommandRegistry 4.3
    Central registration of command CLASSES for SIRIUS LOCAL AI Runtime4.

    Improvements in 4.3:
    - metadata validation for every command
    - duplicate name protection
    - deterministic ordering for NL Router 4.x
    - Self‑Repair 4.4 compatibility (hashing)
    - safe dynamic instantiation
    """

    def __init__(self, context):
        self._commands: dict[str, type[BaseCommand]] = {}
        self.context = context

    # ---------------------------------------------------------
    # REGISTRATION (v4.3)
    # ---------------------------------------------------------
    def register(self, command_cls: type[BaseCommand]):
        """
        Registers a command CLASS by its name.
        Performs metadata validation and duplicate protection.
        """
        if not issubclass(command_cls, BaseCommand):
            raise TypeError(f"Command {command_cls} must inherit from BaseCommand.")

        # Validate metadata
        command_cls.validate_metadata()

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
        Deterministic ordering for NL Router 4.x.
        """
        return dict(sorted(self._commands.items()))

    # ---------------------------------------------------------
    # DYNAMIC INSTANTIATION (v4.3)
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
    # SELF‑REPAIR SUPPORT (v4.3)
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
# DEFAULT REGISTRY (v4.3)
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
