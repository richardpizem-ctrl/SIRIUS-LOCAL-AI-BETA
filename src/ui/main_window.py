# ============================================================
# SIRIUS LOCAL AI – MAIN WINDOW
# Hosts the ORB widget inside the main UI
# ============================================================

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from ui.orb_widget import OrbWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SIRIUS LOCAL AI")

        # Central container
        container = QWidget()
        layout = QVBoxLayout(container)

        # ORB widget
        self.orb = OrbWidget()
        layout.addWidget(self.orb)

        # Set layout
        self.setCentralWidget(container)
