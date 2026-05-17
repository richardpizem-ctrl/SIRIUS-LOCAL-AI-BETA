# ============================================================
#  SEND EMAIL (FINAL v4.3 PIPELINE)
# ============================================================

def send_email(self, draft: dict, sender_profile: dict | None = None):
    """
    Final v4.3 send-email pipeline.
    Converts a draft into a sent email, validates it,
    attaches sender profile, timestamps it, stores it,
    and returns a deterministic structured response.

    Improvements in 4.3:
    - deterministic Runtime4 behavior
    - unified validation contract
    - sender-profile normalization
    - consistent metadata fields
    - Self‑Repair 4.4 compatible structure
    """

    # -----------------------------
    # VALIDATE DRAFT FIELDS
    # -----------------------------
    validation = self.validator.validate_full(
        draft.get("to", ""),
        draft.get("subject", ""),
        draft.get("body", "")
    )

    if not validation["all_valid"]:
        return {
            "status": "error",
            "message": "Draft validation failed.",
            "details": validation
        }

    # -----------------------------
    # COPY DRAFT → SENT EMAIL
    # -----------------------------
    sent = copy.deepcopy(draft)
    sent["status"] = "sent"
    sent["sent_at"] = datetime.now().isoformat()

    # -----------------------------
    # ATTACH SENDER PROFILE
    # -----------------------------
    if isinstance(sender_profile, dict):
        sent["sender_profile"] = sender_profile
    else:
        sent["sender_profile"] = {}

    # -----------------------------
    # NORMALIZE OPTIONAL FIELDS
    # -----------------------------
    if "attachments" not in sent:
        sent["attachments"] = []

    if "metadata" not in sent:
        sent["metadata"] = {}

    # -----------------------------
    # STORE SENT EMAIL
    # -----------------------------
    stored = self.storage.save(sent, prefix="sent")

    # -----------------------------
    # SUCCESS RESPONSE
    # -----------------------------
    return {
        "status": "success",
        "message": "Email sent successfully (local send).",
        "email": sent,
        "stored_as": stored
    }
