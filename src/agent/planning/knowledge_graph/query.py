from neomodel import db

from agent.planning.knowledge_graph.build import create_generic_crypto_framework, establish_generic_dependencies
from agent.planning.knowledge_graph.db import setup_neo4j_connection, test_connection, clear_existing_data
from agent.planning.knowledge_graph.model import CodeFile


def find_all_dependencies(file_path):
    """查找文件的所有直接和间接依赖"""
    try:
        # 使用单个 Cypher 查询获取所有依赖，避免多次递归查询
        query = """
        MATCH (start:CodeFile {path: $file_path})-[:DEPENDS_ON*]->(dep:CodeFile)
        RETURN DISTINCT dep.path as dependency_path, dep.desc as description, dep.file_type as type
        ORDER BY 
            CASE 
                WHEN dep.file_type = 'config_required' THEN 1
                WHEN dep.file_type = 'definition_required' THEN 2
                WHEN dep.file_type = 'registration_required' THEN 3
                ELSE 4
            END,
            dependency_path
        """
        results, meta = db.cypher_query(query, {'file_path': file_path})

        dependencies = []
        for result in results:
            dependencies.append({
                'path': result[0],
                'description': result[1],
                'type': result[2]
            })
        return dependencies
    except Exception as e:
        print(f"查询依赖关系失败: {e}")
        return []

def find_dependents(file_path):
    """查找哪些文件依赖于此文件"""
    try:
        query = """
        MATCH (dependent:CodeFile)-[:DEPENDS_ON]->(target:CodeFile {path: $file_path})
        RETURN dependent.path as dependent_path, dependent.desc as description, dependent.file_type as type
        ORDER BY dependent_path
        """
        results, meta = db.cypher_query(query, {'file_path': file_path})

        dependents = []
        for result in results:
            dependents.append({
                'path': result[0],
                'description': result[1],
                'type': result[2]
            })
        return dependents
    except Exception as e:
        print(f"查询依赖者失败: {e}")
        return []

def demo_dependency_queries():
    """演示依赖关系查询"""

    # 查询EAL注册文件的依赖链
    print("   EAL注册文件的完整依赖链:")
    deps = find_all_dependencies("crypto/eal/src/eal_cipher_method.c")
    for dep in deps:
        print(f"      → {dep}")

    # 查询哪些文件依赖算法定义
    print("\n   依赖算法定义的文件:")
    users = find_dependents("include/crypto/crypt_algid.h")
    for user in users:
        print(f"      ← {user}")

def init_practical_database():
    """初始化实用型密码架构数据库 - 修复版本"""
    setup_neo4j_connection()

    if not test_connection():
        return None

    clear_existing_data()

    print("开始创建文件节点...")
    files = create_generic_crypto_framework()

    print("开始建立依赖关系...")
    established_count = establish_generic_dependencies(files)

    print(f"✓ 数据库初始化完成！创建了 {len(files)} 个节点，建立了 {established_count} 个依赖关系")
    return files

def generate_action_description(file_path, algorithm_name, mode_name):
    """根据文件路径生成具体的操作描述"""

    # 基于文件路径的关键字生成相应的操作说明
    if 'feature.json' in file_path:
        return f'在hitls_crypto->cipher->c数组中添加"{algorithm_name}"特性开关'

    elif 'hitls_config_layer_crypto.h' in file_path:
        macro_name = f"HITLS_CRYPTO_{algorithm_name.upper()}_{mode_name.upper() if mode_name else algorithm_name.upper()}"
        return f'添加 #define {macro_name} 宏定义'

    elif 'crypt_algid.h' in file_path:
        algid_name = f"CRYPT_CIPHER_{algorithm_name.upper()}_{mode_name.upper() if mode_name else algorithm_name.upper()}"
        return f'定义 {algid_name} 算法ID常量'

    elif 'crypt_errno.h' in file_path:
        return f'添加{algorithm_name.upper()}算法相关的错误码定义'

    elif 'eal_cipher_method.c' in file_path:
        return f'在EAL密码方法表中注册{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法'

    elif 'crypt_default_cipher.c' in file_path:
        return f'在默认Provider中注册{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法'

    else:
        return f'修改文件以支持{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法'

def replace_pattern_with_names(pattern, algorithm_name, mode_name):
    """将文件路径模式替换为具体的算法和模式名称"""

    concrete_path = pattern

    # 替换算法名占位符
    if '*' in pattern:
        if 'modes_*' in pattern:
            if mode_name:
                concrete_path = concrete_path.replace('modes_*', f'modes_{mode_name}')
        if 'noasm_*_*' in pattern:
            if algorithm_name and mode_name:
                concrete_path = concrete_path.replace('noasm_*_*', f'noasm_{algorithm_name}_{mode_name}')
        if 'crypt_modes_*' in pattern:
            if mode_name:
                concrete_path = concrete_path.replace('crypt_modes_*', f'crypt_modes_{mode_name}')
        if 'test_suite_sdv_eal_*' in pattern:
            concrete_path = concrete_path.replace('test_suite_sdv_eal_*', f'test_suite_sdv_eal_{algorithm_name}')
        if 'crypto/*/' in pattern:
            concrete_path = concrete_path.replace('crypto/*/', f'crypto/{algorithm_name}/')

    return concrete_path

def generate_creation_description(pattern, algorithm_name, mode_name):
    """生成新文件创建描述 - 基于完整框架定义"""

    # 配置层文件
    if 'feature.json' in pattern:
        return f'配置{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法特性开关和编译选项'

    elif 'hitls_config_layer_crypto.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}相关的功能控制宏'

    # EAL层文件
    elif 'eal_cipher_method.c' in pattern:
        return f'在EAL密码方法表中注册{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法'

    elif 'eal_cipher_local.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的本地数据结构和状态'

    # 类型定义文件
    elif 'crypt_local_types.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法相关的本地类型和函数指针'

    elif 'crypt_types.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法相关的通用数据类型'

    elif 'crypt_algid.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的唯一标识符'

    elif 'crypt_errno.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法相关的错误码'

    # 模式层文件
    elif 'crypt_modes_*.h' in pattern or 'crypt_modes.h' in pattern:
        if mode_name:
            return f'定义{mode_name.upper()}模式的接口，为{algorithm_name.upper()}算法提供统一的加解密操作接口'
        else:
            return f'定义{algorithm_name.upper()}算法的通用模式接口'

    elif 'modes_*.c' in pattern:
        if mode_name:
            return f'实现{mode_name.upper()}模式的具体逻辑，支持{algorithm_name.upper()}算法的加解密操作'
        else:
            return f'实现{algorithm_name.upper()}算法的通用模式逻辑'

    elif 'noasm_*_*.c' in pattern:
        if algorithm_name and mode_name:
            return f'创建{algorithm_name.upper()}-{mode_name.upper()}算法绑定实现，适配通用模式接口'
        else:
            return f'创建{algorithm_name.upper()}算法的平台无关实现'

    # Provider层文件
    elif 'crypt_default_provider.c' in pattern:
        return f'在默认Provider中注册{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的能力查询'

    elif 'crypt_default_provderimpl.h' in pattern:
        return f'声明{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法在默认Provider中的实现函数'

    elif 'crypt_default_cipher.c' in pattern:
        return f'为{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法提供默认的对称加密实现'

    elif 'crypt_eal_implprovider.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的EAL层Provider接口'

    # BSL层文件
    elif 'bsl_obj.h' in pattern:
        return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法相关的对象管理接口'

    # 测试文件
    elif 'test_suite_sdv_eal_*.c' in pattern:
        return f'创建{algorithm_name.upper()}算法的测试套件，验证功能正确性和错误处理'

    elif 'test_suite_sdv_eal_*.data' in pattern:
        return f'提供{algorithm_name.upper()}算法的测试数据，包含各种边界情况的输入数据'

    elif 'test_suite_sdv_eal.c' in pattern:
        return f'扩展EAL层测试套件，添加{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的测试用例'

    elif 'alg_check.c' in pattern:
        return f'添加{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的可用性检查功能'

    # 通用描述
    else:
        # 根据文件路径的关键字生成描述
        if 'test' in pattern:
            return f'创建{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的测试相关文件'
        elif 'include' in pattern or '.h' in pattern:
            return f'定义{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的接口和类型'
        elif 'src' in pattern or '.c' in pattern:
            return f'实现{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}算法的具体功能'
        else:
            return f'创建{algorithm_name.upper()}{f"-{mode_name.upper()}" if mode_name else ""}相关实现文件'

