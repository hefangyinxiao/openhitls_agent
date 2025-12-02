from agent.coding.graph import coding_agent
from agent.planning.graph import planning_agent
from langgraph.graph import StateGraph

from agent.router.graph import agent_router
from agent.state import State

builder = StateGraph(State)
builder.add_node("router", agent_router)
builder.add_node("planning_agent", planning_agent)
builder.add_node("coding_agent", coding_agent)
builder.set_entry_point("router")

graph = builder.compile()
