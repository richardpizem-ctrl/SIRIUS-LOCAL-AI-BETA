from .base_command import BaseCommand
from .help_command import HelpCommand
from .run_command import RunCommand
from .system_info_command import SystemInfoCommand

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
    Command Registry 4.0
    Central registration of commands for SIRIUS LOCAL AI 4.0.

    New in version 4.0:
    - registers command CLASSES, not instances
    - supports introspection 4.0
    - provides metadata for NL Router 4.0
    - supports dynamic instantiation via Runtime Core 4.0
    - supports SECURITY FAMILY 4.0 (identity, risk, capabilities)
    """

    def __init__(self, context):
        self._commands: dict[str, type[BaseCommand]] = {}
        self.context = context

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------
    def register(self, command_cls: type[BaseCommand]):
        """
        Registers a command CLASS by its name.
        """
        if not issubclass(command_cls, BaseCommand):
            raise TypeError(f"Command {command_cls} must inherit from BaseCommand.")

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
        """
        return self._commands

    # ---------------------------------------------------------
    # DYNAMIC INSTANTIATION (v4.0)
    # ---------------------------------------------------------
    def create_instance(self, name: str, *args, **kwargs) -> BaseCommand | None:
        """
        Creates an instance of a command by name.
        Runtime Core 4.0 will use only this.
        """
        cmd_cls = self.get(name)
        if not cmd_cls:
            return None

        return cmd_cls(*args, **kwargs)


# ---------------------------------------------------------
# DEFAULT REGISTRY (v4.0)
# ---------------------------------------------------------
def create_default_registry(context) -> CommandRegistry:
    """
    Creates the default registry with core commands.
    Registers CLASSES, not instances.
    """
    registry = CommandRegistry(context)

    # HelpCommand needs registry, but we register the CLASS
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

    # MoveTextFilesCommand (FS-AGENT)
    registry.register(MoveTextFilesCommand)

    return registry
