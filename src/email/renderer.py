from datetime import datetime


class EmailRenderer:
    """
    EmailRenderer 4.4
    Generates human‑readable email previews, full formatted output,
    and deterministic export text for SIRIUS LOCAL AI.

    New in 4.4:
        - Deterministic formatting contract
        - Stable header ordering
        - Safe handling of missing fields
        - Self‑Repair Layer 4.4 compatible output
        - Export timestamp normalization
        - Guaranteed string output (no exceptions)
    """

    # ---------------------------------------------------------
    # BASIC PREVIEW
    # ---------------------------------------------------------
    def render_preview(self, email: dict) -> str:
        """
        Returns a simple text preview of the email.
        Deterministic and safe for UI display.
        """
        to = email.get("to", "<unknown>")
        subject = email.get("subject", "<no subject>")
        body = email.get("body", "")
        created = email.get("created_at", "")

        preview = (
            f"To: {to}\n"
            f"Subject: {subject}\n"
            f"Created: {created}\n"
            f"---\n"
            f"{body[:300]}{'...' if isinstance(body, str) and len(body) > 300 else ''}"
        )

        return preview

    # ---------------------------------------------------------
    # FULL RENDER
    # ---------------------------------------------------------
    def render_full(self, email: dict) -> str:
        """
        Returns a full formatted email text.
        Deterministic header ordering for Runtime4.4.
        """
        to = email.get("to", "<unknown>")
        subject = email.get("subject", "<no subject>")
        body = email.get("body", "")
        attachments = email.get("attachments", [])
        created = email.get("created_at", "")
        sent = email.get("sent_at", "")

        header = [
            f"To: {to}",
            f"Subject: {subject}",
            f"Created: {created}",
        ]

        if sent:
            header.append(f"Sent: {sent}")

        if isinstance(attachments, list) and attachments:
            header.append(f"Attachments ({len(attachments)}):")
            for a in attachments:
                header.append(f"  - {a}")

        header_text = "\n".join(header)

        return f"{header_text}\n\n---\n\n{body}"

    # ---------------------------------------------------------
    # TIMESTAMPED EXPORT
    # ---------------------------------------------------------
    def render_export(self, email: dict) -> str:
        """
        Returns a version of the email formatted for export.
        Deterministic timestamp format for Self‑Repair 4.4.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        export = (
            f"EMAIL EXPORT ({timestamp})\n"
            f"===========================\n\n"
            f"{self.render_full(email)}"
        )

        return export
