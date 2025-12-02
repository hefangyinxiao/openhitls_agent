import os
import json
from langchain_core.messages import SystemMessage, RemoveMessage
from langchain_litellm import ChatLiteLLM
from langgraph.constants import END
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableConfig
from agent.coding.prompts import get_system_prompt
from agent.state import State
from agent.coding.tools import search_code, set_up, edit_file, edit_jsonfile

llm = ChatLiteLLM(
    model="openai/qwen3-max",
    api_base='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key=os.getenv("QWEN_API_KEY"),
    temperature=0.2,
    top_p=0.95,
    streaming=True,
    request_timeout=30.0
)

tools = [search_code]

llm_with_tools = llm.bind_tools(tools)


def start_node(state: State) -> State:
    """起始节点：初始化任务状态"""
    tls_state = state["substates"]["tls_state"]
    task_files = tls_state.get("task_files", [])
    if not task_files:
        tls_state["is_finished"] = True
        return {"substates": {"tls_state": tls_state}}
    user_query = tls_state.get("user_query", "")
    task_id = tls_state.get("task_id", 0)
    total_tasks = len(task_files)
    current_task = task_files[task_id]
    task_history = tls_state.get("task_history", [])
    algorithm_category = tls_state.get("algorithm_category", "symmetric")
    tls_state["user_query"] = user_query
    tls_state["task_id"] = task_id
    tls_state["total_tasks"] = total_tasks
    tls_state["current_task"] = current_task
    tls_state["task_history"] = task_history
    tls_state["is_finished"] = False    
    
    setup_result = set_up()
    if setup_result["status"] != "ok":
        tls_state["is_finished"] = True
        error_message = SystemMessage(content=f"沙箱初始化失败:\n{setup_result['message']}")
        return {"messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES), error_message], "substates": {"tls_state": tls_state}}
    prompt = get_system_prompt(user_query, current_task, task_history, setup_result, algorithm_category)
    system_prompt = SystemMessage(content=prompt)
    return {
        "messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES), system_prompt],
        "substates": {"tls_state": tls_state}
    }


def agent_node(state: State) -> State:
    """Agent节点：处理当前任务并可能调用工具"""
    messages = state.get("messages", [])
    # 调用模型
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


def tool_node_wrapper(state: State) -> State:
    """工具节点包装器"""
    tool_node = ToolNode(tools)
    result = tool_node.invoke({"messages": state["messages"]})
    return {"messages": result["messages"]}


def parser(state: State) -> State:
    """
    接收Agent格式化修改的输出
    暴露给Agent的操作有CreateFile、EditContent、AddContent、DeleteContent
    本节点将Agent的操作映射为代码修改工具可以接受的参数,并调用对应工具
    """
    messages = state.get("messages", [])
    last_message = messages[-1]
    task_list = json.loads(last_message.content)
    results = []
    is_done = True 
    for task in task_list:
        action = task.get("action")
        location = task.get("location")
        print(state["substates"]["tls_state"]["current_task"])
        filepath = state["substates"]["tls_state"]["current_task"]["Path"]
        content = task.get("content")
        if action=="CreateFile":
            result = edit_file(command="create", file_path=filepath, file_text=content)
        elif action=="EditContent":
            if filepath.endswith(".json") :
                result = edit_jsonfile(operation="set", file_path=filepath, json_path=location, value=content)
            else:
                result = edit_file(command="str_replace", file_path=filepath, old_str=location, new_str=content)
        elif action=="AddContent":
            if filepath.endswith(".json") :
                result = edit_jsonfile(operation="add", file_path=filepath, json_path=location, value=content)
            else:
                result = edit_file(command="insert", file_path=filepath, insert_line=location, file_text=content)
        elif action=="DeleteContent":
            if filepath.endswith(".json") :
                result = edit_jsonfile(operation="remove", file_path=filepath, json_path=location)
            else:
                result = edit_file(command="str_replace", file_path=filepath, old_str=location, file_text="")
        results.append(result)
        if result.get("error"):
            is_done = False
    return {"messages":[{
        "is_done" : is_done,
        "results" : results
        }]}

def process_and_update_task(state: State) -> State:
    """处理任务结果并更新历史"""
    messages = state.get("messages", [])
    tls_state = state["substates"]["tls_state"]
    user_query = tls_state.get("user_query", "")
    current_task = tls_state["current_task"]
    task_files = tls_state.get("task_files", [])
    task_id = tls_state.get("task_id", 0)
    total_tasks = tls_state.get("total_tasks", 0)
    task_history = tls_state.get("task_history", {})
    algorithm_category = tls_state.get("algorithm_category", "symmetric")

    # 提取最终的代码生成信息
    if messages:
        last_message = messages[-1]
        if hasattr(last_message, 'content'):
            task_output = last_message.content
        else:
            task_output = str(last_message)
    else:
        task_output = f"处理了任务: {current_task}"

    current_task_copy = current_task.copy()
    current_task_copy['output'] = task_output
    task_history_copy = task_history.copy()
    task_history_copy.append(current_task_copy)

    if task_id < total_tasks - 1:
        task_id_copy = task_id + 1
        next_task = task_files[task_id_copy]
        prompt = get_system_prompt(user_query, next_task, task_history_copy, "", algorithm_category)
        system_prompt = SystemMessage(content=prompt)
        tls_state["current_task"] = next_task
        tls_state["task_id"] = task_id_copy
        tls_state["task_history"] = task_history_copy
        return {
            "messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES), system_prompt],
            "substates": {"tls_state": tls_state}
        }
    else:
        prompt = get_system_prompt(user_query, {}, task_history_copy, "", algorithm_category)
        system_prompt = SystemMessage(content=prompt)
        tls_state["current_task"] = {}
        tls_state["task_history"] = task_history_copy
        tls_state["is_finished"] = True
        return {
            "messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES), system_prompt],
            "substates": {"tls_state": tls_state}
        }

def should_update(state:State)->str:
    messages = state.get("messages", [])
    if messages and hasattr(messages[-1], 'is_done') and messages[-1].is_done==1:
        return "update_task"
    return "agent"

def should_call_tools(state: State) -> str:
    """决定是否继续循环"""
    messages = state.get("messages", [])

    # 如果有工具调用，继续到工具节点
    if messages and hasattr(messages[-1], 'tool_calls') and messages[-1].tool_calls:
        return "tools"
    return "parser"
    # return "update_task"


def should_finish(state: State) -> str:
    """最终检查是否继续"""
    if state["substates"]["tls_state"].get("is_finished", False):
        return END
    return "agent"
