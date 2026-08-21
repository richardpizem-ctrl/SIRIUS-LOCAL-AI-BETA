# AUTONOMY/modules/navigation.py
# PILIER 3 – Autonómia navigácie (SIRIUS 6.x)

SUPPORTED_NAV_TASKS = {
    "OPEN_EXPLORER": "explorer.exe",
    "OPEN_SETTINGS": "ms-settings:",
    "OPEN_CONTROL_PANEL": "control.exe",
    "OPEN_NETWORK_CONNECTIONS": "ncpa.cpl",
    "OPEN_DISK_MANAGEMENT": "diskmgmt.msc",
    "OPEN_DEVICE_MANAGER": "devmgmt.msc"
}

class Navigation:

    def __init__(self):
        pass

    def propose_navigation(self):
        """
        Generuje návrhy navigačných úloh v štandarde SIRIUS 6.x.
        Autonómia nikdy nevykoná akciu sama – len navrhne.
        """
        proposals = []

        for task_key, command in SUPPORTED_NAV_TASKS.items():
            proposals.append({
                "proposal_id": f"nav-{task_key.lower()}",
                "type": "NAVIGATION_TASK",
                "action": "OPEN",
                "target": command,
                "payload": {
                    "task": task_key
                },
                "priority": "LOW"
            })

        return proposals
