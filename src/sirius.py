# sirius.py
# SIRIUS LOCAL AI – Runtime Entry Point 4.3.x
# Deterministic, safe-mode compatible bootstrap for Runtime 4.3

from __future__ import annotations

import argparse
import threading
import sys
from typing import Optional

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter
from runtime.ai_loop import AILoop


class SiriusApp:
    """
    Main application class that orchestrates the entire SIRIUS runtime 4.3.x.

    Responsibilities:
        - bootstrap RuntimeManager 4.3
        - load plugins via PluginLoader 4.3
        - initialize NL Router 4.3
        - start AI Loop 4.3 (autonomous mode)
        - provide CLI as primary front-end
        - expose hooks for GUI / TRAY / VOICE
        - support safe-mode and degraded-mode
    """

    def __init__(self, enable_ai_loop: bool = True) -> None:
        self.safe_mode = False
        self.degraded_mode = False

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
        Deterministic, safe-mode aware.
        """
        if self.safe_mode:
            return

        try:
            # 1) Initialize runtime
            self.runtime.initialize()

            # 2) Load plugins
            self.plugin_loader.load_all()

            # 3) Initialize NL router
            self.nl_router.initialize()

            # 4) Start AI loop (if enabled)
            if self.ai_loop is not None:
                self._start_ai_loop_background()

        except Exception as exc:
            self.degraded_mode = True
            try:
                self.runtime.log_error(f"Bootstrap failed, entering degraded mode: {exc}")
            except Exception:
                print(f"[SIRIUS] Bootstrap failed: {exc}")

    def _start_ai_loop_background(self) -> None:
        """
        Starts the AI loop in a background thread (autonomous mode).
        """

        if self.ai_loop is None or self.safe_mode:
            return

        def _runner() -> None:
            try:
                self.ai_loop.run()
            except Exception as e:
                try:
                    self.runtime.log_error(f"AI Loop crashed: {e}")
                except Exception:
                    print(f"[SIRIUS] AI Loop crashed: {e}")
                self.degraded_mode = True

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
        Processes text input (CLI, GUI, VOICE) through NL Router 4.3.
        """
        text = text.strip()
        if not text:
            return ""

        if self.safe_mode:
            return "SIRIUS is in SAFE MODE. Text processing is temporarily disabled."

        try:
            return self.nl_router.route(text)
        except Exception as e:
            self.degraded_mode = True
            try:
                self.runtime.log_error(f"Error while handling input: {e}")
            except Exception:
                print(f"[SIRIUS] Error while handling input: {e}")
            return f"Error: {e}"

    # --------------------------------------------------------------------- #
    #  CLI MODE
    # --------------------------------------------------------------------- #

    def run_cli(self) -> None:
        """
        Simple console mode – primary front-end for SIRIUS 4.3.
        """
        header = "SIRIUS LOCAL AI – Runtime 4.3.x"
        if self.safe_mode:
            header += " [SAFE MODE]"
        elif self.degraded_mode:
            header += " [DEGRADED MODE]"

        print(header)
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

    # --------------------------------------------------------------------- #
    #  SAFE-MODE CONTROL
    # --------------------------------------------------------------------- #

    def enter_safe_mode(self) -> None:
        self.safe_mode = True

    def exit_safe_mode(self) -> None:
        self.safe_mode = False


# ------------------------------------------------------------------------- #
#  ARGPARSE / MAIN
# ------------------------------------------------------------------------- #

def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="sirius",
        description="SIRIUS LOCAL AI – Runtime 4.3.x entrypoint",
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

    parser.add_argument(
        "--safe-mode",
        action="store_true",
        help="Start SIRIUS in SAFE MODE (diagnostics only, no autonomous actions).",
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

    if args.safe_mode:
        app.enter_safe_mode()

    try:
        app.bootstrap()
        # For now we only have CLI – GUI/TRAY/VOICE will come later
        app.run_cli()
    finally:
        app.shutdown()


if __name__ == "__main__":
    main()
