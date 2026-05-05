"""
SIRIUS LOCAL AI ALFA – v2.0.0 entrypoint

This is the main entrypoint for the SIRIUS 2.0 runtime.
– bootstrap RuntimeManager 2.0
– load plugins via PluginLoader 2.0
– initialize NL Router 2.0
– start AI Loop 2.0 (autonomous mode)
– CLI mode as the primary front-end
– hooks for GUI / TRAY / VOICE (future modules)
"""

import argparse
import threading
import sys
from typing import Optional

# --- CORE RUNTIME 2.0 ---

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter
from runtime.ai_loop import AILoop


class SiriusApp:
    """
    Main application class that orchestrates the entire SIRIUS runtime.
    """

    def __init__(self, enable_ai_loop: bool = True) -> None:
        # Runtime core
        self.runtime = RuntimeManager()

        # Plugin system
        self.plugin_loader = PluginLoader(self.runtime)

        # Natural language router
        self.nl_router = NaturalLanguageRouter(self.runtime, self.plugin_loader)

        # Autonomous AI loop
        self.ai_loop: Optional[AILoop] = None
        if enable_ai_loop:
            self.ai_loop = AILoop(self.runtime, self.plugin_loader)

        self._ai_loop_thread: Optional[threading.Thread] = None

    # --------------------------------------------------------------------- #
    #  BOOTSTRAP
    # --------------------------------------------------------------------- #

    def bootstrap(self) -> None:
        """
        Initializes the runtime, loads plugins, and prepares the system.
        """
        # 1) Initialize runtime
        self.runtime.initialize()

        # 2) Load plugins
        self.plugin_loader.load_all()

        # 3) Initialize NL router
        self.nl_router.initialize()

        # 4) Start AI loop (if enabled)
        if self.ai_loop is not None:
            self._start_ai_loop_background()

    def _start_ai_loop_background(self) -> None:
        """
        Starts the AI loop in a background thread (autonomous mode).
        """
        if self.ai_loop is None:
            return

        def _runner() -> None:
            try:
                self.ai_loop.run()
            except Exception as e:
                # Runtime should have its own logging, this is just fallback
                self.runtime.log_error(f"AI Loop crashed: {e}")

        self._ai_loop_thread = threading.Thread(
            target=_runner,
            name="SIRIUS-AI-LOOP",
            daemon=True,
        )
        self._ai_loop_thread.start()

    # --------------------------------------------------------------------- #
    #  FRONT-END HOOKS
    # --------------------------------------------------------------------- #

    def handle_text(self, text: str) -> str:
        """
        Processes text input (CLI, GUI, VOICE) through NL Router 2.0.
        """
        text = text.strip()
        if not text:
            return ""

        try:
            return self.nl_router.route(text)
        except Exception as e:
            self.runtime.log_error(f"Error while handling input: {e}")
            return f"Error: {e}"

    # --------------------------------------------------------------------- #
    #  CLI MODE
    # --------------------------------------------------------------------- #

    def run_cli(self) -> None:
        """
        Simple console mode – primary front-end for SIRIUS 2.0.
        """
        print("SIRIUS LOCAL AI ALFA – v2.0.0 (Runtime 2.0)")
        print("Type 'exit' to quit.\n")

        while True:
            try:
                user_input = input(">>> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting SIRIUS.")
                break

            if user_input.lower() in {"exit", "quit"}:
                print("Exiting SIRIUS.")
                break

            if not user_input:
                continue

            output = self.handle_text(user_input)
            if output:
                print(output)

    # --------------------------------------------------------------------- #
    #  SHUTDOWN
    # --------------------------------------------------------------------- #

    def shutdown(self) -> None:
        """
        Gracefully shuts down the runtime and AI loop.
        """
        if self.ai_loop is not None:
            try:
                self.ai_loop.stop()
            except Exception:
                pass

        if self._ai_loop_thread is not None and self._ai_loop_thread.is_alive():
            self._ai_loop_thread.join(timeout=2.0)

        try:
            self.runtime.shutdown()
        except Exception:
            pass


# ------------------------------------------------------------------------- #
#  ARGPARSE / MAIN
# ------------------------------------------------------------------------- #

def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="sirius",
        description="SIRIUS LOCAL AI ALFA – v2.0.0 runtime entrypoint",
    )

    parser.add_argument(
        "--no-ai-loop",
        action="store_true",
        help="Disable autonomous AI loop (runtime runs only on user input).",
    )

    parser.add_argument(
        "--cli",
        action="store_true",
        help="Force CLI mode (no GUI/TRAY/VOICE front-end).",
    )

    # Hooks for future modules – placeholders for now
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Start GUI front-end (when implemented).",
    )
    parser.add_argument(
        "--tray",
        action="store_true",
        help="Start system tray front-end (when implemented).",
    )
    parser.add_argument(
        "--voice",
        action="store_true",
        help="Start voice front-end (when implemented).",
    )

    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
    if argv is None:
        argv = sys.argv[1:]

    args = parse_args(argv)

    app = SiriusApp(enable_ai_loop=not args.no_ai_loop)

    try:
        app.bootstrap()

        # For now we only have CLI – GUI/TRAY/VOICE will come later
        # Logic:
        # – if --cli → run CLI
        # – when GUI/TRAY/VOICE exist, this will decide based on args
        app.run_cli()

    finally:
        app.shutdown()


if __name__ == "__main__":
    main()
