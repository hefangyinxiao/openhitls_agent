import os

from modelscope import snapshot_download
from transformers import AutoModel, AutoTokenizer

# 配置
MODELS = {
    "embedding": "qwen/Qwen3-Embedding-0.6B",  # ModelScope的模型ID
    "reranker": "qwen/Qwen3-Reranker-0.6B"
}
CACHE_DIR = "./workspace/model_cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def download_with_modelscope(model_name: str):
    try:
        print(f"⬇️ 正在通过ModelScope下载 {model_name}...")

        # 关键下载参数
        model_dir = snapshot_download(
            model_id=model_name,
            cache_dir=CACHE_DIR,
            revision='master',  # 使用主分支
            ignore_file_pattern=[".*.md", "*.bin"],  # 过滤非必要文件
        )
        print(f"✅ 下载完成！模型保存到: {model_dir}")
        return model_dir
    except Exception as e:
        print(f"❌ 下载失败: {str(e)}")
        return None


if __name__ == "__main__":
    for model_type, model_name in MODELS.items():
        model_path = download_with_modelscope(model_name)

        # 验证模型
        if model_path:
            try:
                print("🧪 验证模型加载...")
                if "Embedding" in model_name:
                    from langchain_huggingface import HuggingFaceEmbeddings

                    embedding = HuggingFaceEmbeddings(
                        model_name=model_path,
                        model_kwargs={"device": "cpu"}
                    )
                    print(f"嵌入模型测试结果: {len(embedding.embed_documents(['测试'])[0])}维")
                else:
                    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
                    model = AutoModel.from_pretrained(model_path, trust_remote_code=True)
                    print(f"重排序模型参数量: {sum(p.numel() for p in model.parameters()):,}")
            except Exception as e:
                print(f"⚠️ 模型验证失败: {str(e)}")