# nlu/intents.py

from enum import Enum, auto


class Intent(Enum):
    """High-level intents Kratos can recognize from your speech."""
    MINIMIZE_WINDOW = auto()
    MAXIMIZE_WINDOW = auto()
    CLOSE_WINDOW = auto()

    START_DICTATION = auto()
    STOP_DICTATION = auto()

    UNKNOWN = auto()
