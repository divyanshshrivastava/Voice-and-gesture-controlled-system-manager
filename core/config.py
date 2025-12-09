# core/config.py

"""
Central configuration for Kratos.

Anything that feels like a "setting" or "tunable value"
should live here instead of being hard-coded everywhere.
"""

# The word you say to wake Kratos
HOTWORD = "kratos"

# How long (in seconds) Kratos should stay in "active listening"
# mode after the last command before auto-timing out.
LISTEN_TIMEOUT_SECONDS = 8

# Turn this on while developing to get extra prints/logging
DEBUG = True
