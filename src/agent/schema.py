from pydantic import BaseModel, Field

class FConfigSchema(BaseModel):
    planning_model_name: str = Field(
        default="openai/qwen-max-latest",
        description="model_name is the name of the model to use for the agent.",
        json_schema_extra={
            "langgraph_nodes": ["planning_agent"],
        },
    )
    coding_model_name: str = Field(
        default="openai/qwen-max-latest",
        description="model_name is the name of the model to use for the agent.",
        json_schema_extra={
            "langgraph_nodes": ["coding_agent"],
        },
    )
    repo_name: str =Field(
        default="openHiTLS-agent",
        description="repo_name is the name of the repository to work on.",
        json_schema_extra={
            "langgraph_nodes": ["coding_agent"],
        },
    )
    temperature: int=Field(
        default=1.0,
        description="temperature is the temperature to use for the model.",
        json_schema_extra={
            "langgraph_nodes": ["coding_agent"],
        },
    )
    max_iterations: int=Field(
        default=50,
        description="max_iterations is the maximum number of iterations to run the agent.",
        json_schema_extra={
            "langgraph_nodes": ["coding_agent"],
        },
    )

# class ConfigSchema(BaseModel):
#     model_name: str=Field(
#         default="openai/qwen-max-latest",
#         description="model_name is the name of the model to use for the agent.",
#         json_schema_extra={
#             "langgraph_nodes": ["agent"],
#         },
#     )
#     repo_name: str=Field(
#         default="NssMPClib",
#         description="repo_name is the name of the repository to work on.",
#         json_schema_extra={
#             "langgraph_nodes": ["init","agent"],
#         },
#     )
#     temperature: int=Field(
#         default=1.0,
#         description="temperature is the temperature to use for the model.",
#         json_schema_extra={
#             "langgraph_nodes": ["agent"],
#         },
#     )
#     max_iterations: int=Field(
#         default=20,
#         description="max_iterations is the maximum number of iterations to run the agent.",
#         json_schema_extra={
#             "langgraph_nodes": ["agent"],
#         },
#     )