class ConfirmDialog:
    """
    Mock UI Confirm Dialog
    Temporary version – always returns True.
    Will be replaced by a real UI window later.
    """

    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message

    def get_user_confirmation(self) -> bool:
        """
        Temporarily auto-confirms the operation.
        """
        return True
