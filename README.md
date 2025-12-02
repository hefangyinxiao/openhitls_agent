# 使用uv进行环境管理
在项目根目录终端执行环境配置：
```
pip install uv
uv sync 
uv pip install -e .
```
激活uv环境:
```
source .venv/bin/activate
```

# 运行前准备阶段

参照`.env.example`的内容设置 `.env`

在终端执行脚本：
```
bash scripts/repo_clone.sh 
```
需要索引的代码仓库会clone到项目的`/workspace/repo`目录

```
docker run \
--restart always \
--publish=7474:7474 --publish=7687:7687 \
neo4j:2025.09.0
```
运行 neo4j 数据库，登录127.0.0.1:7474来到 neo4j 前端界面，默认账号密码均为`neo4j`，首次登录会提示修改密码，请自行修改并更新`.env`中的`NEO4J_PASSWORD`字段。

# 选择前端并运行项目
## 使用langgraph studio前端
终端运行：
```
langgraph dev
```
## 使用openWebUI作为对话前端
终端运行：
```
python backend/server.py 
```
然后部署OpenWebUI Pipeline并在Pipeline配置页面上传`backend/openwebui_pipeline.py`，设置好`backend/server.py`对应的后端url即可使用。

具体部署方式可参考OpenWebUI官方文档。

# SubAgent开发集成说明
## 开发与集成
新增细分领域agent需在`src/agents`目录下单开一个包（文件夹），并满足以下约定：

1. 包内需要包含一个名为`graph.py`的文件，在其中实例化你的新subgraph，并将类实例变量命名为`agent`。
2. subgraph实例化时需传入`name`参数，名称应能准确描述你agent的功能。

具体示例可参照`src/agents/mpc_agent`包。本项目提供的注册机制将自动处理集成你的subgraph，并创建路由分支。除此之外的子包内容可自行组织不受限制。

最后，你需要手动更新`scripts/repo_clone.sh`脚本，在其中添加对你需要索引的代码仓库的clone操作。
## 代码提交方式
请Fork本项目进行开发，完成开发与集成测试后以PR方式提交回本仓库。
## 需要讨论的事项
如果开发集成过程中遇到以下几种情况，请先与主仓维护者沟通讨论：

1. 需要添加/更新项目依赖。
2. 需要贡献通用工具组件到`toolkits`包。
3. 需要增加/修改你的子包和`scripts/repo_clone.sh`脚本以外的组件功能以支持某些特性。