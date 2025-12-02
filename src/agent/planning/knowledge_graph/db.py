import os

from neomodel import db, config

from agent.planning.knowledge_graph.model import CodeFile
def setup_neo4j_connection():
    """配置Neo4j数据库连接"""
    # 从环境变量获取配置，或者使用默认值
    neo4j_url = os.getenv('NEO4J_BOLT_URL', 'bolt://localhost:7687')
    neo4j_user = os.getenv('NEO4J_USER', 'neo4j')
    neo4j_password = os.getenv('NEO4J_PASSWORD', '20991218')

    config.DATABASE_URL = f'bolt://{neo4j_user}:{neo4j_password}@{neo4j_url.replace("bolt://", "")}'

    print(f"连接Neo4j数据库: {neo4j_url}")

def clear_existing_data():
    """清空现有数据（可选）"""
    try:
        # 使用db.cypher_query来执行原生Cypher查询
        query = "MATCH (n) DETACH DELETE n"
        results, meta = db.cypher_query(query)
        print("✓ 已清空现有数据")
    except Exception as e:
        print(f"清空数据时出错: {e}")

def test_connection():
    """测试数据库连接"""
    try:
        # 尝试执行一个简单查询
        result = CodeFile.nodes.all()[:1]
        print("✓ Neo4j连接成功")
        return True
    except Exception as e:
        print(f"✗ Neo4j连接失败: {e}")
        print("请检查:")
        print("1. Neo4j服务是否启动")
        print("2. 连接配置是否正确")
        print("3. 数据库地址、用户名、密码是否正确")
        return False
