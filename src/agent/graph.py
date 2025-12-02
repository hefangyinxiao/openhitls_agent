from typing import Literal

from langgraph.types import Command

from agent.coding.graph import coding_agent
from agent.planning.graph import planning_agent
from langgraph.graph import StateGraph

from agent.router.graph import agent_router
from agent.state import State


def get_coding_agent(state) -> Command[Literal["coding_agent"]]:
    #If you want to set recursion limit, do it here 
    coding_agent_with_config = coding_agent.with_config(recursion_limit=150)
    return coding_agent_with_config.invoke(state)

def get_planning_agent(state) -> Command[Literal["planning_agent","coding_agent"]]:
    return planning_agent.invoke(state)

def get_router(state) -> Command[Literal["planning_agent","coding_agent"]]:
    return agent_router.invoke(state)

builder = StateGraph(State)
builder.add_node("router",get_router)
builder.add_node("planning_agent", get_planning_agent)
builder.add_node("coding_agent", get_coding_agent)
builder.set_entry_point("router")

graph = builder.compile()
