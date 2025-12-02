
from agent.planning.knowledge_graph.model import CodeFile
def create_generic_crypto_framework():
    """创建完整的密码架构框架"""

    framework_files = {}

    # 0. config/json/feature.json
    framework_files['config/json/feature.json'] = CodeFile(
        path="config/json/feature.json",
        desc="特性配置文件 - 定义所有算法特性、依赖关系和编译选项。所有新增特性需要在此注册。",
        file_type="config_required",
        category='generic'
    ).save()

    # 1. config/macro_config/hitls_config_layer_crypto.h
    framework_files['config/macro_config/hitls_config_layer_crypto.h'] = CodeFile(
        path="config/macro_config/hitls_config_layer_crypto.h",
        desc="定义了与加密相关的宏，用于控制功能的启用和禁用。",
        file_type="config_required",
        category='generic'
    ).save()

    # 2. crypto/eal/src/eal_cipher_method.c
    framework_files['crypto/eal/src/eal_cipher_method.c'] = CodeFile(
        path="crypto/eal/src/eal_cipher_method.c",
        desc="实现了加密算法的注册和方法表。",
        file_type="implementation_required",
        category='crypto'
    ).save()

    # 3. crypto/include/crypt_local_types.h
    framework_files['crypto/include/crypt_local_types.h'] = CodeFile(
        path="crypto/include/crypt_local_types.h",
        desc="定义了加密相关的本地类型。是 openHiTLS 项目中定义本地加密类型和方法的核心头文件，它主要定义了加密框架中使用的各种数据结构、函数指针类型和枚举，用于支持对称加密、哈希、MAC、KDF、随机数生成等操作。",
        file_type="definition_required",
        category='crypto'
    ).save()

    # 4. crypto/modes/include/crypt_modes_*.h
    framework_files['crypto/modes/include/crypt_modes_*.h'] = CodeFile(
        path="crypto/modes/include/crypt_modes_*.h",
        desc="定义了加密模式的接口。",
        file_type="interface_required",
        category='crypto'
    ).save()

    # 5. crypto/modes/src/modes_*.c
    framework_files['crypto/modes/src/modes_*.c'] = CodeFile(
        path="crypto/modes/src/modes_*.c",
        desc="实现了加密模式的具体逻辑。",
        file_type="implementation_required",
        category='crypto'
    ).save()

    # 6. crypto/provider/src/default/crypt_default_provider.c
    framework_files['crypto/provider/src/default/crypt_default_provider.c'] = CodeFile(
        path="crypto/provider/src/default/crypt_default_provider.c",
        desc="实现了默认 Provider 的功能，包括能力查询。",
        file_type="implementation_required",
        category='crypto'
    ).save()

    # 7. include/bsl/bsl_obj.h
    framework_files['include/bsl/bsl_obj.h'] = CodeFile(
        path="include/bsl/bsl_obj.h",
        desc="定义了对象管理的接口。",
        file_type="definition_required",
        category='generic'
    ).save()

    # 8. include/crypto/crypt_algid.h
    framework_files['include/crypto/crypt_algid.h'] = CodeFile(
        path="include/crypto/crypt_algid.h",
        desc="定义了所有支持的算法 ID。通过一系列枚举类型定义了框架支持的各种加密算法、模式和参数的唯一标识符。这些 ID 在框架中被广泛使用，用于标识和选择具体的加密算法或模式。",
        file_type="definition_required",
        category='crypto'
    ).save()

    # 9. include/crypto/crypt_errno.h
    framework_files['include/crypto/crypt_errno.h'] = CodeFile(
        path="include/crypto/crypt_errno.h",
        desc="定义了加密相关的错误码。",
        file_type="definition_required",
        category='crypto'
    ).save()

    # 10. testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.data
    framework_files['testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.data'] = CodeFile(
        path="testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.data",
        desc="纯数据文件，无依赖，包含测试用例的输入数据。",
        file_type="test_required",
        category='test'
    ).save()

    # 11. crypto/modes/src/noasm_*_*.c
    framework_files['crypto/modes/src/noasm_*_*.c'] = CodeFile(
        path="crypto/modes/src/noasm_*_*.c",
        desc="对通用加密模式接口的封装，适配特定算法，初始化加密模式上下文，更新加密模式的加密/解密数据，完成加密模式的加密/解密操作。",
        file_type="implementation_required",
        category='crypto'
    ).save()

    # 12. crypto/provider/include/crypt_default_provderimpl.h
    framework_files['crypto/provider/include/crypt_default_provderimpl.h'] = CodeFile(
        path="crypto/provider/include/crypt_default_provderimpl.h",
        desc="是默认 Provider 的核心接口定义文件，声明了所有支持的密码学功能的实现函数。",
        file_type="interface_required",
        category='crypto'
    ).save()

    #?
    framework_files['include/crypto/crypt_eal_implprovider.h'] = CodeFile(
        path="include/crypto/crypt_eal_implprovider.h",
        desc="定义了 EAL 层的接口，包括算法provider的注册、查询、创建和销毁等操作。",
        file_type="interface_required",
        category='crypto'
    ).save()

    # 13. include/crypto/crypt_types.h
    framework_files['include/crypto/crypt_types.h'] = CodeFile(
        path="include/crypto/crypt_types.h",
        desc="定义了密码学相关的通用数据类型和结构体，为整个项目提供了基础类型支持。",
        file_type="definition_required",
        category='crypto'
    ).save()

    # 14. crypto/provider/src/default/crypt_default_cipher.c
    framework_files['crypto/provider/src/default/crypt_default_cipher.c'] = CodeFile(
        path="crypto/provider/src/default/crypt_default_cipher.c",
        desc="为 openHiTLS 框架中的对称加密算法提供默认实现，上下文创建，算法支持，方法表定义等。",
        file_type="implementation_required",
        category='crypto'
    ).save()

    # 15. testcode/framework/crypto/alg_check.c
    framework_files['testcode/framework/crypto/alg_check.c'] = CodeFile(
        path="testcode/framework/crypto/alg_check.c",
        desc="检查和管理 openHiTLS 框架中各种加密算法的可用性。它通过一系列函数和数据结构，动态地确定哪些算法被启用或禁用，并提供相关的查询接口。",
        file_type="test_required",
        category='test'
    ).save()

    # 16. testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c
    framework_files['testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c'] = CodeFile(
        path="testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c",
        desc="该文件是一个测试套件，专门用于验证 openHiTLS 框架中加密算法的功能和正确性，测试算法，测试用例设计，错误处理测试。",
        file_type="test_required",
        category='test'
    ).save()

    # 17. testcode/sdv/testcase/crypto/eal/test_suite_sdv_eal.c
    framework_files['testcode/sdv/testcase/crypto/eal/test_suite_sdv_eal.c'] = CodeFile(
        path="testcode/sdv/testcase/crypto/eal/test_suite_sdv_eal.c",
        desc="该文件是一个专门用于测试 EAL 层的测试套件。它通过定义一系列测试用例，验证了 EAL 层的功能、性能和错误处理能力。",
        file_type="test_required",
        category='test'
    ).save()

    # 18. crypto/eal/src/eal_cipher_local.h
    framework_files['crypto/eal/src/eal_cipher_local.h'] = CodeFile(
        path="crypto/eal/src/eal_cipher_local.h",
        desc="openHiTLS 框架中 EAL（Encryption Abstraction Layer，加密抽象层）模块的一个头文件，主要用于定义对称加密相关的本地数据结构、状态和函数接口。",
        file_type="definition_required",
        category='crypto'
    ).save()

    # 19. crypto/modes/include/crypt_modes.h
    framework_files['crypto/modes/include/crypt_modes.h'] = CodeFile(
        path="crypto/modes/include/crypt_modes.h",
        desc="定义了加密模式接口，为对称加密算法提供统一的接口，用于初始化加密模式上下文，更新加密模式的加密/解密数据，完成加密模式的加密/解密操作。",
        file_type="interface_required",
        category='crypto'
    ).save()

    print(f"✓ 已创建并保存 {len(framework_files)} 个完整文件节点")
    return framework_files


