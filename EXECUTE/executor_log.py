# executor_log.py – jednotný logovací modul pre EXECUTE

import datetime
import os

LOG_PATH = "executor_log.txt"

def write_log(level: str, message: str):
    """
    Zapíše správu do executor_log.txt v jednotnom formáte.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{level}] {message}\n"

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)

def info(message: str):
    write_log("INFO", message)

def warning(message: str):
    write_log("WARNING", message)

def error(message: str):
    write_log("ERROR", message)

def executed(action: str, result: str):
    write_log("EXECUTED", f"{action} → {result}")
