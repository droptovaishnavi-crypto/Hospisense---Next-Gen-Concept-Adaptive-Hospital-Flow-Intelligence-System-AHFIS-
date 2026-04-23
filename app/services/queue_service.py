from app.models.patient import Patient
from app.db import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


def add_patient(data):
    session = Session()

    patient = Patient(
        symptoms=data.get("symptoms"),
        severity=data.get("severity"),
        queue_position=data.get("queue_position")
    )

    session.add(patient)
    session.commit()
    session.close()

    return {"message": "Patient added"}


def get_all_patients():
    session = Session()

    patients = session.query(Patient).all()

    result = []
    for p in patients:
        result.append({
            "id": p.id,
            "symptoms": p.symptoms,
            "severity": p.severity,
            "queue_position": p.queue_position
        })

    session.close()
    return result