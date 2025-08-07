# Copyright (c) 2025 CarlosIgRuz. MIT License.

"""Simple intent parser for TaskWhisper."""

from typing import Any, Dict

# Keywords that trigger the CreateAppointment intent.
CREATE_APPOINTMENT_KEYWORDS = {
    "cita",
    "appointment",
    "reserva",
    "agendar",
    "schedule",
}


def parse_intent(text: str) -> Dict[str, Any]:
    """Parse user input and extract a high level intent.

    The parser performs a minimal keyword search to detect the
    ``CreateAppointment`` intent. It returns a dictionary with two keys:
    ``intent`` holding the detected intent name and ``params`` holding any
    parameters (empty for now).
    """
    text_lower = text.lower()
    if any(keyword in text_lower for keyword in CREATE_APPOINTMENT_KEYWORDS):
        return {"intent": "CreateAppointment", "params": {}}
    return {"intent": "Unknown", "params": {}}
