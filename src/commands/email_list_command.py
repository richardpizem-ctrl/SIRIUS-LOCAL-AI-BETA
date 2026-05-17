from commands.base_command import BaseCommand
from email.manager import EmailManager


class EmailListCommand(BaseCommand):
    """
    EmailListCommand 4.3
    Lists stored emails (drafts or sent) using EmailManager.

    Improvements in 4.3:
    - unified metadata contract
    - deterministic behavior for Runtime4
    - safe error handling (via BaseCommand.run)
    - consistent return structure
    - NL Router friendly filtering
    """

    # ---------------------------------------------------------
    # METADATA (v4.3)
    # ---------------------------------------------------------
    name = "email-list"
    description = "Lists email drafts or sent emails."
    category = "email"

    required_identity = "OWNER"
    risk_level = 0.2
    capabilities = ["fs_read"]

    keywords = ["email", "list", "drafts", "sent"]
    examples = ["email-list", "email-list draft", "email-list sent"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context, email_manager: EmailManager):
        self.context = context
        self.email_manager = email_manager

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Lists emails.
        Usage:
            email-list
            email-list draft
            email-list sent
        """

        # -----------------------------
        # STATUS FILTER
        # -----------------------------
        status = None
        if len(args) >= 1:
            arg = args[0].lower()
            if arg in ["draft", "drafts"]:
                status = "draft"
            elif arg in ["sent"]:
                status = "sent"
            else:
                return {
                    "status": "error",
                    "message": "Invalid filter. Use: draft | sent"
                }

        # -----------------------------
        # LOAD EMAILS
        # -----------------------------
        emails = self.email_manager.list_emails(status=status)

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "filter": status or "all",
            "count": len(emails),
            "emails": emails
        }
