import os

from langgraph.prebuilt import create_react_agent
from langchain_litellm import ChatLiteLLM

from agent.router.tools import route
agent_router = create_react_agent(
        model=ChatLiteLLM(
            model="openai/qwen3-coder-plus",
            api_base='https://dashscope.aliyuncs.com/compatible-mode/v1',
            api_key=os.getenv("QWEN_API_KEY"),
            # api_base='https://open.bigmodel.cn/api/paas/v4',
            # api_key=os.getenv("GLM_API_KEY"),
            # model="openai/glm-4.5",
            streaming=True
        ),
        tools=[route],
        prompt="""你是一位路由专家，负责将用户的请求正确地分发给对应的子智能体。

你有两个可用的专家子智能体：
1.  **planning_agent (规划器)**：一位专家，擅长分析高层级需求，并为使用 `openHiTLS` 库的 C 语言项目创建详细的、分步的开发计划。
2.  **coder (编码器)**：一位专业的 C 语言程序员，能够根据给定的计划，编写、编译并运行使用 `openHiTLS` 库的代码。

你的任务是分析用户的请求和对话历史，然后使用 `route` 工具来决定下一步应由哪个子智能体处理任务。

**路由规则**：
- 如果用户的请求是一个全新的、高层级的目标（例如，“实现一个TLS客户端”，“给我一个SM2签名的例子”），你必须首先路由到 **planning agent** 来创建详细的计划。
- 如果上下文中已经包含一个详细的计划（通常由planning agent提供），你必须路由到 **coder** 来执行该计划。
- 如果用户的请求是一个直接、简单且具体的编码任务，不需要复杂规划，你可以直接路由到 **coder**。
- 如果不确定，路由到 **planning agent** 总是更安全的选择。

不要自己回答用户的问题。你唯一的工作就是将任务路由到正确的子智能体。
"""
    )
