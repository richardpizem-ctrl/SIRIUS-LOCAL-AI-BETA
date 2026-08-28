# Terminal Assistant Rules (SUPER-FINAL)
# Defines allowed, risky, forbidden and confirmation-required terminal commands.

TERMINAL_ASSISTANT_RULES = {

    # ============================================================
    # 🔵 1. POVOLENÉ PRÍKAZY (bez rizika)
    # ============================================================
    # Tieto príkazy sú bezpečné, autonómia ich môže navrhovať bez potvrdenia.
    "allowed": [
        "help",
        "status",
        "scan",
        "validate",
        "detect",
        "dir",
        "type",
        "echo",
        "cls",
        "cd"
    ],

    # ============================================================
    # 🟡 2. RIZIKOVÉ PRÍKAZY (vyžadujú zvýšenú pozornosť)
    # ============================================================
    # Autonómia ich môže navrhnúť, ale COLNÍK musí rozhodnúť.
    "risky": [
        "copy",
        "move",
        "rename",
        "mkdir",
        "rmdir"
    ],

    # ============================================================
    # 🔴 3. ZAKÁZANÉ PRÍKAZY (autonómia ich nesmie ani navrhnúť)
    # ============================================================
    # Tieto príkazy sú blokované už na úrovni TerminalAssistant.
    "forbidden": [
        "delete",
        "format",
        "shutdown",
        "kg_wipe",
        "unsafe_exec",
        "rm -rf",
        "diskpart",
        "mkfs",
        "erase",
        "poweroff"
    ],

    # ============================================================
    # 🟠 4. PRÍKAZY VYŽADUJÚCE POTVRDENIE (COLNÍK rozhoduje)
    # ============================================================
    # Autonómia ich môže navrhnúť, ale nikdy nevykoná.
    "confirmation_required": [
        "copy",
        "move",
        "rename",
        "mkdir",
        "rmdir"
    ]
}
