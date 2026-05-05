import speech_recognition as sr

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter


class SiriusVoice:
    """
    Voice control for SIRIUS LOCAL AI – v2.0.0
    - listens to the microphone
    - recognizes speech
    - sends text to NL Router 2.0
    """

    def __init__(self):
        # --- BOOTSTRAP RUNTIME 2.0 ---
        self.runtime = RuntimeManager()
        self.runtime.initialize()

        # Plugins
        self.plugins = PluginLoader(self.runtime)
        self.plugins.load_all()

        # NL Router 2.0
        self.router = NaturalLanguageRouter(self.runtime, self.plugins)
        self.router.initialize()

        # Speech Recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    # --------------------------------------------------------
    # SPEECH RECOGNITION
    # --------------------------------------------------------
    def listen(self):
        """
        Listens to the microphone and returns recognized text.
        """
        with self.microphone as source:
            print("🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="sk-SK")
            print(f"➡ Recognized: {text}")
            return text

        except sr.UnknownValueError:
            print("❗ I did not understand.")
            return None

        except sr.RequestError:
            print("❗ Speech recognition service error.")
            return None

    # --------------------------------------------------------
    # PROCESS COMMAND
    # --------------------------------------------------------
    def process(self, text):
        """
        Sends recognized text to NL Router 2.0.
        """
        if not text:
            return

        try:
            result = self.router.route(text)
        except Exception as e:
            result = f"Error: {e}"

        print("➡ Result:", result)

    # --------------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------------
    def run(self):
        """
        Infinite loop – listens to voice and processes commands.
        """
        print("🎙️ SIRIUS Voice Control – active")
        print("Say a command...")

        while True:
            text = self.listen()
            self.process(text)


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------
if __name__ == "__main__":
    voice = SiriusVoice()
    voice.run()
