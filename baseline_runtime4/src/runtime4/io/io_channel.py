# Baseline version of IOChannel
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class IOChannel:
    def __init__(self, logger):
        self.logger = logger

    def send(self, data: str) -> bool:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active send logic is implemented here.
        """
        self.logger.log(f"[Baseline] IOChannel.send() called with data: {data}")
        return True

    def receive(self) -> str | None:
        """
        Baseline version:
        Always returns None.
        """
        self.logger.log("[Baseline] IOChannel.receive() called.")
        return None
