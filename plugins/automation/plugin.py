import subprocess
import sys
import os

class Plugin:
    """
    Automation plugin for SIRIUS-LOCAL-AI.
    Allows running shell commands, scripts, and automated tasks.
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL COMMANDS
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "run command": self.nl_run_command,
            "run script": self.nl_run_script
        }

    def nl_run_command(self, text):
        try:
            result = subprocess.check_output(text, shell=True, stderr=subprocess.STDOUT, encoding="utf-8")
            return f"Output:\n{result}"
        except subprocess.CalledProcessError as e:
            return f"Error:\n{e.output}"

    def nl_run_script(self, text):
        script = text.strip()
        if not os.path.exists(script):
            return "Script does not exist."
        try:
            result = subprocess.check_output([sys.executable, script], stderr=subprocess.STDOUT, encoding="utf-8")
            return f"Script output:\n{result}"
        except subprocess.CalledProcessError as e:
            return f"Script error:\n{e.output}"

    # --------------------------------------------------------
    # AI TASKS
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "run_command": self.ai_run_command,
            "run_script": self.ai_run_script
        }

    def ai_run_command(self, params):
        cmd = params.get("cmd")
        if not cmd:
            return {"error": "Missing 'cmd' parameter."}
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, encoding="utf-8")
            return {"status": "OK", "output": result}
        except subprocess.CalledProcessError as e:
            return {"error": e.output}

    def ai_run_script(self, params):
        script = params.get("script")
        if not script or not os.path.exists(script):
            return {"error": "Script not found."}
        try:
            result = subprocess.check_output([sys.executable, script], stderr=subprocess.STDOUT, encoding="utf-8")
            return {"status": "OK", "output": result}
        except subprocess.CalledProcessError as e:
            return {"error": e.output}

    # --------------------------------------------------------
    # WORKFLOWS
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "auto_cleanup",
                "steps": [
                    {"action": "log", "message": "Starting automatic cleanup..."},
                    {"action": "task", "task": "run_command", "params": {"cmd": "echo Cleanup done"}},
                    {"action": "return", "value": "Automation completed."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "automation_heartbeat",
                "trigger": "interval",
                "interval": 240,
                "action": "run_command",
                "params": {"cmd": "echo Heartbeat OK"}
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Run test command",
                "action": "run_command",
                "params": {"cmd": "echo Test OK"}
            },
            {
                "type": "button",
                "label": "Run script",
                "action": "run_script",
                "params": {"script": "test.py"}
            }
        ]
