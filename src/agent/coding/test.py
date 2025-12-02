import flask
import requests
import json
import argparse
import asyncio
import json
import sys
import os
import time
import re
import shlex
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
# from tools import edit_file, edit_jsonfile



#payload = {
#    "command": "git clone git@gitee.com:openhitls/openhitls.git",
#    "workdir": "/app",
#    "timeout": 80,
#}
#result = requests.post(url, json=payload)
#print(result)

GIT_TOKEN = "26aedeb993d52912961e33e800247e15"
GIT_NAME = "yo11232"
GIT_EMAIL = "3244826942@qq.com"
SANDBOX_URL = "http://localhost:9999"
NEW_REPO_NAME = "tset"
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

# def set_up(
# #    thread_id: Optional[str] = Field(
# #        None, 
# #       description="Injected thread_id from LangGraph, used for conversation-specific branches."),
# ):
#     """
#     Set up for the openhitls and the git environment.
#     Create the branch for this thread
       
#     """
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
#     return f'Set up succeed in dir:"/app/openhitls"\n'
# def set_up():
#     NEW_REPO_NAME = f"tset"
#     url = "https://gitee.com/api/v5/repos/openhitls/openhitls/forks"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"token {GIT_TOKEN}"
#     }
#     data = {
#         "path": NEW_REPO_NAME,
#         "name": NEW_REPO_NAME,
#         "private": True
#     }
#     try:
#         response = requests.post(url, headers=headers, json=data, timeout=30)
#         return_code = response.status_code
#         response = response.json()
#         if return_code == 201:
#             print("[1/2]Fork succeed.\n")
#         else:
#             print(f"Something wrong, {response.get('message',response)}")
#     except requests.exceptions.RequestException as e:
#         print(f"Fork request failed: {e}")
#     time.sleep(5) #Fork给点等待时间，防止clone的时候找不到仓库
#     commands = [
#     {
#         "command": ["git", "config", "--global", "user.name", GIT_NAME],
#         "workdir": "/app",
#         "timeout": 10,
#     },
#     {
#         "command": ["git", "config", "--global", "user.email", GIT_EMAIL],
#         "workdir": "/app",
#         "timeout": 10,
#     },
#     {
#         "command": ["git", "clone", f"git@gitee.com:{GIT_NAME}/{NEW_REPO_NAME}.git"],
#         "workdir": "/app",
#         "timeout": 60,
#     },
#     ]
#     for cmd in commands:
#         payload = {
#             "command": cmd["command"],
#             "workdir": cmd["workdir"],
#             "timeout": cmd["timeout"]
#         }
#         result = SandBox(service="execute_cmd", payload=payload)
#         if result["status"] != "ok":
#             print(result)
#             return result
#     print("[2/2]Sandbox initialized.")


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
    print(value)
    payload = {
        "operation": operation,
        "file_path": file_path,
        "json_path": json_path,
        "value": value,
        "pretty_print": pretty_print,
    }
    result = SandBox(service="edit_json", payload=payload)
    return result

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
        "path": file_path,
        "old_str": old_str,
        "new_str": new_str,
        "insert_line": insert_line,
        "file_text": file_text,
        "view_range": view_range,
    }
    result = SandBox(service="edit_file", payload=payload)
    return result

def set_up():
    NEW_REPO_NAME = "tset"
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
            return f"Something wrong, {response.get('message',response)}"
    except requests.exceptions.RequestException as e:
        return f"Fork request failed: {e}"
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
            print(result)
            return result
    return (f"Remote repository Forked succeed {GIT_NAME}/{NEW_REPO_NAME}\n"
            f"Local repository set and cloned succeed in /app/{NEW_REPO_NAME}")

