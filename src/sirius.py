# sirius_4_5.py
# SIRIUS LOCAL AI – Runtime Entry Point 4.5.0 PRO
# Deterministic, safe-mode compatible bootstrap for Runtime 4.5

from __future__ import annotations

import argparse
import threading
import sys
from typing import Optional

from runtime.runtime_manager_4_5 import RuntimeManager45
from runtime.plugin_loader_4_5 import PluginLoader45
from runtime.nl_router_4_5 import NaturalLanguageRouter45
from runtime.ai_loop_4_5 import AILoop45


class SiriusApp45:
    """
    Main application class orchestrating the entire SIRIUS runtime 4.5.0 PRO.

    Responsibilities:
        - bootstrap RuntimeManager 4.5
        - load plugins via PluginLoader 4.5
        - initialize NL Router 4.5
        - start AI Loop 4.5 (autonomous mode)
        - provide CLI as primary front-end
        - expose hooks for GUI / TRAY / VOICE
        - support safe-mode and degraded-mode
        - Phase‑5 ready
    """

    def __init__(self, enable_ai_loop: bool = True) -> None:
        self.safe_mode = False
        self.degraded_mode = False

        # Runtime core
        self.runtime = RuntimeManager45()

        # Plugin system
        self.plugin_loader = PluginLoader45(self.runtime)

        # Natural language router
        self.nl_router = NaturalLanguageRouter45(self.runtime, self.plugin_loader)

        # Autonomous AI loop
        self.ai_loop: Optional[AILoop45] = None
        if enable_ai_loop:
            self.ai_loop = AILoop45(self.runtime, self.plugin_loader)

        self._ai_loop_thread: Optional[threading.Thread] = None

    # --------------------------------------------------------------------- #
    #  BOOTSTRAP
    # --------------------------------------------------------------------- #

    def bootstrap(self) -> None:
        if self.safe_mode:
            return

        try:
            self.runtime.initialize()
            self.plugin_loader.load_all()
            self.nl_router.initialize()

            if self.ai_loop is not None:
                self._start_ai_loop_background()

        except Exception as exc:
            self.degraded_mode = True
            try:
                self.runtime.log_error(f"Bootstrap failed, entering degraded mode: {exc}")
            except Exception:
                pass

    def _start_ai_loop_background(self) -> None:
        if self.ai_loop is None or self.safe_mode:
            return

        def _runner() -> None:
            try:
                self.ai_loop.run()
            except Exception as e:
                try:
                    self.runtime.log_error(f"AI Loop crashed: {e}")
                except Exception:
                    pass
                self.degraded_mode = True

        self._ai_loop_thread = threading.Thread(
            target=_runner,
            name="SIRIUS-AI-LOOP-45",
            daemon=True,
        )
        self._ai_loop_thread.start()

    # --------------------------------------------------------------------- #
    #  FRONT-END HOOKS
    # --------------------------------------------------------------------- #

    def handle_text(self, text: str) -> str:
        text = text.strip()
        if not text:
            return ""

        if self.safe_mode:
            return "SIRIUS 4.5 is in SAFE MODE. Text processing is temporarily disabled."

        try:
            return self.nl_router.route(text)
        except Exception as e:
            self.degraded_mode = True
            try:
                self.runtime.log_error(f"Error while handling input: {e}")
            except Exception:
                pass
            return f"Error: {e}"

    # --------------------------------------------------------------------- #
    #  CLI MODE
    # --------------------------------------------------------------------- #

    def run_cli(self) -> None:
        header = "SIRIUS LOCAL AI – Runtime 4.5.0 PRO"
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
        description="SIRIUS LOCAL AI – Runtime 4.5.0 PRO entrypoint",
    )

    parser.add_argument(
        "--no-ai-loop",
        action="store_true",
        help="Disable autonomous AI loop.",
    )

    parser.add_argument(
        "--cli",
        action="store_true",
        help="Force CLI mode.",
    )

    parser.add_argument(
        "--safe-mode",
        action="store_true",
        help="Start SIRIUS in SAFE MODE.",
    )

    parser.add_argument("--gui", action="store_true")
    parser.add_argument("--tray", action="store_true")
    parser.add_argument("--voice", action="store_true")

    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
    if argv is None:
        argv = sys.argv[1:]

    args = parse_args(argv)

    app = SiriusApp45(enable_ai_loop=not args.no_ai_loop)

    if args.safe_mode:
        app.enter_safe_mode()

    try:
        app.bootstrap()
        app.run_cli()
    finally:
        app.shutdown()


if __name__ == "__main__":
    main()
