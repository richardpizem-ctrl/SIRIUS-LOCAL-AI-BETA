class Plugin:
    """
    Fully featured example plugin for SIRIUS-LOCAL-AI.
    Demonstrates all capabilities:
    - NL commands
    - AI tasks
    - Workflow
    - AI Loop rules
    - GUI elements
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL COMMANDS
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "hello plugin": self.say_hello,
            "test plugin": self.test_action,
            "plugin workflow": self.run_workflow_demo
        }

    def say_hello(self, text):
        return "Hello! The plugin is active and responding."

    def test_action(self, text):
        return "The plugin is working correctly – NL command executed."

    def run_workflow_demo(self, text):
        return self.rm.run_workflow("plugin_demo_workflow")

    # --------------------------------------------------------
    # AI TASKS
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "plugin_test_task": self.ai_task_example,
            "plugin_status": self.ai_status
        }

    def ai_task_example(self, params):
        return {
            "status": "OK",
            "message": "AI task from the plugin was executed successfully."
        }

    def ai_status(self, params):
        return {
            "plugin": "example",
            "state": "running",
            "info": "Plugin is running without issues."
        }

    # --------------------------------------------------------
    # WORKFLOWS
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "plugin_demo_workflow",
                "steps": [
                    {"action": "log", "message": "Workflow from plugin started."},
                    {"action": "task", "task": "plugin_test_task"},
                    {"action": "return", "value": "Workflow completed successfully."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "plugin_auto_log",
                "trigger": "interval",
                "interval": 30,
                "action": "plugin_status"
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Plugin Test",
                "action": "plugin_test_task"
            },
            {
                "type": "button",
                "label": "Run workflow",
                "action": "plugin_demo_workflow"
            }
        ]
