import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_milvus import Milvus
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ----------------- 初始化设置 -----------------
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com/'

MILVUS_URI = "src/agent/planning/RAG/milvus_0.6b.openhitls.db"
COLLECTION_NAME = "markdown_collection"

# 预加载模型（全局变量）
embedding_model = HuggingFaceEmbeddings(
    model_name="./workspace/model_cache/qwen/Qwen3-Embedding-0.6B",
    model_kwargs={"device": "cuda", "local_files_only": True},
    encode_kwargs={"normalize_embeddings": False}
)

vector_db = Milvus(
    embedding_function=embedding_model,
    collection_name=COLLECTION_NAME,
    connection_args={"uri": MILVUS_URI},
)

rerank_model = AutoModelForCausalLM.from_pretrained(
    "./workspace/model_cache/qwen/Qwen3-Reranker-0.6B",
    device_map="cuda",
    local_files_only=True,
    torch_dtype=torch.float16
).eval()

rerank_tokenizer = AutoTokenizer.from_pretrained(
    "./workspace/model_cache/qwen/Qwen3-Reranker-0.6B",
    padding_side="right",
    local_files_only=True,
    pad_token="<|endoftext|>"
)

# ----------------- 查询函数 -----------------
def search_with_rerank(query: str, top_k: int = 10, rerank_top_k: int = 5):
    try:
        # 第一步：向量检索
        retrieved_docs = vector_db.similarity_search(query, k=top_k)
        if not retrieved_docs:
            return []

        # 第二步：重排序
        scored_docs = []
        for doc in retrieved_docs:
            if not doc.page_content.strip():
                continue

            inputs = rerank_tokenizer(
                query,
                doc.page_content,
                truncation='only_second',
                max_length=4096,
                padding='max_length',
                return_tensors="pt"
            ).to(rerank_model.device)

            with torch.no_grad():
                outputs = rerank_model(**inputs)
                score = outputs.logits[0, -1, 0].item()

            scored_docs.append((score, doc))

        # 按分数排序并返回前k个结果
        scored_docs.sort(key=lambda x: x[0], reverse=True)
        return [doc for (score, doc) in scored_docs[:rerank_top_k]]

    except Exception as e:
        print(f"检索过程中出错: {str(e)}")
        return retrieved_docs[:rerank_top_k] if retrieved_docs else []

# ----------------- 示例查询 -----------------
if __name__ == "__main__":
    query = "用户需求基于OpenHitls实现SM4_HCTR算法"
    results = search_with_rerank(query, top_k=20, rerank_top_k=10)

    print(f"查询: '{query}'")
    for i, doc in enumerate(results):
        print(f"\n结果 {i + 1}:")
        print(f"来源文件: {doc.metadata.get('source', '未知')}")
        print(f"内容: {doc.page_content[:200]}...")  # 只打印前200字符避免输出过长