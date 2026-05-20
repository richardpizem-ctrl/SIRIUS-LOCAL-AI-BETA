# main_window_4_4.py
# SIRIUS LOCAL AI – Main Window 4.4.0 PRO
# Phase‑4 UI Manager compatible main application window (Phase‑5 ready)

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from ui.orb_widget_4_4 import OrbWidget44


class MainWindow44(QMainWindow):
    """
    MainWindow 4.4.0 PRO

    Responsibilities:
        - Host the ORB widget (Phase‑4, Phase‑5 ready)
        - Provide a stable root container for UI Manager 4.4
        - Support safe‑mode and degraded‑mode (Security Family 4.4)
        - Provide structured lifecycle hooks
        - Deterministic, offline-only behavior
        - Self‑Repair 4.4 compatible
    """

    def __init__(self):
        super().__init__()

        self.safe_mode = False
        self.degraded_mode = False

        self.setWindowTitle("SIRIUS LOCAL AI")
        self.setMinimumSize(600, 400)

        # -----------------------------------------------------
        # Central container
        # -----------------------------------------------------
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # -----------------------------------------------------
        # ORB widget (Phase‑4 / Phase‑5 ready)
        # -----------------------------------------------------
        try:
            self.orb = OrbWidget44()
            layout.addWidget(self.orb, alignment=Qt.AlignCenter)

        except Exception as exc:
            self.degraded_mode = True
            layout.addWidget(self._build_error_placeholder(str(exc)))

        # -----------------------------------------------------
        # Finalize layout
        # -----------------------------------------------------
        self.setCentralWidget(container)

    # ---------------------------------------------------------
    # Internal fallback UI
    # ---------------------------------------------------------

    def _build_error_placeholder(self, message: str) -> QWidget:
        """
        Simple degraded-mode placeholder widget.
        Used when ORB widget fails to initialize.
        """
        from PySide6.QtWidgets import QLabel

        label = QLabel(f"UI Error (DEGRADED MODE)\n{message}")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: red; font-size: 14px;")
        return label

    # ---------------------------------------------------------
    # Lifecycle hooks (Phase‑4 / Phase‑5 ready)
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        """Switch window into safe-mode."""
        self.safe_mode = True
        self.setWindowTitle("SIRIUS LOCAL AI – SAFE MODE")

    def exit_safe_mode(self):
        """Return window to normal mode."""
        self.safe_mode = False
        self.setWindowTitle("SIRIUS LOCAL AI")

    def is_safe_mode(self) -> bool:
        return self.safe_mode

    def is_degraded_mode(self) -> bool:
        return self.degraded_mode
