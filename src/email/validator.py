import re


class EmailValidator:
    """
    EmailValidator 4.5
    Provides validation utilities for email addresses, subjects,
    body text, and attachment paths in a deterministic and safe way.

    Updated in 4.5:
        - Deterministic Runtime4.5 behavior
        - Normalized whitespace handling (unchanged)
        - Strict type validation (unchanged)
        - Stable output contract for EmailManager 4.5
        - Self‑Repair Layer 4.5 compatible structure
        - Metadata version bumped to 4.5
    """

    # ---------------------------------------------------------
    # EMAIL ADDRESS VALIDATION
    # ---------------------------------------------------------
    EMAIL_REGEX = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def validate_email(self, email: str) -> bool:
        """
        Validates an email address format.
        Deterministic and safe.
        """
        if not isinstance(email, str):
            return False

        email = email.strip()
        if len(email) == 0:
            return False

        return bool(self.EMAIL_REGEX.match(email))

    # ---------------------------------------------------------
    # SUBJECT VALIDATION
    # ---------------------------------------------------------
    def validate_subject(self, subject: str) -> bool:
        """
        Validates subject length and type.
        Deterministic and safe.
        """
        if not isinstance(subject, str):
            return False

        subject = subject.strip()
        if len(subject) == 0:
            return False

        if len(subject) > 300:
            return False

        return True

    # ---------------------------------------------------------
    # BODY VALIDATION
    # ---------------------------------------------------------
    def validate_body(self, body: str) -> bool:
        """
        Validates email body text.
        Deterministic and safe.
        """
        if not isinstance(body, str):
            return False

        body = body.strip()
        if len(body) == 0:
            return False

        return True

    # ---------------------------------------------------------
    # ATTACHMENT VALIDATION
    # ---------------------------------------------------------
    def validate_attachment(self, path: str) -> bool:
        """
        Validates attachment path format.
        Deterministic and safe.
        """
        if not isinstance(path, str):
            return False

        path = path.strip()
        if len(path) == 0:
            return False

        return True

    # ---------------------------------------------------------
    # FULL EMAIL VALIDATION
    # ---------------------------------------------------------
    def validate_full(self, to: str, subject: str, body: str) -> dict:
        """
        Validates all components of an email.
        Returns a dict with validation results.
        Deterministic output for Runtime4.5.
        """
        email_ok = self.validate_email(to)
        subject_ok = self.validate_subject(subject)
        body_ok = self.validate_body(body)

        return {
            "email_valid": email_ok,
            "subject_valid": subject_ok,
            "body_valid": body_ok,
            "all_valid": email_ok and subject_ok and body_ok,
            "validator_version": "4.5"
        }
