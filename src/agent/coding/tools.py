import os
import requests
import aiohttp
import asyncio
import re
import json
import time
from typing import Optional, Dict
from dotenv import load_dotenv
from langchain_core.tools import tool
from agent.coding.prompts import OPENHITLS_RULE
from pydantic import BaseModel, Field
from typing import List, Optional

# --- 1. 配置模块 ---
load_dotenv()

# Sourcegraph 配置
SOURCEGRAPH_URL = os.getenv("SOURCEGRAPH_URL") 
SOURCEGRAPH_ACCESS_TOKEN = os.getenv("SOURCEGRAPH_ACCESS_TOKEN")


# # 沙箱环境配置
SANDBOX_URL = os.getenv("SANDBOX_URL")
GIT_TOKEN = os.getenv("GIT_TOKEN")
GIT_NAME = os.getenv("GIT_NAME")
GIT_EMAIL = os.getenv("GIT_EMAIL")
NEW_REPO_NAME = os.getenv("NEW_REPO_NAME")

def add_line_numbers(text: str, start_line: int = 1) -> str:
    lines = text.splitlines()
    numbered_lines = [f"{i+start_line:6}\t{line}" for i, line in enumerate(lines)]
    return "\n".join(numbered_lines)


@tool
def search_code(query: str) -> str:
    """
    在 Sourcegraph 中搜索代码。此工具对于查找函数定义、用法示例或特定代码模式非常有用。
    它会返回完整的文件内容以便于大型语言模型（LLM）理解上下文。
    查询参数 'query' 应该是一个有效的 Sourcegraph 查询字符串。
    例如: 'repo:openHiTLS/openHiTLS file:client.c HITLS_Connect'
    另一个例子: 'repo:openHiTLS/openHiTLS type:symbol kind:function CRYPT_EAL_Init'
    """
    if not SOURCEGRAPH_URL or not SOURCEGRAPH_ACCESS_TOKEN:
        return "错误: 环境变量 SOURCEGRAPH_URL 或 SOURCEGRAPH_ACCESS_TOKEN 未设置。"

    graphql_query = """
    query CodeSearch($query: String!) {
      search(query: $query, version: V3, patternType: literal) {
        results {
          results {
            __typename
            ... on FileMatch {
              repository { name }
              file { 
                path
                content
              }
            }
          }
          alert {
            title
            description
          }
        }
      }
    }
    """
    
    headers = {'Authorization': f'token {SOURCEGRAPH_ACCESS_TOKEN}'}
    
    try:
        response = requests.post(
            SOURCEGRAPH_URL,
            headers=headers,
            json={'query': graphql_query, 'variables': {'query': query}}
        )
        response.raise_for_status()
        data = response.json()

        if "errors" in data:
            return f"Error from Sourcegraph API: {data['errors']}"
            
        search_results = data.get("data", {}).get("search", {}).get("results", {}).get("results", [])
        if not search_results:
            alert = data.get("data", {}).get("search", {}).get("results", {}).get("alert")
            if alert:
                return f"Search returned an alert: {alert['title']}. Description: {alert['description']}"
            return "No code results found."

        formatted_results = []
        for res in search_results:
            if res.get('__typename') == 'FileMatch':
                repo_name = res.get('repository', {}).get('name', 'N/A')
                file_path = res.get('file', {}).get('path', 'N/A')
                content = res.get('file', {}).get('content', '')
                content = add_line_numbers(content, 1)
                formatted_results.append(
                    f"### Repository: {repo_name}\n"
                    f"#### File: {file_path}\n"
                    f"```c\n{content}\n```"
                )
        
        return "\n\n---\n\n".join(formatted_results)

    except requests.RequestException as e:
        return f"Network or HTTP error when calling Sourcegraph API: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

class FileChange(BaseModel):
    """A model to represent a planned change to a single file."""
    file_path: str = Field(..., description="The full path to the file that needs to be created or modified.")
    description_of_changes: str = Field(..., description="A concise, one-sentence summary of the required changes in this file.")

