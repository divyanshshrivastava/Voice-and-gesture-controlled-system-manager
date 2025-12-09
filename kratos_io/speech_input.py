# kratos_io/speech_input.py

import speech_recognition as sr
from core import config
from io import TextIOBase

recognizer = sr.Recognizer()


def listen_once() -> str:
    """
    Listens to the microphone once and returns detected speech as text.
    Blocking call — Kratos will wait until you say something.
    """
    with sr.Microphone() as source:
        if config.DEBUG:
            print("[Kratos] Listening for speech...")

        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        if config.DEBUG:
            print(f"[STT Raw]: {text}")
        return text.lower()

    except sr.UnknownValueError:
        if config.DEBUG:
            print("[STT] Could not understand audio.")
        return ""

    except sr.RequestError as e:
        print(f"[STT] Error while calling recognition service: {e}")
        return ""
