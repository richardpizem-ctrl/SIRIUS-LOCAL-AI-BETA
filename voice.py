import speech_recognition as sr

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter


# ============================================================
# SIRIUS VOICE CONTROL (v4.0.0)
# ============================================================
class SiriusVoice:
    """
    SIRIUS LOCAL AI — Voice Control (v4.0.0)

    Features:
    - Listens to microphone
    - Recognizes Slovak speech
    - Sends text to NL Router v4
    - Unified logging and safe error handling
    """

    def __init__(self):
        # ----------------------------------------------------
        # BOOTSTRAP RUNTIME v4
        # ----------------------------------------------------
        self.runtime = RuntimeManager()
        self.runtime.initialize()

        # Plugins
        self.plugins = PluginLoader(self.runtime)
        self.plugins.load_plugins()

        # NL Router v4
        self.router = NaturalLanguageRouter(self.runtime, self.plugins)
        self.router.initialize()

        # Speech Recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.runtime.logger.info("Voice engine initialized (v4.0.0)")

    # --------------------------------------------------------
    # SPEECH RECOGNITION (v4)
    # --------------------------------------------------------
    def listen(self):
        """Listen to microphone and return recognized text."""
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio, language="sk-SK")
            self.runtime.logger.info(f"Recognized: {text}")
            return text

        except sr.UnknownValueError:
            self.runtime.logger.warning("Voice: Could not understand speech")
            return None

        except sr.RequestError as e:
            self.runtime.logger.error(f"Voice: Speech recognition service error: {e}")
            return None

        except Exception as e:
            self.runtime.logger.error(f"Voice: Unexpected error: {e}")
            return None

    # --------------------------------------------------------
    # PROCESS COMMAND (v4)
    # --------------------------------------------------------
    def process(self, text):
        """Send recognized text to NL Router v4."""
        if not text:
            return

        try:
            result = self.router.route(text)
            self.runtime.logger.info(f"Voice NL result: {result}")
        except Exception as e:
            self.runtime.logger.error(f"Voice NL processing error: {e}")

    # --------------------------------------------------------
    # MAIN LOOP (v4)
    # --------------------------------------------------------
    def run(self):
        """Continuous voice listening loop."""
        self.runtime.logger.info("SIRIUS Voice Control — active (v4.0.0)")
        self.runtime.logger.info("Listening for commands...")

        while True:
            text = self.listen()
            self.process(text)


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    voice = SiriusVoice()
    voice.run()
