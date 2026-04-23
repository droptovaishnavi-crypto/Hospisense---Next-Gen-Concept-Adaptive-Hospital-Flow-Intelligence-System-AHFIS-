from langgraph.graph import StateGraph
from app.workflows.state import PatientState

from app.agents.triage_agent import triage_patient
from app.agents.prediction_agent import predict_load
from app.agents.flow_agent import optimize_queue


def build_workflow():

    graph = StateGraph(PatientState)

    # Nodes
    def triage_node(state):
        state["severity"] = triage_patient(state)
        return state

    def prediction_node(state):
        state["load"] = predict_load(state)
        return state

    def flow_node(state):
        state["queue_position"] = optimize_queue(state)
        return state

    # Add nodes
    graph.add_node("triage", triage_node)
    graph.add_node("predict", prediction_node)
    graph.add_node("flow", flow_node)

    # Flow
    graph.set_entry_point("triage")
    graph.add_edge("triage", "predict")
    graph.add_edge("predict", "flow")

    return graph.compile()