def get_dependency_execution_order(algorithm_name, mode_name):
    """获取基于依赖关系的执行顺序"""

    query = """
   // 找到所有没有入边的节点（起点）
MATCH (start:CodeFile)
WHERE NOT (start)<-[:DEPENDS_ON]-()
WITH start
// 对每个起点进行拓扑排序
CALL {
    WITH start
    MATCH path = (start)-[:DEPENDS_ON*0..]->(leaf)
    WHERE NOT (leaf)-[:DEPENDS_ON]->()
    RETURN nodes(path) as nodes_in_path
}
// 收集所有路径并去重
UNWIND nodes_in_path as node
WITH DISTINCT node
RETURN node.path as path, node.desc as description
// 拓扑排序已经隐含在路径顺序中，直接返回即可
    """

    try:
        results, meta = db.cypher_query(query)

        # 转换为与注册清单一致的格式
        execution_files = []
        for i, result in enumerate(results):
            file_path = result[0]
            description = result[1]

            file_path = replace_pattern_with_names(file_path, algorithm_name, mode_name)
            action = generate_creation_description(file_path, algorithm_name, mode_name)


            execution_files.append({
                'path': file_path,
                'action': action,
                'description': description,
                'order': i + 1
            })

        return execution_files

    except Exception as e:
        print(f"获取依赖顺序失败: {e}")


def get_registration_checklist_from_graph(algorithm_name, mode_name=None):
    """从图数据库中动态生成新算法的注册清单 - 修复版本"""

    checklist = []

    # 1. 首先获取所有必须修改的现有文件（非模式文件）
    existing_files_query = """
    MATCH (file:CodeFile)
    WHERE NOT file.path CONTAINS '*' AND NOT file.path CONTAINS 'pattern'
    AND (file.file_type CONTAINS 'required' OR file.file_type CONTAINS 'registration' OR file.file_type CONTAINS 'definition')
    RETURN file.path as path, file.desc as description, file.file_type as type
    ORDER BY 
        CASE 
            WHEN file.file_type = 'config_required' THEN 1
            WHEN file.file_type = 'definition_required' THEN 2
            WHEN file.file_type = 'registration_required' THEN 3
            ELSE 4
        END
    """

    try:
        # 查询现有文件
        existing_results, meta = db.cypher_query(existing_files_query)

        # 处理现有文件（需要修改的文件）
        if existing_results:
            checklist.append({
                'category': '必须修改的现有文件',
                'files': []
            })

            for result in existing_results:
                file_path = result[0]
                description = result[1]
                file_type = result[2]

                # 根据文件类型和路径生成具体的操作说明
                action = generate_action_description(file_path, algorithm_name, mode_name)

                checklist[0]['files'].append({
                    'path': file_path,
                    'action': action,
                    'type': '修改现有文件',
                    'description': description
                })

        # 2. 查询需要创建的模式文件模板
        pattern_files_query = """
        MATCH (file:CodeFile)
        WHERE file.path CONTAINS '*' OR file.path CONTAINS 'pattern' OR file.file_type = 'implementation_pattern'
        RETURN file.path as pattern, file.desc as description, file.file_type as type
        """

        pattern_results, meta = db.cypher_query(pattern_files_query)

        if pattern_results:
            checklist.append({
                'category': '需要创建的新文件',
                'files': []
            })

            for result in pattern_results:
                pattern = result[0]
                description = result[1]
                file_type = result[2]

                # 将模式替换为具体的算法和模式名称
                concrete_path = replace_pattern_with_names(pattern, algorithm_name, mode_name)
                action = generate_creation_description(pattern, algorithm_name, mode_name)

                checklist[1]['files'].append({
                    'path': concrete_path,
                    'action': action,
                    'type': '新建文件',
                    'original_pattern': pattern,
                    'description': description
                })

        # 3. 查询依赖关系，确定执行顺序 - 使用修复后的函数
        dependency_order = get_dependency_execution_order(algorithm_name, mode_name)
        checklist.append({
            'category': '推荐执行顺序',
            'files': dependency_order,  # 直接使用返回的文件列表
            'is_order': True
        })

        return checklist

    except Exception as e:
        print(f"从图数据库生成清单失败: {e}")


