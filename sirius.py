# ============================================================
# PATH BOOTSTRAP (musí byť úplne hore, pred všetkými importmi)
# ============================================================
import os
import sys

# Absolútna cesta k priečinku, kde leží tento štartovací skript
root_dir = os.path.dirname(os.path.abspath(__file__))

# Pridaj root do sys.path
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Pridaj src/ ak existuje
src_dir = os.path.join(root_dir, "src")
if os.path.exists(src_dir) and src_dir not in sys.path:
    sys.path.insert(0, src_dir)


# ============================================================
# SIRIUS LOCAL AI – Main Entry Point (v4.5.0 PRO)
# Deterministic, safe-mode compatible bootstrap (Phase‑5 ready)
# ============================================================

from __future__ import annotations

import sys

# Runtime 4.5 line
from runtime.cli_4_5 import SiriusCLI45
from runtime.runtime_manager_4_5 import RuntimeManager45

# Runtime 5.1 line (optional mode)
from runtime5_cli import Runtime5CLI


# ============================================================
# MAIN ENTRY (v4.5.0 PRO)
# ============================================================
def main():
    # --------------------------------------------------------
    # OPTIONAL: Runtime 5.1 MODE
    # --------------------------------------------------------
    if "--runtime5" in sys.argv:
        print("SIRIUS LOCAL AI – Runtime 5.1 MODE")
        print("Type 'exit' to quit.\n")

        cli5 = Runtime5CLI()

        try:
            while True:
                text = input("> ")
                if text.strip().lower() in ("exit", "quit"):
                    break

                # Runtime5 CLI handles commands internally
                cli5.run(["runtime5", text])

        except KeyboardInterrupt:
            print("\n[Runtime5] Shutdown requested.")

        return  # exit after Runtime5 mode

    # --------------------------------------------------------
    # DEFAULT: Runtime 4.5.0 PRO
    # --------------------------------------------------------
    rm = RuntimeManager45()

    safe_mode = False
    degraded_mode = False

    # Runtime initialization
    try:
        rm.initialize()
        rm.logger.info("SIRIUS LOCAL AI – Entry point started (v4.5.0 PRO)")
    except Exception as exc:
        degraded_mode = True
        print(f"[ENTRY] Runtime initialization failed: {exc}")

    # CLI startup
    try:
        cli = SiriusCLI45()
        if safe_mode:
            cli.safe_mode = True
        cli.run(sys.argv)
    except Exception as exc:
        degraded_mode = True
        rm.logger.error(f"[ENTRY] CLI startup error: {exc}")

    # Final log
    if degraded_mode:
        rm.logger.warning("SIRIUS LOCAL AI – Execution finished in DEGRADED MODE")
    else:
        rm.logger.info("SIRIUS LOCAL AI – Execution finished cleanly")


# ============================================================
# EXECUTION
# ============================================================
if __name__ == "__main__":
    main()
