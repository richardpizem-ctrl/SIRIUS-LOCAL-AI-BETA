import speech_recognition as sr
from runtime.runtime_manager import RuntimeManager


class SiriusHotword:
    """
    HOTWORD mode for SIRIUS-LOCAL-AI
    - waits for the word "sirius"
    - after activation listens for a command
    - sends the command to the NL Router
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.hotword = "sirius"

    # --------------------------------------------------------
    # SPEECH RECOGNITION
    # --------------------------------------------------------
    def listen(self):
        with self.microphone as source:
            print("🎤 Listening for hotword...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="sk-SK").lower()
            print(f"➡ Recognized: {text}")
            return text
        except:
            return ""

    # --------------------------------------------------------
    # LISTEN FOR COMMAND AFTER HOTWORD
    # --------------------------------------------------------
    def listen_command(self):
        with self.microphone as source:
            print("🎤 Listening for command...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="sk-SK")
            print(f"➡ Command: {text}")
            return text
        except:
            print("❗ Could not understand the command.")
            return None

    # --------------------------------------------------------
    # PROCESS COMMAND
    # --------------------------------------------------------
    def process(self, text):
        if not text:
            return

        result = self.rm.handle_nl(text)
        print("➡ Result:", result)

    # --------------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------------
    def run(self):
        print("🟢 SIRIUS HOTWORD MODE – active")
        print("Say: 'Sirius'")

        while True:
            text = self.listen()

            if self.hotword in text:
                print("🟡 Hotword detected → waiting for command...")
                command = self.listen_command()
                self.process(command)


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------
if __name__ == "__main__":
    hw = SiriusHotword()
    hw.run()
