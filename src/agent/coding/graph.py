from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from agent.coding.nodes import agent_node, tool_node_wrapper, process_and_update_task, should_call_tools, should_finish, \
    start_node,parser,should_update
from agent.state import State, TaskAgentState


# 构建图
def build_graph():
    graph = StateGraph(State)

    # 添加节点
    graph.add_node("start", start_node)
    graph.add_node("agent", agent_node)
    graph.add_node("tools", tool_node_wrapper)
    graph.add_node("update_task", process_and_update_task)
    graph.add_node("parser", parser)
    # 添加边
    graph.add_edge(START, "start")
    graph.add_conditional_edges("start", should_finish, {
        "agent": "agent",
        END: END
    })
    # graph.add_conditional_edges("agent", should_call_tools, {
    #     "tools": "tools",
    #     "update_task": "update_task"
    # })
    graph.add_conditional_edges("agent", should_call_tools, {
        "tools": "tools",
        "parser": "parser"
    })
    graph.add_conditional_edges("parser", should_update,{
        "agent":"agent",
        "update_task":"update_task"
    })
    graph.add_edge("tools", "agent")
    graph.add_conditional_edges("update_task", should_finish, {
        "agent": "agent",
        END: END
    })

    # 启用checkpointer
    checkpointer = InMemorySaver()
    return graph.compile(checkpointer=checkpointer)


coding_agent = build_graph()

