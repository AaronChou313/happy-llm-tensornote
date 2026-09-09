"""Run the chapter 7 RAG demo with explicit paths and credentials."""
import argparse
import os
from pathlib import Path

from Embeddings import OpenAIEmbedding
from LLM import OpenAIChat
from VectorBase import VectorStore
from utils import ReadFiles


def parse_args():
    parser = argparse.ArgumentParser(description="Happy-LLM RAG demo")
    parser.add_argument("--data-dir", default="data", help="Markdown, text, or PDF document directory")
    parser.add_argument("--storage-dir", default=".tensornote-runs/rag-storage")
    parser.add_argument("--question", default="RAG 的原理是什么？")
    parser.add_argument("--chat-model", default="Qwen/Qwen2.5-32B-Instruct")
    parser.add_argument("--top-k", type=int, default=1)
    return parser.parse_args()


def main():
    args = parse_args()
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("缺少 OPENAI_API_KEY。请在 TensorNote 的受信任运行环境中配置，不要写入笔记或仓库。")
    if not os.getenv("OPENAI_BASE_URL"):
        raise SystemExit("缺少 OPENAI_BASE_URL。请为兼容 OpenAI API 的服务配置地址。")
    data_dir = Path(args.data_dir)
    if not data_dir.is_dir():
        raise SystemExit(f"文档目录不存在：{data_dir}")
    docs = ReadFiles(str(data_dir)).get_content(max_token_len=600, cover_content=150)
    if not docs:
        raise SystemExit(f"文档目录中没有可读取的 md、txt 或 pdf 文件：{data_dir}")
    embedding = OpenAIEmbedding()
    vector = VectorStore(docs)
    vector.get_vector(EmbeddingModel=embedding)
    vector.persist(path=args.storage_dir)
    matches = vector.query(args.question, EmbeddingModel=embedding, k=args.top_k)
    context = matches[0] if matches else ""
    print(OpenAIChat(model=args.chat_model).chat(args.question, [], context))


if __name__ == "__main__":
    main()
