# app.py
# SIRIUS LOCAL AI – Application Entry Point 4.3.x
# Deterministic, safe-mode compatible startup pipeline

import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


def run_sirius_app():
    """
    Main entry point for SIRIUS LOCAL AI Runtime (4.3.x).

    Responsibilities:
        - Initialize QApplication
        - Initialize MainWindow
        - Provide safe-mode and degraded-mode fallback
        - Provide deterministic startup behavior
        - Provide error-safe execution
    """

    try:
        app = QApplication(sys.argv)

        # Main window (Phase‑4)
        win = MainWindow()
        win.show()

        return sys.exit(app.exec())

    except Exception as exc:
        # Global startup failure → degraded mode fallback
        print("\n[SIRIUS RUNTIME ERROR]")
        print("Startup failed. Entering degraded mode.")
        print(f"Exception: {exc}\n")

        # Minimal fallback window
        try:
            app = QApplication(sys.argv)
            from PySide6.QtWidgets import QLabel

            fallback = QLabel(
                "SIRIUS LOCAL AI – Startup Error\n(DEGRADED MODE)",
                alignment=0x84  # Qt.AlignCenter
            )
            fallback.resize(400, 200)
            fallback.show()

            return sys.exit(app.exec())

        except Exception:
            print("Critical failure: unable to start fallback UI.")
            return 1


if __name__ == "__main__":
    run_sirius_app()
