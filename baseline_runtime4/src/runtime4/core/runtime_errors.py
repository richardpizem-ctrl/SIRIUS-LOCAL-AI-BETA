# Baseline version of RuntimeErrors
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class RuntimeErrors:
    def __init__(self):
        self.errors = []

    def add(self, message: str) -> None:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active error handling logic is implemented here.
        """
        self.errors.append(message)

    def get_all(self) -> list:
        """
        Baseline version:
        Returns the stored list without processing.
        """
        return self.errors
