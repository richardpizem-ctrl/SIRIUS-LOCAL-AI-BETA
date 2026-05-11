from dearpygui.core import *
from dearpygui.simple import *

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter


# ============================================================
# SIRIUS GUI (v4.0.0)
# ============================================================
class SiriusGUI:
    """
    SIRIUS LOCAL AI — Graphical User Interface (v4.0.0)

    Features:
    - Natural language input
    - Direct AI task execution
    - Plugin‑powered actions
    - Unified logging and runtime integration
    """

    def __init__(self):
        # ----------------------------------------------------
        # BOOTSTRAP RUNTIME v4
        # ----------------------------------------------------
        self.runtime = RuntimeManager()
        self.runtime.initialize()

        # Plugins (v4)
        self.plugins = PluginLoader(self.runtime)
        self.plugins.load_all()

        # NL Router (v4)
        self.router = NaturalLanguageRouter(self.runtime, self.plugins)
        self.router.initialize()

        self.runtime.logger.info("GUI initialized (v4.0.0)")

    # --------------------------------------------------------
    # GUI LOGIC (v4)
    # --------------------------------------------------------
    def send_nl(self, sender, data):
        """Process natural language input."""
        text = get_value("##input")
        if not text.strip():
            return

        try:
            result = self.router.route(text)
            add_text(f"> {text}", parent="Log")
            add_text(str(result), parent="Log")
        except Exception as e:
            self.runtime.logger.error(f"NL error: {e}")
            add_text(f"Error: {e}", parent="Log")

        set_value("##input", "")

    def run_ai_task(self, sender, data):
        """Execute AI task from GUI button."""
        task_name = data.get("task")
        params = data.get("params", {})

        try:
            result = self.runtime.handle_ai_task(task_name, params)
        except Exception as e:
            self.runtime.logger.error(f"AI task error: {e}")
            result = f"Error: {e}"

        add_text(str(result), parent="Log")

    # --------------------------------------------------------
    # GUI WINDOW (v4)
    # --------------------------------------------------------
    def run(self):
        self.runtime.logger.info("Starting GUI window")

        with window("SIRIUS LOCAL AI – GUI (v4.0.0)", width=650, height=520):

            add_text("SIRIUS – Local AI Runtime (v4.0.0)")
            add_separator()

            add_input_text("##input", label="Command", width=450)
            add_button("Send", callback=self.send_nl)

            add_separator()
            add_text("Quick actions:")

            add_button(
                "Snap VS Code Left",
                callback=self.run_ai_task,
                callback_data={"task": "snap_left", "params": {"app": "code.exe"}}
            )

            add_button(
                "Snap VS Code Right",
                callback=self.run_ai_task,
                callback_data={"task": "snap_right", "params": {"app": "code.exe"}}
            )

            add_separator()
            add_text("Log:")
            add_child("Log", width=600, height=260)

        start_dearpygui()


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    gui = SiriusGUI()
    gui.run()
