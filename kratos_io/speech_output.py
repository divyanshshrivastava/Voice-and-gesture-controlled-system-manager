# kratos_io/speech_output.py

import pyttsx3
from core import config


class KratosVoice:
    """
    Very simple, robust TTS wrapper.

    To avoid weird pyttsx3 issues where only the first utterance
    is spoken, we create a *fresh* engine on every call to say().
    """

    def __init__(self):
        # You can keep global settings here if needed later
        self.rate = 170
        self.volume = 1.0

    def _create_engine(self):
        """Create and configure a new pyttsx3 engine instance."""
        try:
            engine = pyttsx3.init(driverName="sapi5")
        except Exception:
            engine = pyttsx3.init()

        engine.setProperty("rate", self.rate)
        engine.setProperty("volume", self.volume)

        # Try to pick a "non-weird" voice (often male on Windows)
        voices = engine.getProperty("voices")
        for v in voices:
            name = v.name.lower()
            # crude filter; you can customize this later
            if "zira" not in name:
                engine.setProperty("voice", v.id)
                break

        return engine

    def say(self, text: str):
        """Speak the given text out loud."""
        if config.DEBUG:
            print(f"[Kratos says]: {text}")

        engine = self._create_engine()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        # Let engine be garbage-collected; no reuse


# Single shared interface object (but it recreates engine for each call)
kratos_voice = KratosVoice()
