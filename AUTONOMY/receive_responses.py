# IPC – RECEIVE FROM COLNIK
# Autonómia číta odpovede COLNÍKA

import json
import os

class IPCReceiver:

    def __init__(self, in_path="C:\\SIRIUS_IPC\\colnik_out.json"):
        self.in_path = in_path

    def receive(self):
        """
        Reads COLNIK responses if available.
        """
        if not os.path.exists(self.in_path):
            return []

        try:
            with open(self.in_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print("IPC RECEIVE ERROR:", e)
            return []
