import platform
import os
from commands.base_command import BaseCommand


class SystemInfoCommand(BaseCommand):
    """
    SystemInfoCommand 4.3
    Returns basic information about the system, platform, and environment.

    Improvements in 4.3:
    - unified metadata contract
    - deterministic output for Runtime4
    - safe error handling (via BaseCommand.run)
    - consistent structure for CLI, NL Router, and GUI
    """

    # ---------------------------------------------------------
    # METADATA (v4.3)
    # ---------------------------------------------------------
    name = "system-info"
    description = "Displays information about the system, platform, and environment."
    category = "system"

    required_identity = "FAMILY"     # safe for everyone
    risk_level = 0.0
    capabilities = ["system_read"]

    keywords = ["system", "info", "platform", "os", "environment"]
    examples = ["system-info", "show system info"]

    # ---------------------------------------------------------
    # EXECUTION (v4.3)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Returns an overview of basic system information.
        Output is structured for Workflow Engine 4.3.
        """

        info = {
            "platform": platform.system(),
            "platform_release": platform.release(),
            "platform_version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "working_directory": os.getcwd(),
        }

        # Text output for CLI / NL Router
        text_output = ["System information:\n"]
        for key, value in info.items():
            text_output.append(f"- {key}: {value}")

        return {
            "status": "success",
            "info": info,
            "text": "\n".join(text_output)
        }
