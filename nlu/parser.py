from nlu.intents import Intent


def parse_intent(text: str) -> Intent:
    t = text.lower().strip()

    if not t:
        return Intent.UNKNOWN

    # Window control commands
    if "minimize" in t or "minimise" in t:
        return Intent.MINIMIZE_WINDOW

    if "maximize" in t or "maximise" in t or "make full screen" in t:
        return Intent.MAXIMIZE_WINDOW

    if "close" in t and ("window" in t or "this" in t or "app" in t):
        return Intent.CLOSE_WINDOW

    # Dictation controls
    if "start dictation" in t or "start typing" in t:
        return Intent.START_DICTATION

    if "stop dictation" in t or "stop typing" in t:
        return Intent.STOP_DICTATION

    return Intent.UNKNOWN
