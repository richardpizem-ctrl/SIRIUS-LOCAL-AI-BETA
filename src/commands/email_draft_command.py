from commands.base_command import BaseCommand
from email.manager import EmailManager


class EmailDraftCommand(BaseCommand):
    """
    EmailDraftCommand 4.4
    Creates a new email draft using EmailManager with validation,
    snapshot, and structured JSON output.

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
    name = "email-draft"
    description = "Creates a new email draft."
    category = "email"

    required_identity = "OWNER"
    risk_level = 0.4
    capabilities = ["context_read", "context_write", "fs_write"]

    keywords = ["email", "draft", "compose"]
    examples = ["email-draft <to> <subject> <body>"]

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
        if len(args) < 3:
            return {
                "status": "error",
                "message": "Usage: email-draft <to> <subject> <body>"
            }

        to = args[0]
        subject = args[1]
        body = " ".join(args[2:])

        # -----------------------------
        # SNAPSHOT BEFORE CREATION
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # CREATE DRAFT
        # -----------------------------
        draft = self.email_manager.create_draft(
            to=to,
            subject=subject,
            body=body
        )

        # EmailManager may return an error dict
        if isinstance(draft, dict) and draft.get("status") == "error":
            return draft

        # -----------------------------
        # LOG INTO CONTEXT STATE
        # -----------------------------
        self.context.merge({
            "last_email_draft_id": draft["id"],
            "last_email_draft_to": draft["to"],
            "last_email_draft_subject": draft["subject"]
        })

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "message": "Draft created successfully.",
            "draft_id": draft["id"],
            "to": draft["to"],
            "subject": draft["subject"]
        }