class SourceFile(BaseModel):
    """A model to represent a source file with its full content."""
    file_path: str = Field(..., description="The full path to the file being written.")
    code_content: str = Field(..., description="The complete and final source code for the specified file.")

@tool
def propose_integration_framework(framework: List[FileChange]) -> str:
    """
    Call this tool after the initial research to propose a high-level plan of all file modifications.
    This is your blueprint for the implementation.
    """
    print("\n--- TOOL: Proposing Integration Framework ---")
    print("The agent has proposed the following blueprint for integration:")
    for change in framework:
        print(f"- Path: {change.file_path}")
        print(f"  Change: {change.description_of_changes}")
    return "Framework proposed successfully. You may now proceed with implementing the files one by one using the write_code tool."

# @tool
# def write_code(file: SourceFile) -> str:
#     """
#     Call this tool to write the complete code for a single file as planned in the framework.
#     This should be called for each file in your proposed framework.
#     """
#     print(f"\n--- TOOL: Writing Code for file: {file.file_path} ---")
#     print("```c")
#     print(file.code_content)
#     print("```")
#     return f"Code for {file.file_path} has been written successfully."

# @tool
# async def write_file(path: str, content: str) -> str:
#     """
#     将内容写入到指定的文件路径。如果文件或目录不存在，会自动创建。
#     注意: 此工具应在受限的沙箱环境中使用，以防止写入任意系统路径。
#     """
#     try:
#         dir_path = os.path.dirname(path)
#         if dir_path:
#             os.makedirs(dir_path, exist_ok=True)
#         with open(path, 'w', encoding='utf-8') as f:
#             f.write(content)
#         return f"成功将内容写入到文件: {path}"
#     except Exception as e:
#         return f"写入文件 {path} 时出错: {str(e)}"

# @tool
# async def execute_bash_command(command: str) -> str:
#     """在沙箱环境中执行一个shell命令。可用于编译 (cmake, make) 和运行生成的可执行文件。"""
#     try:
#         timeout = aiohttp.ClientTimeout(total=60)
#         async with aiohttp.ClientSession(timeout=timeout) as session:
#             async with session.post(SANDBOX_URL, json={"command": command}) as response:
#                 if response.status == 200:
#                     result = await response.json()
#                     # [改进] 如果沙箱能返回退出码，判断 result.get('exit_code') == 0 会更可靠。
#                     output = f"命令 '{command}' 执行成功。\n"
#                     output += f"--- STDOUT ---\n{result.get('stdout', '')}\n"
#                     output += f"--- STDERR ---\n{result.get('stderr', '')}"
#                     return output
#                 else:
#                     error_body = await response.text()
#                     return f"执行命令 '{command}' 时出错: HTTP 状态码 {response.status}, 响应: {error_body}"
#     except asyncio.TimeoutError:
#         return f"执行命令 '{command}' 时超时（超过60秒）。"
#     except Exception as e:
#         return f"执行命令 '{command}' 时连接到沙箱环境出错: {str(e)}"

# @tool
# async def compile_and_run_c_project(cmake_content: str, c_code_content: str, main_c_path: str = "main.c") -> str:
#     """一个组合工具，它自动化了整个C项目的创建、编译和运行流程。"""
#     await write_file("CMakeLists.txt", cmake_content)
#     await write_file(main_c_path, c_code_content)
#     cmake_result = await execute_bash_command("cmake .")
#     make_result = await execute_bash_command("make")
    
#     run_result = "编译失败，未执行。"
    
#     if "error:" not in make_result.lower() and "fail" not in make_result.lower() and "failed" not in make_result.lower():
#         # [改进] 动态从 CMakeLists.txt 内容中解析可执行文件名，而不是硬编码。
#         executable_name = "main_app"  # 默认值
#         match = re.search(r"project\s*\(\s*(\S+)\s*\)", cmake_content, re.IGNORECASE)
#         if match:
#             executable_name = match.group(1)
        
