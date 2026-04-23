import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Hospital AI Dashboard", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏥 Hospital AI")
page = st.sidebar.radio("Navigation", ["Dashboard", "Add Patient", "Queue View"])

# ---------------- STYLES ----------------
def severity_color(severity):
    if severity == "CRITICAL":
        return "red"
    elif severity == "URGENT":
        return "orange"
    elif severity == "NORMAL":
        return "green"
    else:
        return "gray"

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.title("📊 Hospital Dashboard")

    response = requests.get("http://127.0.0.1:8000/patients")

    if response.status_code == 200:
        patients = response.json()

        if len(patients) == 0:
            st.info("No data available")
        else:
            df = pd.DataFrame(patients)

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Patients", len(df))
            col2.metric("Critical Cases", len(df[df["severity"] == "CRITICAL"]))
            col3.metric("Urgent Cases", len(df[df["severity"] == "URGENT"]))

            st.write("### Severity Distribution")
            st.bar_chart(df["severity"].value_counts())

# ---------------- ADD PATIENT ----------------
elif page == "Add Patient":
    st.title("📝 Add Patient")

    symptoms = st.text_input("Enter Symptoms")

    if st.button("🚀 Process Patient"):
        response = requests.post(
            "http://127.0.0.1:8000/process",
            json={"symptoms": symptoms}
        )

        if response.status_code == 200:
            data = response.json()

            st.success("Patient Added!")

            st.metric("Severity", data.get("severity"))
            st.metric("Queue Position", data.get("queue_position"))

# ---------------- QUEUE VIEW ----------------
elif page == "Queue View":
    st.title("📋 Patient Queue")

    response = requests.get("http://127.0.0.1:8000/patients")

    if response.status_code == 200:
        patients = response.json()

        if len(patients) == 0:
            st.info("Queue is empty")
        else:
            for p in patients:
                color = severity_color(p["severity"])

                st.markdown(
                    f"""
                    <div style="
                        padding:15px;
                        margin-bottom:10px;
                        border-radius:10px;
                        background-color:#ffffff;
                        box-shadow:0px 2px 8px rgba(0,0,0,0.1);
                        border-left:8px solid {color};
                    ">
                        <b>🧑 Symptoms:</b> {p['symptoms']} <br>
                        <b>⚠ Severity:</b> {p['severity']} <br>
                        <b>📍 Queue Position:</b> {p['queue_position']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )