import os
import shutil

class Plugin:
    """
    File Manager plugin for SIRIUS-LOCAL-AI.
    Allows:
    - creating folders
    - moving files
    - deleting files
    - listing directory contents
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL COMMANDS
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "create folder": self.nl_create_folder,
            "move files": self.nl_move_files,
            "delete file": self.nl_delete_file,
            "list directory": self.nl_list_directory
        }

    def nl_create_folder(self, text):
        path = text.strip()
        try:
            os.makedirs(path, exist_ok=True)
            return f"Folder created: {path}"
        except Exception as e:
            return f"Error creating folder: {e}"

    def nl_move_files(self, text):
        try:
            src, dst = text.split("->")
            src = src.strip()
            dst = dst.strip()
            os.makedirs(dst, exist_ok=True)
            for file in os.listdir(src):
                shutil.move(os.path.join(src, file), dst)
            return f"Files moved from {src} to {dst}"
        except Exception as e:
            return f"Error moving files: {e}"

    def nl_delete_file(self, text):
        path = text.strip()
        try:
            os.remove(path)
            return f"File deleted: {path}"
        except Exception as e:
            return f"Error deleting file: {e}"

    def nl_list_directory(self, text):
        path = text.strip()
        try:
            items = os.listdir(path)
            if not items:
                return "Directory is empty."
            return "\n".join(items)
        except Exception as e:
            return f"Error reading directory: {e}"

    # --------------------------------------------------------
    # AI TASKS
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "create_folder": self.ai_create_folder,
            "move_files": self.ai_move_files,
            "delete_file": self.ai_delete_file,
            "list_directory": self.ai_list_directory
        }

    def ai_create_folder(self, params):
        path = params.get("path")
        os.makedirs(path, exist_ok=True)
        return {"status": "OK", "created": path}

    def ai_move_files(self, params):
        src = params.get("src")
        dst = params.get("dst")
        os.makedirs(dst, exist_ok=True)
        for file in os.listdir(src):
            shutil.move(os.path.join(src, file), dst)
        return {"status": "OK", "moved": True}

    def ai_delete_file(self, params):
        path = params.get("path")
        os.remove(path)
        return {"status": "OK", "deleted": path}

    def ai_list_directory(self, params):
        path = params.get("path")
        return {"items": os.listdir(path)}

    # --------------------------------------------------------
    # WORKFLOWS
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "auto_clean_downloads",
                "steps": [
                    {"action": "log", "message": "Cleaning Downloads folder..."},
                    {"action": "task", "task": "list_directory", "params": {"path": "Downloads"}},
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
                "name": "monitor_downloads",
                "trigger": "interval",
                "interval": 60,
                "action": "list_directory",
                "params": {"path": "Downloads"}
            }
        ]

    # --------------------------------------------------------
    # GUI ELEMENTS
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Create folder",
                "action": "create_folder"
            },
            {
                "type": "button",
                "label": "Move files",
                "action": "move_files"
            }
        ]
