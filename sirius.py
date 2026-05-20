# sirius_4_4.py
# SIRIUS LOCAL AI – Main Entry Point (v4.4.0 PRO)
# Deterministic, safe-mode compatible bootstrap (Phase‑5 ready)

from __future__ import annotations

import sys
from runtime.cli_4_4 import SiriusCLI44
from runtime.runtime_manager_4_4 import RuntimeManager44


# ============================================================
# MAIN ENTRY (v4.4.0 PRO)
# ============================================================
def main():
    # Initialize runtime first (global logger, config, env)
    rm = RuntimeManager44()

    safe_mode = False
    degraded_mode = False

    try:
        rm.initialize()
        rm.logger.info("SIRIUS LOCAL AI – Entry point started (v4.4.0 PRO)")
    except Exception as exc:
        degraded_mode = True
        print(f"[ENTRY] Runtime initialization failed: {exc}")

    # Start CLI (safe-mode aware)
    try:
        cli = SiriusCLI44()
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
