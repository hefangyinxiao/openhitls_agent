import json

from agent.coding.prompts import TASK_INSTRUCTION

# def get_task_instruction(instance: dict, task: str = 'auto_search', include_pr=False, include_hint=False):
#     """Identical implementation to original"""
#     output_format = None
#     instruction = ""
#
#     task_description = TASK_INSTRUCTION
#
#     instruction += task_description
#
#     if include_pr:
#         problem_statement = instance['problem_statement']
#         instruction += problem_statement.strip()
#
#     if output_format:
#         instruction += output_format
#
#     if include_hint:
#         instruction += (
#             'IMPORTANT: You should ONLY interact with the environment provided to you AND NEVER ASK FOR HUMAN HELP.\n'
#             'Don\'t include any lambda functions!\n'
#             'You should NOT modify any files!\n'
#         )
#
#     return instruction


def convert_to_json(obj):
    if isinstance(obj, list):
        res_obj = []
        for o in obj:
            try:
                json_o = json.loads(o.model_dump_json())
            except:
                json_o = o
            res_obj.append(json_o)
        return res_obj
    else:
        try:
            return json.loads(obj.model_dump_json())
        except:
            print(f'{type(obj)} cannot be converted to json directly.')
            return None

