"""
SIRIUS LOCAL AI – Main Entry Point
Starts the CLI parser and executes commands.
"""

import sys
from runtime.cli import CLI


def main():
    cli = CLI()
    cli.run(sys.argv)


if __name__ == "__main__":
    main()
