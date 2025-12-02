from typing import TypedDict, Annotated, Dict, List, Any

from langgraph.graph import add_messages, StateGraph
from langchain_core.messages import AnyMessage

class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    substates: Dict[str, StateGraph]


class TaskAgentState(TypedDict):
    user_query: str  # 用户的提问
    algorithm_category: str # 算法类别
    current_task: Dict[str, str]  # 当前要修改的文件
    task_files: List[Dict[str, Any]]  # 任务文件列表，由 planning agent 提供
    task_id: int
    total_tasks: int
    task_history: List[Dict[str, Any]]  # 已处理的任务列表
    is_finished: bool
    