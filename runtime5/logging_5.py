# runtime5/logging_5.py

import datetime

def log5(message: str):
    """
    Simple logging function for Runtime 5.x.
    """
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[RUNTIME5 {timestamp}] {message}")
