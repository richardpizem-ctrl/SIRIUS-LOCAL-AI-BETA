# runtime5/error_handler_5.py

from runtime5.logging_5 import log5

class ErrorHandler5:
    """
    Centralized error handling for Runtime 5.x.
    Ensures the system never crashes and always returns a safe fallback.
    """

    @staticmethod
    def safe_execute(fn, fallback=None):
        try:
            return fn()
        except Exception as e:
            log5(f"[ERROR] {str(e)}")
            return fallback or {
                "error": True,
                "message": "Runtime5 encountered an internal error.",
                "details": str(e)
            }
