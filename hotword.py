# hotword_4_3.py
# SIRIUS LOCAL AI – Hotword Listener (v4.3.x)
# Deterministic, safe-mode compatible, sandboxed hotword engine

from __future__ import annotations

import speech_recognition as sr
from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader_4_3 import PluginLoader43
from runtime.nl_router_4_3 import NaturalLanguageRouter43


class SiriusHotword43:
    """
    SIRIUS LOCAL AI — Hotword Listener (v4.3.x)

    Features:
        - Listens for activation word "sirius"
        - After activation listens for a command
        - Sends command to NL Router 4.3
        - Safe-mode + degraded-mode support
        - Deterministic, isolated error handling
        - Self‑Repair 4.4 ready
    """

    def __init__(self):
        # Runtime bootstrap
        self.runtime = RuntimeManager()
        self.safe_mode = False
        self.degraded_mode = False

        try:
            self.runtime.initialize()
        except Exception as exc:
            self.degraded_mode = True
            print(f"[HOTWORD] Runtime init failed: {exc}")

        # Plugins
        try:
            self.plugins = PluginLoader43(self.runtime)
            self.plugins.load_all()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] Plugin load error: {exc}")

        # NL Router
        try:
            self.router = NaturalLanguageRouter43(self.runtime, self.plugins)
            self.router.initialize()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] NL Router init error: {exc}")

        # Speech Recognition
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] Microphone init error: {exc}")

        # Hotword
        self.hotword = "sirius"

        self.runtime.logger.info("Hotword engine initialized (v4.3.x)")

    # --------------------------------------------------------
    # SPEECH RECOGNITION (4.3.x)
    # --------------------------------------------------------
    def listen(self):
        """Listen for hotword."""
        if self.safe_mode:
            return ""

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio, language="sk-SK").lower()
            self.runtime.logger.info(f"[HOTWORD] Recognized: {text}")
            return text

        except sr.UnknownValueError:
            self.runtime.logger.warning("[HOTWORD] Could not understand speech")
            return ""

        except sr.RequestError as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] Speech recognition service error: {e}")
            return ""

        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] Unexpected error: {e}")
            return ""

    # --------------------------------------------------------
    # LISTEN FOR COMMAND (4.3.x)
    # --------------------------------------------------------
    def listen_command(self):
        """Listen for command after hotword."""
        if self.safe_mode:
            return None

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio, language="sk-SK")
            self.runtime.logger.info(f"[HOTWORD] Command recognized: {text}")
            return text

        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] Command recognition error: {e}")
            return None

    # --------------------------------------------------------
    # PROCESS COMMAND (4.3.x)
    # --------------------------------------------------------
    def process(self, text):
        """Send recognized text to NL Router 4.3."""
        if not text:
            return

        if self.safe_mode:
            self.runtime.logger.warning("[HOTWORD] NL routing blocked: SAFE MODE")
            return

        try:
            result = self.router.route(text)
            self.runtime.logger.info(f"[HOTWORD] NL result: {result}")
        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] NL processing error: {e}")

    # --------------------------------------------------------
    # MAIN LOOP (4.3.x)
    # --------------------------------------------------------
    def run(self):
        header = "SIRIUS HOTWORD MODE — active (v4.3.x)"
        if self.safe_mode:
            header += " [SAFE MODE]"
        elif self.degraded_mode:
            header += " [DEGRADED MODE]"

        self.runtime.logger.info(header)
        self.runtime.logger.info("Waiting for hotword: 'sirius'")

        try:
            while True:
                text = self.listen()

                if self.hotword in text:
                    self.runtime.logger.info("[HOTWORD] Hotword detected → listening for command")
                    command = self.listen_command()
                    self.process(command)

        except KeyboardInterrupt:
            self.runtime.logger.info("[HOTWORD] Shutdown requested (KeyboardInterrupt)")

        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[HOTWORD] Main loop error: {e}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    hw = SiriusHotword43()
    hw.run()