def establish_generic_dependencies(files):
    """建立完整的依赖关系"""

    dependencies = [
        # 1. 配置宏依赖特性配置文件
        ("config/macro_config/hitls_config_layer_crypto.h", "config/json/feature.json"),

        # 2-6. EAL加密方法实现的核心依赖
        ("crypto/eal/src/eal_cipher_method.c", "config/macro_config/hitls_config_layer_crypto.h"),
        ("crypto/eal/src/eal_cipher_method.c", "crypto/include/crypt_local_types.h"),
        ("crypto/eal/src/eal_cipher_method.c", "include/crypto/crypt_algid.h"),
        ("crypto/eal/src/eal_cipher_method.c", "include/crypto/crypt_errno.h"),
        ("crypto/eal/src/eal_cipher_method.c", "crypto/modes/include/crypt_modes_*.h"),

        # 7,15. 本地类型定义依赖算法ID
        ("crypto/include/crypt_local_types.h", "include/crypto/crypt_algid.h"),

        # 8,11,13. 加密模式接口依赖基础模式定义
        ("crypto/modes/include/crypt_modes_*.h", "crypto/modes/include/crypt_modes.h"),

        # 9-10,12. 加密模式实现依赖
        ("crypto/modes/src/modes_*.c", "bsl/err/include/bsl_err_internal.h"),
        ("crypto/modes/src/modes_*.c", "include/crypto/crypt_errno.h"),
        ("crypto/modes/src/modes_*.c", "crypto/modes/include/crypt_modes_*.h"),

        # 14. 基础模式定义依赖本地类型
        ("crypto/modes/include/crypt_modes.h", "crypto/include/crypt_local_types.h"),

        # 16. 无汇编实现依赖特定模式接口
        ("crypto/modes/src/noasm_*_*.c", "crypto/modes/include/crypt_modes_*.h"),

        # 17-18. Provider实现层次依赖
        ("crypto/provider/include/crypt_default_provderimpl.h", "include/crypto/crypt_eal_implprovider.h"),
        ("include/crypto/crypt_eal_implprovider.h", "include/crypto/crypt_types.h"),

        # 19-21. 默认Provider实现依赖
        ("crypto/provider/src/default/crypt_default_provider.c", "include/crypto/crypt_algid.h"),
        ("crypto/provider/src/default/crypt_default_provider.c", "crypto/provider/include/crypt_default_provderimpl.h"),
        ("crypto/provider/src/default/crypt_default_provider.c", "include/bsl/bsl_obj.h"),

        # 22-24. 默认加密实现依赖
        ("crypto/provider/src/default/crypt_default_cipher.c", "crypto/include/crypt_local_types.h"),
        ("crypto/provider/src/default/crypt_default_cipher.c", "crypto/modes/include/crypt_modes_*.h"),
        ("crypto/provider/src/default/crypt_default_cipher.c", "include/crypto/crypt_eal_implprovider.h"),

        # 25. BSL对象定义依赖类型定义
        ("include/bsl/bsl_obj.h", "include/bsl/bsl_types.h"),

        # 26. 算法ID定义依赖BSL对象管理
        ("include/crypto/crypt_algid.h", "include/bsl/bsl_obj.h"),

        # 28. 算法检查依赖算法ID定义
        ("testcode/framework/crypto/alg_check.c", "include/crypto/crypt_algid.h"),

        # 29-30. 测试套件依赖
        ("testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c", "crypto/eal/src/eal_cipher_local.h"),
        ("testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c", "include/crypto/crypt_errno.h"),

        # 31. EAL测试套件依赖
        ("testcode/sdv/testcase/crypto/eal/test_suite_sdv_eal.c", "crypto/eal/src/eal_cipher_local.h"),

        # 32. 测试套件依赖数据文件
        ("testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c",
         "testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.data"),

        ("testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c","include/bsl/bsl_sal.h"),
        ("crypto/eal/src/eal_cipher_local.h","include/crypto/crypt_algid.h"),
        ("crypto/eal/src/eal_cipher_local.h","include/crypto/crypt_eal_cipher.h"),
        ("","include/bsl/bsl_sal.h")
    ]

    established_count = 0
    for source_key, target_key in dependencies:
        try:
            if source_key in files and target_key in files:
                source = files[source_key]
                target = files[target_key]
                source.depends_on.connect(target)
                established_count += 1
                print(f"  建立依赖: {source_key} -> {target_key}")
            else:
                print(f"  跳过缺失的依赖: {source_key} -> {target_key}")
        except Exception as e:
            print(f"  建立依赖失败 {source_key} -> {target_key}: {e}")

    print(f"✓ 已建立 {established_count} 个完整依赖关系")
    return established_count