"""
SIRIUS LOCAL AI – Main Entry Point (v4.0.0)
Bootstraps the CLI interface and executes commands.
"""

import sys
from runtime.cli import SiriusCLI
from runtime.runtime_manager import RuntimeManager


# ============================================================
# MAIN ENTRY (v4.0.0)
# ============================================================
def main():
    # Initialize runtime first (global logger, config, env)
    rm = RuntimeManager()
    rm.initialize()

    rm.logger.info("SIRIUS LOCAL AI – Entry point started (v4.0.0)")

    # Start CLI
    cli = SiriusCLI()
    cli.run(sys.argv)

    rm.logger.info("SIRIUS LOCAL AI – Execution finished")


# ============================================================
# EXECUTION
# ============================================================
if __name__ == "__main__":
    main()
