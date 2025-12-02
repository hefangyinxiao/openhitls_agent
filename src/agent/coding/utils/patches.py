import json
from typing import Literal, Union, Dict, Any, Optional, Mapping, Type

from langchain_core.messages import ToolCall, ToolMessage, BaseMessage, HumanMessage, AIMessage, SystemMessage, \
    FunctionMessage, ChatMessage, BaseMessageChunk, ToolCallChunk, HumanMessageChunk, AIMessageChunk, \
    SystemMessageChunk, FunctionMessageChunk, ChatMessageChunk
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import ToolNode
from litellm.types.utils import Delta
from sqlalchemy import false


class AdaptedToolNode(ToolNode):
    def _run_one(self,
        call: ToolCall,
        input_type: Literal["list", "dict", "tool_calls"],
        config: RunnableConfig
    ) -> ToolMessage:
        processed_call = self.preprocess_args(call)
        return super()._run_one(processed_call, input_type, config)

    async def _arun_one(
        self,
        call: ToolCall,
        input_type: Literal["list", "dict", "tool_calls"],
        config: RunnableConfig,
    ) -> ToolMessage:
        processed_call = self.preprocess_args(call)
        return await super()._arun_one(processed_call, input_type, config)

    def preprocess_args(self, call):
        if isinstance(call["args"], str):
            try:
                call.args = json.loads(call.args, strict_mode=false)
            except Exception as e:
                print(e)
        return call


def fix_json(input_data: Union[str, Dict[str, Any]]) -> Optional[Union[Dict[str, Any], str]]:
    """
    Fix common JSON formatting issues in either a string or dictionary input.

    Args:
        input_data: Either a JSON string or a dictionary that needs formatting fixes

    Returns:
        The fixed dictionary (if input was dict) or string (if input was string),
        or None if fixes couldn't be applied
    """
    if not isinstance(input_data, (str, dict)):
        return None

    # Convert dict to string for processing if needed
    fixed_str= json.dumps(input_data) if isinstance(input_data, dict) else input_data

    fixes = [
        lambda s: s.replace("'", '"')
    ]

    for fix in fixes:
        try:
            fixed_str = fix(fixed_str)
        except (json.JSONDecodeError, Exception):
            continue
    return fixed_str if isinstance(input_data, str) else json.loads(fixed_str)


def _convert_dict_to_message(_dict: Mapping[str, Any]) -> BaseMessage:
    role = _dict["role"]
    if role == "user":
        return HumanMessage(content=_dict["content"])
    elif role == "assistant":
        # Fix for azure
        # Also OpenAI returns None for tool invocations
        content = _dict.get("content", "") or ""

        additional_kwargs = {}
        if _dict.get("function_call"):
            additional_kwargs["function_call"] = dict(_dict["function_call"])

        if _dict.get("tool_calls"):
            for tc in _dict["tool_calls"]:
                tc.model_extra['function']["arguments"]=fix_json(tc.model_extra['function']["arguments"])
            additional_kwargs["tool_calls"] = _dict["tool_calls"]

        return AIMessage(content=content, additional_kwargs=additional_kwargs)
    elif role == "system":
        return SystemMessage(content=_dict["content"])
    elif role == "function":
        return FunctionMessage(content=_dict["content"], name=_dict["name"])
    elif role == "tool":
        return ToolMessage(content=_dict["content"], tool_call_id=_dict["tool_call_id"])
    else:
        return ChatMessage(content=_dict["content"], role=role)


def _convert_delta_to_message_chunk(
        delta: Union[Delta, Dict[str, Any]], default_class: Type[BaseMessageChunk]
) -> BaseMessageChunk:
    # Handle both Delta objects and dicts
    if isinstance(delta, dict):
        role = delta.get("role")
        content = delta.get("content") or ""
        function_call = delta.get("function_call")
        raw_tool_calls = delta.get("tool_calls")
        reasoning_content = delta.get("reasoning_content")
    else:
        role = delta.role
        content = delta.content or ""
        function_call = delta.function_call
        raw_tool_calls = delta.tool_calls
        reasoning_content = getattr(delta, "reasoning_content", None)

    if function_call:
        additional_kwargs = {"function_call": dict(function_call)}
    elif reasoning_content:
        additional_kwargs = {"reasoning_content": reasoning_content}
    else:
        additional_kwargs = {}

    tool_call_chunks = []
    if raw_tool_calls:
        additional_kwargs["tool_calls"] = raw_tool_calls
        try:
            tool_call_chunks = [
                ToolCallChunk(
                    name=rtc["function"]["name"] if isinstance(rtc, dict) else rtc.function.name,
                    args=fix_json(rtc["function"]["arguments"]) if isinstance(rtc, dict) else fix_json(rtc.function.arguments),
                    id=rtc["id"] if isinstance(rtc, dict) else rtc.id,
                    index=rtc["index"] if isinstance(rtc, dict) else rtc.index,
                )
                for rtc in raw_tool_calls
            ]
        except KeyError:
            pass

    if role == "user" or default_class == HumanMessageChunk:
        return HumanMessageChunk(content=content)
    elif role == "assistant" or default_class == AIMessageChunk:
        return AIMessageChunk(
            content=content,
            additional_kwargs=additional_kwargs,
            tool_call_chunks=tool_call_chunks,
        )
    elif role == "system" or default_class == SystemMessageChunk:
        return SystemMessageChunk(content=content)
    elif role == "function" or default_class == FunctionMessageChunk:
        if isinstance(delta, dict):
            func_args = function_call.get("arguments", "") if function_call else ""
            func_name = function_call.get("name", "") if function_call else ""
        else:
            func_args = delta.function_call.arguments if function_call else ""
            func_name = delta.function_call.name if function_call else ""
        return FunctionMessageChunk(
            content=func_args, name=func_name
        )
    elif role or default_class == ChatMessageChunk:
        return ChatMessageChunk(content=content, role=role)  # type: ignore[arg-type]
    else:
        return default_class(content=content)  # type: ignore[call-arg]

import langchain_litellm.chat_models.litellm as litellm_module
litellm_module._convert_dict_to_message = _convert_dict_to_message
litellm_module._convert_delta_to_message_chunk = _convert_delta_to_message_chunk
