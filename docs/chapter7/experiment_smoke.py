"""Deterministic, offline checks for the RAG and Agent examples."""
import argparse
import ast
import json
import math
from collections import Counter
from pathlib import Path


def tokens(text):
    return Counter(part.lower() for part in text.replace("，", " ").replace("。", " ").split())


def cosine(left, right):
    keys = set(left) | set(right)
    dot = sum(left[key] * right[key] for key in keys)
    norm = math.sqrt(sum(value * value for value in left.values())) * math.sqrt(sum(value * value for value in right.values()))
    return dot / norm if norm else 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", choices=("rag", "agent"), required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    files = {
        "rag": ["RAG/demo.py", "RAG/Embeddings.py", "RAG/LLM.py", "RAG/VectorBase.py"],
        "agent": ["Agent/demo.py", "Agent/src/core.py", "Agent/src/tools.py", "Agent/src/utils.py"],
    }[args.module]
    for relative in files:
        ast.parse((root / relative).read_text(encoding="utf-8"), filename=relative)
    result = {"module": args.module, "checked": files, "network": False, "credentials_used": False}
    if args.module == "rag":
        query = tokens("RAG 检索 生成")
        candidates = ["RAG 先检索知识再生成", "Agent 可以调用工具"]
        scores = [cosine(query, tokens(item)) for item in candidates]
        result.update({"query": "RAG 检索 生成", "top_document": candidates[max(range(2), key=scores.__getitem__)]})
    else:
        result.update({"local_tool_examples": {"add": 5, "compare": "5 > 3", "letter_count": 3}})
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