#         run_result = await execute_bash_command(f"./{executable_name}")
    
#     final_output = (
#         f"--- CMake 结果 ---\n{cmake_result}\n\n"
#         f"--- Make (编译) 结果 ---\n{make_result}\n\n"
#         f"--- 运行结果 ---\n{run_result}\n\n"
#         "--- 专家提示 ---\n"
#         f"{OPENHITLS_RULE}"
#     )
#     return final_output


def SandBox(service: str, payload: dict):
    """
    Post requests to remote sandbox。
    """
    url = f"{SANDBOX_URL}/{service}"
    try:
        response = requests.post(url, json=payload, timeout=60)
        # response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return {
                "status": "error",
                "error": f"[SandBox Error] Invalid JSON response from {url}",
                "output": response.text
            }
        return response.json() 
    except requests.exceptions.RequestException as e:
        return {"status":"error",
                "error": f"[SandBox Error] Failed to connect to {url}: {str(e)}"
                }
    except json.JSONDecodeError:
        return {"status": "error",
                "error": f"[SandBox Error] Invalid JSON response from service {service}"
                }



json_operationlists = ["view", "set", "add", "remove"]

def edit_jsonfile(
    operation: str,
    file_path: str,
    json_path: Optional[str] = None,
    value: Optional[object] = None,
    pretty_print: bool = True
):
    """
    Call this tool to edit the JSON files.
    """
    if value is not None:
        value = json.dumps(value, ensure_ascii=False)
    else:
        value = None
    payload = {
        "operation": operation,
        "file_path": f"/app/{NEW_REPO_NAME}/{file_path}",
        "json_path": json_path,
        "value": value,
        "pretty_print": pretty_print,
    }
    result = SandBox(service="edit_json", payload=payload)
    return result



text_operationlists = ["view", "create", "str_replace", "insert"]

def edit_file(
    command: str,
    file_path: str,
    old_str: Optional[str] = None,
    new_str: Optional[str] = None,
    insert_line: Optional[int] = None,
    file_text: Optional[str] = None,
    view_range: Optional[List[int]] = None
):
    """
    Call this tool to perform general text file operations.
    Supported commands: view, create, str_replace, insert.
    """
    payload = {
        "command": command,
        "path": f"/app/{NEW_REPO_NAME}/{file_path}",
        "old_str": old_str,
        "new_str": new_str,
        "insert_line": insert_line,
        "file_text": file_text,
        "view_range": view_range,
    }
    result = SandBox(service="edit_file", payload=payload)
    return result


