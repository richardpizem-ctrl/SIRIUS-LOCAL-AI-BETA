import inspect
from commands.base_command import BaseCommand


class HelpCommand(BaseCommand):
    """
    HelpCommand 4.3
    Provides detailed command introspection for CLI, NL Router, and GUI.

    Improvements in 4.3:
    - unified metadata contract
    - deterministic output for Runtime4
    - safe error handling (via BaseCommand.run)
    - consistent structure for all help responses
    """

    # ---------------------------------------------------------
    # METADATA (v4.3)
    # ---------------------------------------------------------
    name = "help"
    description = "Displays a list of commands or detailed information about a specific command."
    category = "system"

    required_identity = "FAMILY"   # Help is safe for everyone
    risk_level = 0.0
    capabilities = []

    keywords = ["help", "commands", "info"]
    examples = ["help", "help move_files"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, command_registry):
        """
        command_registry: dict {command_name: CommandClass}
        """
        self.command_registry = command_registry

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, command_name: str = None):
        """
        If no command name is provided → list all commands.
        If command name is provided → show detailed info.
        """
        if not command_name:
            return self._list_commands()

        return self._describe_command(command_name)

    # ---------------------------------------------------------
    # LIST ALL COMMANDS
    # ---------------------------------------------------------
    def _list_commands(self):
        """
        Returns a list of all registered commands with basic metadata.
        """
        output = []

        for name, cmd in self.command_registry.items():
            output.append({
                "name": cmd.name,
                "description": cmd.description,
                "category": cmd.category,
                "required_identity": cmd.required_identity,
                "risk_level": cmd.risk_level
            })

        return {
            "status": "success",
            "count": len(output),
            "commands": output
        }

    # ---------------------------------------------------------
    # DESCRIBE SINGLE COMMAND
    # ---------------------------------------------------------
    def _describe_command(self, name):
        """
        Returns detailed metadata for a single command.
        """
        cmd = self.command_registry.get(name)

        if not cmd:
            return {
                "status": "error",
                "message": f"Command '{name}' not found."
            }

        return {
            "status": "success",
            "name": cmd.name,
            "description": cmd.description,
            "category": cmd.category,
            "required_identity": cmd.required_identity,
            "risk_level": cmd.risk_level,
            "capabilities": cmd.capabilities,
            "keywords": cmd.keywords,
            "examples": cmd.examples,
            "parameters": cmd.get_parameters()
        }
