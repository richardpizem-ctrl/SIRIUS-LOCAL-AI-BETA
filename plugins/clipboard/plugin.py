import pyperclip

class Plugin:
    """
    Clipboard plugin for SIRIUS-LOCAL-AI.
    Allows reading and writing text to the system clipboard.
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL COMMANDS
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "copy": self.nl_copy,
            "paste": self.nl_paste,
            "clipboard": self.nl_read_clipboard
        }

    def nl_copy(self, text):
        pyperclip.copy(text)
        return f"Copied to clipboard: {text}"

    def nl_paste(self, text):
        content = pyperclip.paste()
        return f"From clipboard: {content}"

    def nl_read_clipboard(self, text):
        content = pyperclip.paste()
        return f"Clipboard contains: {content}"

    # --------------------------------------------------------
    # AI TASKS
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "clipboard_copy": self.ai_copy,
            "clipboard_paste": self.ai_paste,
            "clipboard_read": self.ai_read
        }

    def ai_copy(self, params):
        text = params.get("text", "")
        pyperclip.copy(text)
        return {"status": "OK", "copied": text}

    def ai_paste(self, params):
        content = pyperclip.paste()
        return {"status": "OK", "content": content}

    def ai_read(self, params):
        content = pyperclip.paste()
        return {"clipboard": content}

    # --------------------------------------------------------
    # WORKFLOWS
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "clipboard_log",
                "steps": [
                    {"action": "log", "message": "Reading clipboard content..."},
                    {"action": "task", "task": "clipboard_read"},
                    {"action": "return", "value": "Done."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP RULES
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "clipboard_monitor",
                "trigger": "interval",
                "interval": 90,
                "action": "clipboard_read",
                "params": {}
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Copy text",
                "action": "clipboard_copy",
                "params": {"text": "Hello world"}
            },
            {
                "type": "button",
                "label": "Paste from clipboard",
                "action": "clipboard_paste"
            },
            {
                "type": "button",
                "label": "Show clipboard",
                "action": "clipboard_read"
            }
        ]