def push_changes(
    reason: Optional[str] = "Commit generated code"
):
    NEW_REPO_NAME = "tset"
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
        print(result)
        if result["status"] != "ok":
            if cmd["command"][1] == "commit" and "nothing to commit" in (result.get("stdout") or "").lower():
                continue
            print("[!]error")
            return result
    return (f"Changes committed with message '{reason}' and pushed successfully to "
            f"{GIT_NAME}/{NEW_REPO_NAME} in /app/{NEW_REPO_NAME}")
    # payload = {
    #     "command": ["git", "config", "--global", "user.name", GIT_NAME],
    #     "workdir": "/app",
    #     "timeout": 10,
    # }
    # result = SandBox(service="execute_cmd", payload=payload)
    # print(result)
    # payload = {
    #     "command": ["git", "config", "--global", "user.email", GIT_EMAIL],
    #     "workdir": "/app",
    #     "timeout": 10,
    # }
    # result = SandBox(service="execute_cmd", payload=payload)
    # print(result)
    # payload = {
    #     "command": ["git", "clone", f"git@gitee.com:{GIT_NAME}/{NEW_REPO_NAME}.git"],
    #     "workdir": "/app",
    #     "timeout": 60,
    # }
    # result = SandBox(service="execute_cmd", payload=payload)
    # print(result)
    # payload = {
    #     "command": ["rm", "-rf", f"README.md"],
    #     "workdir": f"/app/{NEW_REPO_NAME}",
    #     "timeout": 10,
    # }
    # result = SandBox(service="execute_cmd", payload=payload)
    # print(result)
    # payload = {
    #     "command": ["git", "add", "."],
    #     "workdir": f"/app/{NEW_REPO_NAME}",
    #     "timeout": 10,
    # }
    # result = SandBox(service="execute_cmd", payload=payload)
    # print(result)
    # reason = "test"
    # payload = {
    #     "command": ["git", "commit", "-m", f"{reason}"],
    #     "workdir": f"/app/{NEW_REPO_NAME}",
    #     "timeout": 10,
    # }
    # result = SandBox(service="execute_cmd", payload=payload)
    # print(result)
    # payload = {
    #     "command": f'git push -u origin main',
    #     "workdir": f"/app/{NEW_REPO_NAME}",
    #     "timeout": 10,        
    # }
    # result = SandBox(service="execute_cmd", payload=payload)
    # print(result)
    
    
    
    
    # try:
    #     result = subprocess.run(
    #     [
    #         "curl", "-f", "-X", "POST",
    #         "-H", "Content-Type: application/json",
    #         "-H", f"Authorization: token {GIT_TOKEN}",
    #         "-d", json.dumps({"path":NEW_REPO_NAME,
    #                           "name":NEW_REPO_NAME,
    #                           "private":True}
    #                         ),
    #         f"https://gitee.com/api/v5/repos/openhitls/openhitls/forks"
    #         ],
    #     cwd=".",
    #     capture_output=True,
    #     text=True,
    #     check=True,
    #     timeout=80
    #     )
    # except subprocess.TimeoutExpired as e:
    #     print(f"Timeout after {e.timeout} seconds.")
    #     return f"Fork operation timed out after {e.timeout} seconds."
    # except subprocess.CalledProcessError as e:
    #     return f"Fork operation failed with return code {e.returncode}"
    # if result.returncode != 0:
    #     sys.exit(result.returncode)
    # print(result)
# def push_changes(
#     reason: Optional[str] = Field(
#         "Commit generated code", 
#         description="The reason for the change.Defult as : Commit generated code."
#     ),
    
# ):
#     """
#     Commit changes to remote repo
#     """
#     NEW_REPO_NAME = "chat_1145145"
#     payload = {
#         "command": f'rm -rf README.md',
#         "workdir": f"/app/{NEW_REPO_NAME}",
#         "timeout": 80,        
#     }
#     result = SandBox(service="execute_cmd", payload=payload)
#     print(result)
#     if result.get("status")!= "ok":
#         return result
#     payload = {
#         "command": 'git add .',
#         "workdir": f"/app/{NEW_REPO_NAME}",
#         "timeout": 80,        
#     }
#     result = SandBox(service="execute_cmd", payload=payload)
#     print(result)
#     if result.get("status")!= "ok":
#         return result
#     payload = {
#         "command": f'git commit -m {reason}',
#         "workdir": f"/app/{NEW_REPO_NAME}",
#         "timeout": 80,        
#     }
#     result = SandBox(service="execute_cmd", payload=payload)
#     print(result)
#     if result.get("status")!= "ok":
#         return result
#     payload = {
#         "command": f'git push -u origin main',
#         "workdir": f"/app/{NEW_REPO_NAME}",
#         "timeout": 80,        
#     }
#     result = SandBox(service="execute_cmd", payload=payload)
#     print(result)
#     if result.get("status")!= "ok":
#         return result
#     print(result)
def add_line_numbers(text: str, start_line: int = 1) -> str:
    lines = text.splitlines()
    numbered_lines = [f"{i+start_line:6}\t{line}" for i, line in enumerate(lines)]
    return "\n".join(numbered_lines)
if __name__ == "__main__":
    # print(set_up())
    # print(push_changes("man!"))/app/tsetfeature.json
    print(edit_jsonfile("add",
                        f"/app/{NEW_REPO_NAME}/config/json/feature.json",
                        "$.libs.hitls_crypto.features.c.modes.hctr",
                        "good"
                        )
          )
    # print(
    #     edit_file(
    #         command="str_replace",
    #         file_path= f"/app/{NEW_REPO_NAME}/configure.py",
    #         old_str="# -*- coding: utf-8 -*-",
    #         new_str=""
    #     )
    # )

# payload = {
#     "operation": "add",                  
#     "file_path": "/app/app/feature.json",  
#     "json_path": "$.libs.hitls_crypto.features.c.modes.hctr",     
#     "value": 'null',                   
#     "pretty_print": True                 
# }