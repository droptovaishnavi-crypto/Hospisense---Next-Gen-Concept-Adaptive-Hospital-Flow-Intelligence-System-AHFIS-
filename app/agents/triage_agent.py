import pickle

model = pickle.load(open("app/models/triage_model.pkl", "rb"))
vectorizer = pickle.load(open("app/models/vectorizer.pkl", "rb"))

def triage_patient(state):
    symptoms = state.get("symptoms", "")
    X = vectorizer.transform([symptoms])
    prediction = model.predict(X)
    return prediction[0]