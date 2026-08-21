# TERMINAL ASSISTANT – AUTONOMY 6.x
# Generuje návrhy terminálových príkazov pre COLNÍK

from core.json_format import make_request

class TerminalAssistant:

    def __init__(self):
        pass

    def propose_terminal_open(self):
        """
        Návrh na otvorenie terminálu.
        """
        return [
            make_request({
                "proposal_id": "term-open",
                "action": "OPEN",
                "target": "cmd.exe",
                "payload": {},
                "priority": "LOW"
            })
        ]

    def propose_kill_process(self, process_name):
        """
        Návrh na ukončenie procesu.
        """
        return [
            make_request({
                "proposal_id": "term-kill",
                "action": "EXECUTE",
                "target": f"taskkill /F /IM {process_name}",
                "payload": {"process": process_name},
                "priority": "MEDIUM"
            })
        ]

    def propose_disk_cleanup(self, path):
        """
        Návrh na vyčistenie priečinka.
        """
        return [
            make_request({
                "proposal_id": "term-clean",
                "action": "EXECUTE",
                "target": f"del /Q \"{path}\\*.*\"",
                "payload": {"path": path},
                "priority": "MEDIUM"
            })
        ]

    def propose_move(self, src, dst):
        """
        Návrh na presun súboru.
        """
        return [
            make_request({
                "proposal_id": "term-move",
                "action": "EXECUTE",
                "target": f"move \"{src}\" \"{dst}\"",
                "payload": {"src": src, "dst": dst},
                "priority": "MEDIUM"
            })
        ]
