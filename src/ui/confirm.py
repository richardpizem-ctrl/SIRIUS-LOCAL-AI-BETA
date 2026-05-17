# confirm.py
# SIRIUS LOCAL AI – ConfirmDialog 4.3.x
# Deterministic, offline-only confirmation dialog (UI Manager Phase‑4 compatible)

class ConfirmDialog:
    """
    ConfirmDialog 4.3.x

    Responsibilities:
        - Provide deterministic confirmation results
        - Integrate with UI Manager Phase‑4
        - Support safe-mode and degraded-mode
        - Provide structured confirmation package
        - Offline-only, no side-effects

    This is a logic-layer mock.
    The real UI window will be injected by UI Manager Phase‑5.
    """

    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message

        self.safe_mode = False
        self.degraded_mode = False

        # Default behavior (Phase‑4 mock)
        self.auto_confirm = True

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def get_user_confirmation(self) -> dict:
        """
        Return a structured confirmation package.

        In Phase‑4:
            - auto-confirm is used (no real UI window)
            - safe-mode forces denial
            - degraded-mode returns fallback structure
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "confirmed": False,
                "title": self.title,
                "message": self.message,
                "degraded_mode": self.degraded_mode,
            }

        try:
            confirmed = bool(self.auto_confirm)

            return {
                "status": "ok",
                "confirmed": confirmed,
                "title": self.title,
                "message": self.message,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "confirmed": False,
                "title": self.title,
                "message": self.message,
                "exception": str(exc),
                "degraded_mode": True,
            }