def set_up():
    """
    Set up the local and remote openHiTLS repository.
    """
    url = "https://gitee.com/api/v5/repos/openhitls/openhitls/forks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"token {GIT_TOKEN}"
    }
    data = {
        "path": NEW_REPO_NAME,
        "name": NEW_REPO_NAME,
        "private": True
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        return_code = response.status_code
        response = response.json()
        if return_code != 201:
            return {
            "status": "fail",
            "message":f"Something wrong, {response.get('message',response)}"
            }
    except requests.exceptions.RequestException as e:
        return {
            "status": "fail",
            "message":f"Fork request failed: {e}"
            }
    time.sleep(5) #Fork后给点等待时间，防止clone的时候找不到仓库
    commands = [
    {
        "command": ["git", "config", "--global", "user.name", GIT_NAME],
        "workdir": "/app",
        "timeout": 10,
    },
    {
        "command": ["git", "config", "--global", "user.email", GIT_EMAIL],
        "workdir": "/app",
        "timeout": 10,
    },
    {
        "command": ["git", "clone", f"git@gitee.com:{GIT_NAME}/{NEW_REPO_NAME}.git"],
        "workdir": "/app",
        "timeout": 60,
    },
    ]
    for cmd in commands:
        payload = {
            "command": cmd["command"],
            "workdir": cmd["workdir"],
            "timeout": cmd["timeout"]
        }
        result = SandBox(service="execute_cmd", payload=payload)
        if result["status"] != "ok":
            return result
    return {
            "status": "ok",
            "message":(f"Remote repository Forked succeed {GIT_NAME}/{NEW_REPO_NAME}\n"
            f"Local repository set and cloned succeed in /app/{NEW_REPO_NAME}")
            }

# @tool
# def set_up(
# #    thread_id: Optional[str] = Field(
# #        None,
# #        description="Injected thread_id from LangGraph, used for conversation-specific branches."
# #    ),
# ):
#     """
#     Set up for the openhitls and the git environment.
       
#     """
# #NEW_REPO_NAME = f"chat_{thread_id}"
#     NEW_REPO_NAME = f"openhitls"
#     payload = {
#         "command": [
#             "curl", "-X", "POST",
#             "-H", "Content-Type: application/json",
#             "-H", f"Authorization: token {GIT_TOKEN}",
#             "-d", json.dumps({"path":NEW_REPO_NAME, "name":NEW_REPO_NAME,"private":True}),
#             f"https://gitee.com/api/v5/repos/openhitls/openhitls/forks"
#             ],
#         "workdir": "/app",
#         "timeout": 80,
#     }
#     result = SandBox(service="execute_cmd", payload=payload)
#     if result.get("status")!= "ok":
#         return result
#     payload = {
#         "command": f"git clone git@gitee.com:{GIT_NAME}/{NEW_REPO_NAME}.git",
#         "workdir": "/app",
#         "timeout": 80,
#     }
#     result = SandBox(service="execute_cmd", payload=payload)
#     if result.get("status")!= "ok":
#         return result
#     return f'Set up succeed in dir:"/app/{NEW_REPO_NAME}"\n'

# @tool
# def execute_cmd_tool(
#     command: str = Field(
#         ...,
#         description="The command to execute inside the sandbox. Can be a string (e.g., 'ls -l') or a JSON array of strings."
#     ),
#     workdir: Optional[str] = Field(
#         None,
#         description="Optional working directory inside the container."
#     ),
#     timeout: Optional[int] = Field(
#         40,
#         description="Optional timeout in seconds. Defaults to 40."
#     ),
#     env: Optional[Dict[str, str]] = Field(
#         None,
#         description="Optional environment variables to set inside the container."
#     )
# ):
#     """
#     Calls the sandbox service to execute a command inside the container.
#     """
#     payload = {
#         "command": command,
#         "workdir": workdir,
#         "timeout": timeout,
#         "env": env
#     }
#     result = SandBox(service="execute_cmd", payload=payload)
#     return result



@tool
def push_changes(
    reason: Optional[str] = "Commit generated code."
):
    """
    Commit and push changes to the remote repository.

    Parameters:
    - reason: Commit message, default is "Commit generated code"
    """
    commands = [
    {
        "command": ["git", "add", "."],
        "workdir": f"/app/{NEW_REPO_NAME}",
        "timeout": 10,
    },
    {
        "command": ["git", "commit", "-m", reason],
        "workdir": f"/app/{NEW_REPO_NAME}",
        "timeout": 10,
    },
    {
        "command": ["git", "push", "-u", "origin", "main"],
        "workdir": f"/app/{NEW_REPO_NAME}",
        "timeout": 10,
    },
    ]
    for cmd in commands:
        payload = {
            "command": cmd["command"],
            "workdir": cmd["workdir"],
            "timeout": cmd["timeout"]
        }
        result = SandBox(service="execute_cmd", payload=payload)
        if result["status"] != "ok":
            if cmd["command"][1] == "commit" and "nothing to commit" in (result.get("stdout") or "").lower():
                continue
            return result
    return (f"Changes committed with message '{reason}' and pushed successfully to "
            f"{GIT_NAME}/{NEW_REPO_NAME} in /app/{NEW_REPO_NAME}")

@tool
def finish(reason: str) -> str:
    """当任务成功完成时，调用此工具来结束流程。"""
    return f"任务成功完成: {reason}"