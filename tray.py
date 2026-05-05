import threading
import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageDraw
import subprocess
import sys
import os
import pathlib


class SiriusTray:
    """
    Windows Tray icon for SIRIUS LOCAL AI – v2.0.0
    - opens GUI (via python -m)
    - restarts the entire SIRIUS runtime
    - exits the system
    """

    def __init__(self):
        self.icon = pystray.Icon(
            "SIRIUS",
            self._create_icon(),
            "SIRIUS LOCAL AI",
            self._menu()
        )

    # --------------------------------------------------------
    # ICON
    # --------------------------------------------------------
    def _create_icon(self):
        """
        Simple black and white icon (32x32).
        """
        img = Image.new("RGB", (32, 32), "black")
        d = ImageDraw.Draw(img)
        d.rectangle([8, 8, 24, 24], fill="white")
        return img

    # --------------------------------------------------------
    # MENU
    # --------------------------------------------------------
    def _menu(self):
        return (
            Item("Open GUI", self.open_gui),
            Item("Restart SIRIUS", self.restart_sirius),
            Item("Exit Tray", self.exit_app)
        )

    # --------------------------------------------------------
    # ACTIONS
    # --------------------------------------------------------
    def open_gui(self, icon, item):
        """
        Launches the GUI using python -m so it works with any path.
        """
        python = sys.executable

        # GUI module in root directory
        gui_path = pathlib.Path(__file__).parent / "gui.py"

        subprocess.Popen([python, str(gui_path)])

    def restart_sirius(self, icon, item):
        """
        Restarts the entire SIRIUS system.
        Uses python -m sirius to start the main orchestrator.
        """
        python = sys.executable

        # Main orchestrator sirius.py
        sirius_path = pathlib.Path(__file__).parent / "sirius.py"

        subprocess.Popen([python, str(sirius_path)])
        os._exit(0)

    def exit_app(self, icon, item):
        """
        Stops the tray icon.
        """
        icon.stop()

    # --------------------------------------------------------
    # RUN
    # --------------------------------------------------------
    def run(self):
        """
        Runs the tray icon in a separate thread.
        """
        threading.Thread(target=self.icon.run, daemon=True).start()


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------
if __name__ == "__main__":
    tray = SiriusTray()
    tray.run()

    # Tray runs in background → keep main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
