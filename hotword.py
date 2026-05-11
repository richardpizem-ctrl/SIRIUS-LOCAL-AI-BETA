import speech_recognition as sr
from runtime.runtime_manager import RuntimeManager


# ============================================================
# SIRIUS HOTWORD ENGINE (v4.0.0)
# ============================================================
class SiriusHotword:
    """
    SIRIUS LOCAL AI — Hotword Listener (v4.0.0)

    Features:
    - Listens for activation word "sirius"
    - After activation listens for a command
    - Sends command to NL Router through RuntimeManager
    - Unified logging and safe error handling
    """

    def __init__(self):
        # Runtime v4
        self.rm = RuntimeManager()
        self.rm.initialize()

        # Speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Hotword
        self.hotword = "sirius"

        self.rm.logger.info("Hotword engine initialized (v4.0.0)")

    # --------------------------------------------------------
    # SPEECH RECOGNITION (v4)
    # --------------------------------------------------------
    def listen(self):
        """Listen for hotword."""
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio, language="sk-SK").lower()
            self.rm.logger.info(f"Recognized: {text}")
            return text

        except Exception as e:
            self.rm.logger.warning(f"Hotword listen error: {e}")
            return ""

    # --------------------------------------------------------
    # LISTEN FOR COMMAND (v4)
    # --------------------------------------------------------
    def listen_command(self):
        """Listen for command after hotword."""
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio, language="sk-SK")
            self.rm.logger.info(f"Command recognized: {text}")
            return text

        except Exception as e:
            self.rm.logger.error(f"Command recognition error: {e}")
            return None

    # --------------------------------------------------------
    # PROCESS COMMAND (v4)
    # --------------------------------------------------------
    def process(self, text):
        """Send recognized text to NL Router."""
        if not text:
            return

        try:
            result = self.rm.handle_nl(text)
            self.rm.logger.info(f"NL result: {result}")
        except Exception as e:
            self.rm.logger.error(f"NL processing error: {e}")

    # --------------------------------------------------------
    # MAIN LOOP (v4)
    # --------------------------------------------------------
    def run(self):
        self.rm.logger.info("SIRIUS HOTWORD MODE — active (v4.0.0)")
        self.rm.logger.info("Waiting for hotword: 'sirius'")

        while True:
            text = self.listen()

            if self.hotword in text:
                self.rm.logger.info("Hotword detected → listening for command")
                command = self.listen_command()
                self.process(command)


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    hw = SiriusHotword()
    hw.run()
