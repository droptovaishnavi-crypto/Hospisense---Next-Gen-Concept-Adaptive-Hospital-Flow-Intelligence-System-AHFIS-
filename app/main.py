from fastapi import FastAPI
from app.services.queue_service import add_patient, get_all_patients

app = FastAPI()

# 🔹 Load workflow safely
try:
    from app.workflows.patient_flow import build_workflow
    workflow = build_workflow()
except Exception as e:
    print("Error loading workflow:", e)
    workflow = None


@app.get("/")
def home():
    return {"message": "Hospital AI System Running"}


# 🔹 Process patient + store in DB
@app.post("/process")
def process_patient(data: dict):
    if workflow is None:
        return {"error": "Workflow not initialized. Check logs."}

    result = workflow.invoke(data)

    # 🔥 Save patient to database
    add_patient(result)

    return result


# 🔹 NEW API: View all patients in queue
@app.get("/patients")
def view_patients():
    patients = get_all_patients()
    return patients