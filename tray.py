import threading
import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageDraw
import subprocess
import sys
import os
import pathlib

from runtime.runtime_manager import RuntimeManager


# ============================================================
# SIRIUS TRAY ICON (v4.0.0)
# ============================================================
class SiriusTray:
    """
    SIRIUS LOCAL AI — Windows Tray Icon (v4.0.0)

    Features:
    - Launch GUI
    - Restart SIRIUS runtime
    - Exit tray safely
    """

    def __init__(self):
        # Runtime for logging
        self.rm = RuntimeManager()
        self.rm.initialize()

        self.icon = pystray.Icon(
            "SIRIUS",
            self._create_icon(),
            "SIRIUS LOCAL AI",
            self._menu()
        )

        self.rm.logger.info("Tray initialized (v4.0.0)")

    # --------------------------------------------------------
    # ICON (v4)
    # --------------------------------------------------------
    def _create_icon(self):
        """Create simple black/white tray icon."""
        img = Image.new("RGB", (32, 32), "black")
        d = ImageDraw.Draw(img)
        d.rectangle([8, 8, 24, 24], fill="white")
        return img

    # --------------------------------------------------------
    # MENU (v4)
    # --------------------------------------------------------
    def _menu(self):
        return (
            Item("Open GUI", self.open_gui),
            Item("Restart SIRIUS", self.restart_sirius),
            Item("Exit Tray", self.exit_app)
        )

    # --------------------------------------------------------
    # ACTIONS (v4)
    # --------------------------------------------------------
    def open_gui(self, icon, item):
        """Launch GUI using python."""
        try:
            python = sys.executable
            gui_path = pathlib.Path(__file__).parent / "gui.py"
            subprocess.Popen([python, str(gui_path)])
            self.rm.logger.info("GUI launched from tray")
        except Exception as e:
            self.rm.logger.error(f"Tray GUI launch error: {e}")

    def restart_sirius(self, icon, item):
        """Restart entire SIRIUS runtime."""
        try:
            python = sys.executable
            sirius_path = pathlib.Path(__file__).parent / "sirius.py"
            subprocess.Popen([python, str(sirius_path)])
            self.rm.logger.info("SIRIUS restarted from tray")
            os._exit(0)
        except Exception as e:
            self.rm.logger.error(f"Tray restart error: {e}")

    def exit_app(self, icon, item):
        """Stop tray icon."""
        self.rm.logger.info("Tray exit requested")
        icon.stop()

    # --------------------------------------------------------
    # RUN (v4)
    # --------------------------------------------------------
    def run(self):
        """Run tray icon in background thread."""
        self.rm.logger.info("Tray icon running")
        threading.Thread(target=self.icon.run, daemon=True).start()


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    tray = SiriusTray()
    tray.run()

    # Keep main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
