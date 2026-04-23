# 🏥 HospiSense AI  
### Adaptive Hospital Flow Intelligence System (AHFIS)

An AI-powered multi-agent system designed to intelligently manage hospital patient triage, optimize queue flow, and assist real-time medical decision-making using Machine Learning, NLP, and LangGraph orchestration.

---

# 🚨 Problem Statement

Hospitals often face:
- Overcrowded queues and delayed treatments
- Manual and inconsistent patient triage decisions
- Lack of real-time prioritization for critical patients
- Inefficient resource allocation (beds, doctors, ICU)

👉 This leads to delayed emergency care and reduced operational efficiency.

---

# 🚀 Solution

HospiSense AI introduces an **intelligent hospital flow system** that:
- Automatically prioritizes patients based on severity
- Uses AI agents to simulate hospital decision-making
- Dynamically manages patient flow and resources
- Provides real-time dashboard visibility

---

# 🧠 System Architecture (5-Tier AI Pipeline)

## 🟦 1. Input Layer
- React Web Dashboard
- Flutter Mobile App
- Patient symptom + emergency input interface

---

## ⚙️ 2. Orchestrator Layer
- FastAPI backend
- LangGraph-based workflow engine
- Coordinates all AI agents

---

## 🤖 3. AI Agent Layer (LangGraph Nodes)

- 🩷 **Triage Agent** → Classifies patient severity  
- 🟠 **Prediction Agent** → Predicts risk level  
- 🟣 **Flow Agent** → Optimizes queue priority  
- 🟦 **Resource Agent** → Allocates hospital resources  

---

## 🧠 4. Machine Learning Layer

- scikit-learn → triage classification & flow prediction  
- PyTorch → advanced risk prediction models  
- spaCy NLP → symptom text processing & extraction  

---

## 📦 5. Output Layer

- PostgreSQL → patient records storage  
- Decision Engine → final priority ranking system  
- Live Dashboard → real-time hospital queue visualization  

---

# 🔥 Key Features

- AI-based patient triage system  
- Multi-agent orchestration using LangGraph  
- Real-time hospital queue optimization  
- Intelligent resource allocation system  
- Web + Mobile accessible interface  
- Scalable backend architecture  

---

# 🛠️ Tech Stack

- FastAPI  
- LangGraph  
- scikit-learn  
- PyTorch  
- spaCy  
- PostgreSQL  
- React (Frontend)  
- Flutter (Mobile App)

---

# 🌍 Impact

- Reduces emergency waiting time  
- Improves critical patient prioritization  
- Automates hospital decision workflows  
- Enhances healthcare operational efficiency  

---

# 📊 Project Vision

To build an **AI-driven hospital intelligence system** that ensures:

> “Right patient, right priority, right time.”

---

# 🚀 How to Run

## Backend
```bash
uvicorn app.main:app --reload

Frontend
streamlit run frontend/app.py

👩‍💻 Author

Vaishnavi Devi R
AI / ML Enthusiast | Data Science | Deep Learning

