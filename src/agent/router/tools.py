from typing import Literal

from langchain.tools import tool
from langgraph.types import Command


@tool
def route(goto:str) -> Command[Literal["planning_agent","coding_agent"]]:
    """根据用户输入路由到专家Agent["planning_agent"]"""
    return Command(
        goto=goto,
        graph=Command.PARENT,
    )