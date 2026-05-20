import platform
import os
from commands.base_command import BaseCommand


class SystemInfoCommand(BaseCommand):
    """
    SystemInfoCommand 4.4
    Returns basic information about the system, platform, and environment.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic output for Runtime4.4
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Safe execution via BaseCommand.run()
        - Stable structure for CLI, NL Router, GUI, Workflow Engine
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
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
    # EXECUTION (v4.4)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Returns an overview of basic system information.
        Output is structured for Workflow Engine 4.4.
        Deterministic ordering guaranteed.
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

        # Deterministic text output for CLI / NL Router
        text_output = ["System information:\n"]
        for key in sorted(info.keys()):
            text_output.append(f"- {key}: {info[key]}")

        return {
            "status": "success",
            "info": info,
            "text": "\n".join(text_output)
        }
