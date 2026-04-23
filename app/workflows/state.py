from typing import TypedDict

class PatientState(TypedDict):
    symptoms: str
    severity: str
    load: int
    queue_position: int