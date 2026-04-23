from sqlalchemy import Column, Integer, String
from app.db import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    symptoms = Column(String)
    severity = Column(String)
    queue_position = Column(Integer)

Base.metadata.create_all(engine)