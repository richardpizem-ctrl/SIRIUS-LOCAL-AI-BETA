# executor_rules.py – bezpečnostné pravidlá pre EXECUTE modul

SAFE_ACTIONS = {
    "DUPLICATE_FOUND",
    "OPTIMIZE_RAM",
    "OPTIMIZE_CPU",
    "CLEAN_DISK"
}

DANGEROUS_ACTIONS = {
    "EXECUTE",
    "DELETE_FILE",
    "MOVE_FILE",
    "WRITE_SYSTEM",
    "MODIFY_CONFIG",
    "SHUTDOWN",
    "RESTART"
}

def is_action_safe(action: str) -> bool:
    """
    Vráti True, ak je akcia bezpečná.
    Vráti False, ak je akcia riziková alebo neznáma.
    """

    # Bezpečné akcie – povolené
    if action in SAFE_ACTIONS:
        return True

    # Rizikové akcie – zakázané
    if action in DANGEROUS_ACTIONS:
        return False

    # Neznáme akcie – automaticky zakázať
    return False
