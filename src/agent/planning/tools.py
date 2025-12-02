import os
from typing import Annotated, Literal, Dict, Any, List

import litellm
from langchain.tools import tool
from langchain_core.messages import RemoveMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_litellm import ChatLiteLLM

from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langgraph.prebuilt import InjectedState
from langgraph.types import Command

# from agent.coding.utils.utils import get_task_instruction
from agent.planning.knowledge_graph.query import get_dependency_execution_order, init_practical_database
from agent.planning.RAG.retrieval import search_with_rerank

from agent.state import TaskAgentState

@tool
def recall(algorithm_name: str, category: Literal["symmetric", "asymmetric", "hash"], mode_name: str = None):
    """
    检索图数据库获取代码实现蓝图，把国标的加密文档的相关需求也给coding_agent。
    Args:
        algorithm_name: 要实现的算法；
        category (Literal["symmetric", "asymmetric", "hash"]): 算法的主要密码学类别，对应后文的动态加载的提示词；
        mode_name: 要实现的模式。
    Returns:
        代码实现蓝图，列表，完善给coding的message。
    """

    init_practical_database()
    messages = [{"role": "user", "content": f'算法名称：{algorithm_name}，算法类别：{category}，模式名称：{mode_name}' }]
    
    query = messages[0]["content"]
    
    retrieved_docs = search_with_rerank(query, top_k=10, rerank_top_k=1) #打算取一个文档

    doc_needed = ""

    if retrieved_docs:
        first_doc = retrieved_docs[0]

        file_path = first_doc.metadata.get('source')

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    doc_needed = f.read()
                    llm = ChatLiteLLM(
                        model="openai/qwen3-max",  # 模型名称
                        api_key=os.environ["QWEN_API_KEY"],  # API密钥
                        api_base='https://dashscope.aliyuncs.com/compatible-mode/v1'
                    )
                    message = HumanMessage(content=doc_needed+f'\n请总结这段文档，提取出与算法名称：{algorithm_name}，算法类别：{category}，模式名称：{mode_name}相关的部分作为代码实现指引')
                    summary_response = llm.invoke([message])
                    doc_needed = summary_response.content
                    print(f"已检索到文档，路径为: {file_path}")
            except FileNotFoundError:
                doc_needed = f"错误：在路径 {file_path} 未找到文件。"
            except Exception as e:
                doc_needed = f"读取文件时出错: {e}"
                
    full_user_content = (
    f'算法名称：{algorithm_name}，算法类别：{category}，模式名称：{mode_name}'
    f"\n\n请参考以下标准文档以实现用户需求：\n\n{doc_needed}"
    )

    updated_messages = [
        HumanMessage(content=full_user_content)
    ]

    execution_plan = get_dependency_execution_order(algorithm_name, mode_name)

    tls_state = TaskAgentState(
        user_query=full_user_content,
        algorithm_category=category,  # 传入 'category'
        task_files=execution_plan,    # 传入文件列表
        
        task_id=0,                    
        total_tasks=len(execution_plan), 
        current_task={},              
        task_history=[],
        is_finished=False
    )

    return Command(
        goto="coding_agent",
        update={
            "messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES), *updated_messages],
            "substates": {
                "tls_state": tls_state
            }
        },
        graph=Command.PARENT,
    )


# @tool
# def transfer_to_coding_agent(state: Annotated[dict, InjectedState], config: RunnableConfig) -> Command[
#     Literal["coding_agent"]]:
#     """Transfer to coding_agent."""
#     repo_name = "openHiTLS"
#     custom_instance = {
#         'instance_id': repo_name,
#         'problem_statement': state["messages"][-1].content,
#     }

#     messages = [
#         {
#             "role": "user",
#             "content": get_task_instruction(custom_instance, include_pr=True, include_hint=True),
#         }
#     ]

#     return Command(
#         goto="coding_agent",
#         update={"messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES), *messages]},
#         graph=Command.PARENT,
#     )
