from commands.base_command import BaseCommand
from email.manager import EmailManager


class EmailDeleteCommand(BaseCommand):
    """
    EmailDeleteCommand 4.4
    Deletes an email (draft or sent) by ID using EmailManager.

    New in 4.4:
        - Integrity Hooks (Self‑Repair Layer 4.4)
        - Health Metadata
        - Deterministic execution contract
        - Extended audit (identity, params, risk, capabilities)
        - Unified error model
        - Safe execution via BaseCommand.run()
    """

    # ---------------------------------------------------------
    # METADATA (v4.4)
    # ---------------------------------------------------------
    name = "email-delete"
    description = "Deletes an email draft or sent email by ID."
    category = "email"

    required_identity = "OWNER"
    risk_level = 0.5
    capabilities = ["fs_write"]

    keywords = ["email", "delete", "remove"]
    examples = ["email-delete <email_id>"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context, email_manager: EmailManager):
        self.context = context
        self.email_manager = email_manager

    # ---------------------------------------------------------
    # EXECUTION (deterministic)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 1:
            return {
                "status": "error",
                "message": "Usage: email-delete <email_id>"
            }

        email_id = args[0]

        # -----------------------------
        # SNAPSHOT BEFORE DELETE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # DELETE EMAIL
        # -----------------------------
        success = self.email_manager.delete_email(email_id)

        if not success:
            return {
                "status": "error",
                "message": f"Email '{email_id}' not found."
            }

        # -----------------------------
        # LOG INTO CONTEXT STATE
        # -----------------------------
        self.context.merge({
            "last_email_deleted_id": email_id
        })

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "message": f"Email '{email_id}' deleted successfully.",
            "email_id": email_id
        }