if __name__ == '__main__':
    # 执行
    config = {"configurable": {"thread_id": "task_agent_1"}}
    task_files_simple = [
        {'path': 'crypto/eal/src/eal_cipher_method.c', 'action': '在EAL密码方法表中注册SM4-HCTR算法',
         'description': '实现了加密算法的注册和方法表。', 'order': 1},
        {'path': 'config/macro_config/hitls_config_layer_crypto.h',
         'action': '定义SM4-HCTR相关的功能控制宏',
         'description': '定义了与加密相关的宏，用于控制功能的启用和禁用。', 'order': 2},
        {'path': 'config/json/feature.json', 'action': '配置SM4-HCTR算法特性开关和编译选项',
         'description': '特性配置文件 - 定义所有算法特性、依赖关系和编译选项。所有新增特性需要在此注册。',
         'order': 3}, {'path': 'crypto/include/crypt_local_types.h',
                       'action': '定义SM4-HCTR算法相关的本地类型和函数指针',
                       'description': '定义了加密相关的本地类型。是 openHiTLS 项目中定义本地加密类型和方法的核心头文件，它主要定义了加密框架中使用的各种数据结构、函数指针类型和枚举，用于支持对称加密、哈希、MAC、KDF、随机数生成等操作。',
                       'order': 4},
        {'path': 'include/crypto/crypt_algid.h', 'action': '定义SM4-HCTR算法的唯一标识符',
         'description': '定义了所有支持的算法 ID。通过一系列枚举类型定义了框架支持的各种加密算法、模式和参数的唯一标识符。这些 ID 在框架中被广泛使用，用于标识和选择具体的加密算法或模式。',
         'order': 5}, {'path': 'include/bsl/bsl_obj.h', 'action': '定义SM4-HCTR算法相关的对象管理接口',
                       'description': '定义了对象管理的接口。', 'order': 6},
        {'path': 'include/crypto/crypt_errno.h', 'action': '定义SM4-HCTR算法相关的错误码',
         'description': '定义了加密相关的错误码。', 'order': 7},
        {'path': 'crypto/modes/include/crypt_modes_hctr.h', 'action': '定义SM4-HCTR算法的接口和类型',
         'description': '定义了加密模式的接口。', 'order': 8},
        {'path': 'crypto/modes/include/crypt_modes.h',
         'action': '定义HCTR模式的接口，为SM4算法提供统一的加解密操作接口',
         'description': '定义了加密模式接口，为对称加密算法提供统一的接口，用于初始化加密模式上下文，更新加密模式的加密/解密数据，完成加密模式的加密/解密操作。',
         'order': 9}, {'path': 'crypto/modes/src/modes_hctr.c', 'action': '实现SM4-HCTR算法的具体功能',
                       'description': '实现了加密模式的具体逻辑。', 'order': 10},
        {'path': 'crypto/provider/src/default/crypt_default_provider.c',
         'action': '在默认Provider中注册SM4-HCTR算法的能力查询',
         'description': '实现了默认 Provider 的功能，包括能力查询。', 'order': 11},
        {'path': 'crypto/provider/include/crypt_default_provderimpl.h',
         'action': '声明SM4-HCTR算法在默认Provider中的实现函数',
         'description': '是默认 Provider 的核心接口定义文件，声明了所有支持的密码学功能的实现函数。',
         'order': 12}, {'path': 'include/crypto/crypt_eal_implprovider.h',
                        'action': '定义SM4-HCTR算法的EAL层Provider接口',
                        'description': '定义了 EAL 层的接口，包括算法provider的注册、查询、创建和销毁等操作。',
                        'order': 13},
        {'path': 'include/crypto/crypt_types.h', 'action': '定义SM4-HCTR算法相关的通用数据类型',
         'description': '定义了密码学相关的通用数据类型和结构体，为整个项目提供了基础类型支持。',
         'order': 14},
        {'path': 'crypto/modes/src/noasm_sm4_hctr.c', 'action': '实现SM4-HCTR算法的具体功能',
         'description': '对通用加密模式接口的封装，适配特定算法，初始化加密模式上下文，更新加密模式的加密/解密数据，完成加密模式的加密/解密操作。',
         'order': 15}, {'path': 'crypto/provider/src/default/crypt_default_cipher.c',
                        'action': '为SM4-HCTR算法提供默认的对称加密实现',
                        'description': '为 openHiTLS 框架中的对称加密算法提供默认实现，上下文创建，算法支持，方法表定义等。',
                        'order': 16},
        {'path': 'testcode/framework/crypto/alg_check.c', 'action': '添加SM4-HCTR算法的可用性检查功能',
         'description': '检查和管理 openHiTLS 框架中各种加密算法的可用性。它通过一系列函数和数据结构，动态地确定哪些算法被启用或禁用，并提供相关的查询接口。',
         'order': 17}, {'path': 'testcode/sdv/testcase/crypto/sm4/test_suite_sdv_eal_sm4.c',
                        'action': '创建SM4-HCTR算法的测试相关文件',
                        'description': '该文件是一个测试套件，专门用于验证 openHiTLS 框架中加密算法的功能和正确性，测试算法，测试用例设计，错误处理测试。',
                        'order': 18},
        {'path': 'crypto/eal/src/eal_cipher_local.h', 'action': '定义SM4-HCTR算法的本地数据结构和状态',
         'description': 'openHiTLS 框架中 EAL（Encryption Abstraction Layer，加密抽象层）模块的一个头文件，主要用于定义对称加密相关的本地数据结构、状态和函数接口。',
         'order': 19}, {'path': 'testcode/sdv/testcase/crypto/sm4/test_suite_sdv_eal_sm4.data',
                        'action': '创建SM4-HCTR算法的测试相关文件',
                        'description': '纯数据文件，无依赖，包含测试用例的输入数据。', 'order': 20},
        {'path': 'testcode/sdv/testcase/crypto/eal/test_suite_sdv_eal.c',
         'action': '扩展EAL层测试套件，添加SM4-HCTR算法的测试用例',
         'description': '该文件是一个专门用于测试 EAL 层的测试套件。它通过定义一系列测试用例，验证了 EAL 层的功能、性能和错误处理能力。',
         'order': 21}
    ]
    user_query = "算法：SM4；模式：HCTR"
    tls_state = TaskAgentState()
    tls_state["task_files"] = task_files_simple
    tls_state["user_query"] = user_query
    result = coding_agent.with_config(recursion_limit=300).invoke({
        "substates": {"tls_state": tls_state}
    }, config)

    print("最终状态:", result)