def demo_graph_based_checklist():
    """演示基于图的动态清单生成 - 修复版本"""

    print("\n" + "=" * 60)
    print("基于图数据库的动态注册清单")
    print("=" * 60)

    # 生成SM4-HCTR的注册清单
    checklist = get_registration_checklist_from_graph("sm4", "hctr")

    total_steps = 0
    for category in checklist:
        if 'is_order' in category and category['is_order']:
            print(f"\n📋 {category['category']}:")
            for file_info in category['files']:  # 统一使用 file_info
                icon = "🔢"  # 使用数字图标表示执行顺序
                print(f"   {icon} {file_info['order']}. {file_info['path']}")
                print(f"      操作: {file_info['action']}")
                if 'description' in file_info:
                    print(f"      说明: {file_info['description']}")
        else:
            total_steps += len(category['files'])
            print(f"\n📁 {category['category']}:")
            for file_info in category['files']:
                icon = "📄" if file_info['type'] == '新建文件' else "✏️"
                print(f"   {icon} {file_info['path']}")
                print(f"      操作: {file_info['action']}")
                if 'description' in file_info:
                    print(f"      说明: {file_info['description']}")

    print(f"\n总计需要处理 {total_steps} 个文件")

# 更新主演示函数
def demo_practical_usage():
    """演示实际使用场景 - 使用图数据库版本"""

    print("\n" + "="*60)
    print("密码算法注册实用指南（图数据库驱动）")
    print("="*60)

    # 使用图数据库生成清单
    demo_graph_based_checklist()

    # 其他演示功能保持不变
    print("\n2. 依赖关系查询演示:")
    demo_dependency_queries()

from neomodel import db

def find_dependency_chain(start_path):
    """
    从指定路径的节点开始，沿着 depends_on 关系回溯到树根
    返回从根节点到当前节点的路径列表
    """
    # 查询回溯到根节点的路径
    query = """
    MATCH (start:CodeFile {path: $start_path})
    MATCH path = (root:CodeFile)-[:DEPENDS_ON*]->(start)
    WHERE NOT (root)-[:DEPENDS_ON]->(:CodeFile)
    RETURN nodes(path) as nodes
    ORDER BY length(path) DESC
    LIMIT 1
    """

    results, meta = db.cypher_query(query, {'start_path': start_path})

    if results and results[0]:
        nodes = [CodeFile.inflate(node) for node in results[0][0]]
        return nodes
    else:
        # 如果没有找到路径，可能当前节点就是根节点
        start_node = CodeFile.nodes.get(path=start_path)
        return [start_node]

def print_dependency_chain(start_path):
    """
    打印从根节点到指定节点的依赖链
    """
    try:
        chain = find_dependency_chain(start_path)

        print(f"依赖链 (从根节点到 {start_path}):")
        print("-" * 50)

        for i, code_file in enumerate(chain, 1):
            print(f"{i}. 路径: {code_file.path}")
            print(f"   描述: {code_file.desc}")
            print(f"   文件类型: {code_file.file_type}")
            print(f"   类别: {code_file.category}")
            print()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("开始初始化密码架构图数据库...")
    files = init_practical_database()

    start_path = "testcode/sdv/testcase/crypto/*/test_suite_sdv_eal_*.c"
    print_dependency_chain(start_path)


    if files:
        demo_practical_usage()
        print("\n✓ 演示完成！")
    else:
        print("数据库初始化失败！")