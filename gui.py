# gui.py
# SIRIUS LOCAL AI – Graphical User Interface (v4.5.0 PRO)
# Deterministic, safe‑mode compatible GUI front‑end (Phase‑5 ready, Runtime 4.5 line)

from __future__ import annotations

from dearpygui.core import *
from dearpygui.simple import *

from runtime.runtime_manager_4_5 import RuntimeManager45
from runtime.plugin_loader_4_5 import PluginLoader45
from runtime.nl_router_4_5 import NaturalLanguageRouter45


class SiriusGUI45:
    """
    SIRIUS LOCAL AI — Graphical User Interface (v4.5.0 PRO)

    Features:
        - Natural language input
        - Direct AI task execution
        - Plugin-powered actions
        - Safe-mode + degraded-mode support
        - Deterministic, isolated error handling
        - Phase‑5 ready (separate Runtime5 line)
    """

    def __init__(self) -> None:
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        self.runtime: RuntimeManager45 | None = None
        self.plugins: PluginLoader45 | None = None
        self.router: NaturalLanguageRouter45 | None = None

        # ----------------------------------------------------
        # Runtime bootstrap (Runtime 4.5 line)
        # ----------------------------------------------------
        try:
            self.runtime = RuntimeManager45()
            self.runtime.initialize()
        except Exception as exc:
            self.degraded_mode = True
            print(f"[GUI] Runtime init failed: {exc}")
            # bez runtime nemá zmysel pokračovať, ale GUI necháme žiť v degraded mode

        # Plugins
        if self.runtime is not None:
            try:
                self.plugins = PluginLoader45(self.runtime)
                self.plugins.load_all()
            except Exception as exc:
                self.degraded_mode = True
                self.runtime.logger.error(f"[GUI] Plugin load error: {exc}")

        # NL Router
        if self.runtime is not None and self.plugins is not None:
            try:
                self.router = NaturalLanguageRouter45(self.runtime, self.plugins)
                self.router.initialize()
            except Exception as exc:
                self.degraded_mode = True
                self.runtime.logger.error(f"[GUI] NL Router init error: {exc}")

        if self.runtime is not None:
            self.runtime.logger.info("GUI initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # GUI LOGIC (4.5.0 PRO)
    # --------------------------------------------------------
    def send_nl(self, sender, data) -> None:
        """Process natural language input."""
        if self.safe_mode:
            add_text("[SAFE MODE] NL routing disabled", parent="Log")
            return

        if self.router is None or self.runtime is None:
            add_text("[ERROR] NL router not available", parent="Log")
            return

        text = get_value("##input")
        if not text or not text.strip():
            return

        try:
            result = self.router.route(text)
            add_text(f"> {text}", parent="Log")
            add_text(str(result), parent="Log")
        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[GUI] NL error: {e}")
            add_text(f"Error: {e}", parent="Log")

        set_value("##input", "")

    def run_ai_task(self, sender, data) -> None:
        """Execute AI task from GUI button."""
        if self.safe_mode:
            add_text("[SAFE MODE] AI tasks disabled", parent="Log")
            return

        if self.runtime is None:
            add_text("[ERROR] Runtime not available", parent="Log")
            return

        task_name = data.get("task") if isinstance(data, dict) else None
        params = data.get("params", {}) if isinstance(data, dict) else {}

        if not task_name:
            add_text("[ERROR] No task specified", parent="Log")
            return

        try:
            result = self.runtime.handle_ai_task(task_name, params)
        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[GUI] AI task error: {e}")
            result = f"Error: {e}"

        add_text(str(result), parent="Log")

    # --------------------------------------------------------
    # GUI WINDOW (4.5.0 PRO)
    # --------------------------------------------------------
    def run(self) -> None:
        header = "SIRIUS LOCAL AI – GUI (v4.5.0 PRO)"
        if self.safe_mode:
            header += " [SAFE MODE]"
        elif self.degraded_mode:
            header += " [DEGRADED MODE]"

        if self.runtime is not None:
            self.runtime.logger.info("Starting GUI window")

        with window(header, width=650, height=520):

            add_text(header)
            add_separator()

            add_input_text("##input", label="Command", width=450)
            add_button("Send", callback=self.send_nl)

            add_separator()
            add_text("Quick actions:")

            add_button(
                "Snap VS Code Left",
                callback=self.run_ai_task,
                callback_data={"task": "snap_left", "params": {"app": "code.exe"}},
            )

            add_button(
                "Snap VS Code Right",
                callback=self.run_ai_task,
                callback_data={"task": "snap_right", "params": {"app": "code.exe"}},
            )

            add_separator()
            add_text("Log:")
            add_child("Log", width=600, height=260)

        start_dearpygui()

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self) -> None:
        self.safe_mode = True

    def exit_safe_mode(self) -> None:
        self.safe_mode = False


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    gui = SiriusGUI45()
    gui.run()
