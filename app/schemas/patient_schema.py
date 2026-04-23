from pydantic import BaseModel

class Patient(BaseModel):
    symptoms: str