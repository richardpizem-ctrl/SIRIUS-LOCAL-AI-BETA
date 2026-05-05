from .base_command import BaseCommand


class TriageTestCommand(BaseCommand):
    """
    TriageTestCommand 4.0
    Test command for AITE (Automatic Input Triage Engine).

    New in version 4.0:
    - integration with BaseCommand lifecycle
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (filesystem read)
    - NL Router metadata
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "triage-test"
    description = "Tests AITE triage on a given file."
    category = "diagnostics"

    required_identity = "FAMILY"     # safe for everyone
    risk_level = 0.1                 # low risk
    capabilities = ["fs_read"]

    keywords = ["triage", "detect", "file type", "analyze"]
    examples = ["triage-test C:/path/file.png"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, runtime):
        self.runtime = runtime

    # ---------------------------------------------------------
    # EXECUTION (v4.0)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Tests AITE triage on a given file.
        """
        if not args:
            return {
                "status": "error",
                "message": "Usage: triage-test <path>"
            }

        path = args[0]

        try:
            result = self.runtime.aite.process(path)
        except Exception as e:
            return {
                "status": "error",
                "message": "AITE error",
                "exception": str(e)
            }

        return {
            "status": "success",
            "path": path,
            "triage": result
        }
