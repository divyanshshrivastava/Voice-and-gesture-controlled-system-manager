# kratos_io/wake_word.py

"""
Wake-word detection utilities for Kratos.

Instead of requiring an exact match to the string "kratos",
we allow fuzzy matches because STT can mishear it as things like
"creators", "crat", "cratos", etc.
"""

from core.config import HOTWORD
import difflib

# Words that STT often confuses "kratos" with
COMMON_MISHEARINGS = {
    "cratos",
    "creators",
    "crat",
}


def word_is_close_to_hotword(word: str, threshold: float = 0.7) -> bool:
    """
    Returns True if a single word is similar enough to the HOTWORD.
    Uses a simple similarity ratio from difflib.
    """
    word = word.lower()

    # exact or known mishearing
    if word == HOTWORD:
        return True
    if word in COMMON_MISHEARINGS:
        return True

    # fuzzy similarity check
    ratio = difflib.SequenceMatcher(None, word, HOTWORD).ratio()
    return ratio >= threshold


def text_contains_hotword(text: str) -> bool:
    """
    Check if any word in the given text is close enough to the hotword.
    """
    text = text.lower().strip()
    if not text:
        return False

    words = text.split()
    for w in words:
        if word_is_close_to_hotword(w):
            return True

    return False
