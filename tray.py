# tray_4_3.py
# SIRIUS LOCAL AI – Windows Tray Icon (v4.3.x)
# Deterministic, safe-mode compatible tray module

from __future__ import annotations

import threading
import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageDraw
import subprocess
import sys
import os
import pathlib

from runtime.runtime_manager import RuntimeManager


class SiriusTray43:
    """
    SIRIUS LOCAL AI — Windows Tray Icon (v4.3.x)

    Features:
        - Launch GUI (safe, sandboxed)
        - Restart SIRIUS runtime (deterministic)
        - Exit tray safely
        - Safe-mode + degraded-mode support
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.safe_mode = False
        self.degraded_mode = False

        try:
            self.rm.initialize()
            self.rm.logger.info("Tray initialized (v4.3.x)")
        except Exception as exc:
            self.degraded_mode = True
            print(f"[TRAY] Initialization failed: {exc}")

        self.icon = pystray.Icon(
            "SIRIUS",
            self._create_icon(),
            "SIRIUS LOCAL AI",
            self._menu()
        )

    # --------------------------------------------------------
    # ICON (4.3.x)
    # --------------------------------------------------------
    def _create_icon(self):
        """Create simple black/white tray icon."""
        img = Image.new("RGB", (32, 32), "black")
        d = ImageDraw.Draw(img)
        d.rectangle([8, 8, 24, 24], fill="white")
        return img

    # --------------------------------------------------------
    # MENU (4.3.x)
    # --------------------------------------------------------
    def _menu(self):
        return (
            Item("Open GUI", self.open_gui),
            Item("Restart SIRIUS", self.restart_sirius),
            Item("Safe Mode", self.toggle_safe_mode),
            Item("Exit Tray", self.exit_app),
        )

    # --------------------------------------------------------
    # ACTIONS (4.3.x)
    # --------------------------------------------------------
    def open_gui(self, icon, item):
        """Launch GUI using python (sandboxed)."""
        if self.safe_mode:
            self.rm.logger.warning("GUI launch blocked: SAFE MODE")
            return

        try:
            python = sys.executable
            gui_path = pathlib.Path(__file__).parent / "gui.py"
            subprocess.Popen([python, str(gui_path)])
            self.rm.logger.info("GUI launched from tray")
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"Tray GUI launch error: {e}")

    def restart_sirius(self, icon, item):
        """Restart entire SIRIUS runtime safely."""
        if self.safe_mode:
            self.rm.logger.warning("Restart blocked: SAFE MODE")
            return

        try:
            python = sys.executable
            sirius_path = pathlib.Path(__file__).parent / "sirius.py"
            subprocess.Popen([python, str(sirius_path)])
            self.rm.logger.info("SIRIUS restarted from tray")
            os._exit(0)
        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"Tray restart error: {e}")

    def toggle_safe_mode(self, icon, item):
        """Toggle safe mode."""
        self.safe_mode = not self.safe_mode
        state = "ON" if self.safe_mode else "OFF"
        self.rm.logger.info(f"Tray safe mode toggled → {state}")

    def exit_app(self, icon, item):
        """Stop tray icon."""
        self.rm.logger.info("Tray exit requested")
        icon.stop()

    # --------------------------------------------------------
    # RUN (4.3.x)
    # --------------------------------------------------------
    def run(self):
        """Run tray icon in background thread."""
        header = "Tray icon running (v4.3.x)"
        if self.safe_mode:
            header += " [SAFE MODE]"
        elif self.degraded_mode:
            header += " [DEGRADED MODE]"

        self.rm.logger.info(header)

        threading.Thread(target=self.icon.run, daemon=True).start()


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    tray = SiriusTray43()
    tray.run()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
