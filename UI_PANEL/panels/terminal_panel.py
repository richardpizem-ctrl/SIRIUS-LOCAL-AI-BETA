import time
import os
import urllib.request

class TerminalPanel:
    """
    UI PANEL – TERMINAL PANEL
    Spracováva akcie:
    - run_terminal
    - execute_command
    """

    def __init__(self):
        # aktuálny pracovný adresár pre simulovaný shell
        self.current_dir = os.getcwd()

    def handle(self, req: dict) -> dict:
        """
        Spracuje terminálový request.
        Podporované príkazy:
        - echo TEXT
        - ls / dir
        - cd PATH
        - pwd
        - help
        - clear
        - shutdown
        """

        rid = req.get("request_id", "UNKNOWN_ID")
        action = req.get("action", "UNKNOWN_ACTION")
        target = req.get("target", "UNKNOWN_TARGET")
        payload = req.get("payload", {})

        text = payload.get("text", "")
        language = payload.get("language", "SK")

        print(f"[TERMINAL_PANEL] Spúšťam terminálový request: {rid}")
        print(f"  Action: {action}")
        print(f"  Target: {target}")
        print(f"  Payload: {payload}")

        time.sleep(0.3)

        # -----------------------------
        # PARSOVANIE PRÍKAZU
        # -----------------------------
        parts = text.strip().split(" ", 1)
        command = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        output = ""

        # -----------------------------
        # IMPLEMENTÁCIA PRÍKAZOV
        # -----------------------------

        # shutdown
        if command == "shutdown":
            try:
                urllib.request.urlopen("http://localhost:8080/shutdown")
                output = "BACKEND SA VYPÍNA..."
            except Exception as e:
                output = f"CHYBA PRI SHUTDOWN: {e}"

        # echo
        elif command == "echo":
            output = arg

        # ls / dir
        elif command in ["ls", "dir"]:
            try:
                items = os.listdir(self.current_dir)
                output = "\n".join(items)
            except Exception as e:
                output = f"CHYBA: {e}"

        # cd
        elif command == "cd":
            try:
                new_path = arg if arg else self.current_dir
                os.chdir(new_path)
                self.current_dir = os.getcwd()
                output = f"DIR ZMENENÝ NA: {self.current_dir}"
            except Exception as e:
                output = f"CHYBA: {e}"

        # pwd
        elif command == "pwd":
            output = self.current_dir

        # help
        elif command == "help":
            output = (
                "DOSTUPNÉ PRÍKAZY:\n"
                "echo TEXT – vypíše text\n"
                "ls / dir – vypíše obsah adresára\n"
                "cd PATH – zmení adresár\n"
                "pwd – aktuálny adresár\n"
                "clear – vyčistí obrazovku\n"
                "shutdown – vypne backend\n"
                "help – zoznam príkazov"
            )

        # clear
        elif command == "clear":
            output = ""  # UI si to vyčistí samo

        # neznámy príkaz
        else:
            output = f"NEZNÁMY PRÍKAZ: {command}"

        print(f"[TERMINAL_PANEL] Request {rid} spracovaný OK.")

        return {
            "request_id": rid,
            "success": True,
            "module": "terminal",
            "action": action,
            "target": target,
            "output": output,
            "language": language
        }
