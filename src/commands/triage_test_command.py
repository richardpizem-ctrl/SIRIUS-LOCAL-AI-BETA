from commands.base_command import BaseCommand


class TriageTestCommand(BaseCommand):
    """
    TriageTestCommand 4.4
    Tests AITE (Automatic Input Triage Engine) on a given file.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic execution contract
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Safe execution via BaseCommand.run()
        - Stable NL Router output
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
    # ---------------------------------------------------------
    name = "triage-test"
    description = "Tests AITE triage on a given file."
    category = "diagnostics"

    required_identity = "FAMILY"     # safe for everyone
    risk_level = 0.1
    capabilities = ["fs_read"]

    keywords = ["triage", "detect", "file type", "analyze"]
    examples = ["triage-test <path>"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, runtime):
        self.runtime = runtime

    # ---------------------------------------------------------
    # EXECUTION (4.4)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Tests AITE triage on a given file.
        Usage:
            triage-test <path>
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if not args:
            return {
                "status": "error",
                "message": "Usage: triage-test <path>"
            }

        path = args[0]

        # -----------------------------
        # AITE PROCESSING
        # -----------------------------
        try:
            result = self.runtime.aite.process(path)
        except Exception as e:
            return {
                "status": "error",
                "message": "AITE error",
                "exception": str(e)
            }

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "path": path,
            "triage": result
        }
