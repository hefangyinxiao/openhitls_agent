import aiohttp
import asyncio
from typing import Any, List


async def run_python_interpreter(code_snippets: List[str], ports: List[int] = [5010, 5011, 5012]) -> tuple:
    """
    Executes complete Python file codes in a sandboxed environment and returns the results or error information.
    This tool can run complete Python programs and provide output, including successful execution results or detailed error traces.

    **Usage Example:**
    # Execute multiple complete Python programs
    run_python_interpreter(code_snippets=[
    '''
    from NssMPC.secure_model.mpc_party.semi_honest import SemiHonestCS
    from NssMPC import ArithmeticSecretSharing, RingTensor
    from NssMPC.config.runtime import PartyRuntime
    from NssMPC.config.configs import DEVICE
    import torch

    p0 = SemiHonestCS(type='server')

    p0.set_multiplication_provider()

    p0.online()

    with PartyRuntime(p0):
        x = RingTensor.convert_to_ring(torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=DEVICE))
        X = ArithmeticSecretSharing.share(x, 2)
        shared_x = X[0]
        p0.send(X[1])
        shared_y = p0.receive()
        print(shared_x)
        print(shared_y)
        shared_result = shared_x * shared_y - shared_x + shared_y
        result = shared_result.restore().convert_to_real_field()

    print(result)

    p0.close()
    ''',
    '''
    from NssMPC.secure_model.mpc_party.semi_honest import SemiHonestCS
    from NssMPC import ArithmeticSecretSharing, RingTensor
    from NssMPC.config.runtime import PartyRuntime
    from NssMPC.config.configs import DEVICE
    import torch

    p1 = SemiHonestCS(type='client')

    p1.set_multiplication_provider()

    p1.online()

    with PartyRuntime(p1):
        y = RingTensor.convert_to_ring(torch.tensor([[-1.0, 2.0], [4.0, 3.0]], device=DEVICE))
        Y = ArithmeticSecretSharing.share(y, 2)
        shared_y = Y[0]
        p1.send(Y[1])
        shared_x = p1.receive()
        print(shared_x)
        print(shared_y)
        shared_result = shared_x * shared_y - shared_x + shared_y
        result = shared_result.restore().convert_to_real_field()

    print(result)

    p1.close()
    '''
    ])

    **Output Format:**
    Each Python program execution returns a JSON response with the following structure:
    ```json
    {
        "output": "Standard output content from the program",
        "error": "Error message if execution failed, empty string if successful",
        "stack_trace": "Complete stack trace if error occurred, empty string if successful"
    }
    ```
    Args:
        code_snippets (list): "A list of complete Python file codes to execute. Each element in the list represents
                        a complete Python program/file that will be executed independently.
                        Each code snippet should be a full, self-contained Python program with all necessary
                        imports, class definitions, function definitions, and execution logic.
                        Multi-line code should be properly formatted with newline characters.
        ports (List[int]): List of ports for the interpreter servers, default is [5010, 5011, 5012].
    """
    response = await _sync_post_requests(code_snippets, ports)
    print("[解释器] 代码执行结果:", response)
    return code_snippets, response


# def has_errors(response: list) -> bool:
#     return any(r['error'] is not None for r in response)


# def response_to_str(response: list) -> str:
#     output_lines = ['\n## [解释器] 代码执行报告\n']
#     for idx, item in enumerate(response):
#         stack_trace = item.get('stack_trace')
#         error = item.get('error')
#         output = item.get('output', '')
#         if error:
#             output_lines.append(f"## ❌ Error {idx}\n```diff\n- {error}\n{stack_trace}\n```")
#         if output:
#             output_lines.append(f"## ✅ Output {idx}\n```\n{output}\n```")

#     markdown_content = '\n\n'.join(output_lines)
#     return markdown_content


async def _sync_post_requests(code_snippets: List[str], ports: List[int]) -> List[Any]:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, code in enumerate(code_snippets):
            url = f'http://localhost:{ports[i]}/exec'
            # url = f'http://10.147.20.102:{ports[i]}/exec'
            tasks.append(session.post(url, data=code))

        responses = await asyncio.gather(*tasks)
        return [await r.json() for r in responses]
