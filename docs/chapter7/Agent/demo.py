"""CLI entry point for the chapter 7 tool-calling Agent."""
import argparse
import os

from openai import OpenAI

from src.core import Agent
from src.tools import add, compare, count_letter_in_string


def parse_args():
    parser = argparse.ArgumentParser(description="Happy-LLM Agent demo")
    parser.add_argument("--prompt", help="Run one request and exit; omit for interactive mode")
    parser.add_argument("--model", default="Qwen/Qwen2.5-32B-Instruct")
    return parser.parse_args()


def main():
    args = parse_args()
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    if not api_key or not base_url:
        raise SystemExit("请在受信任环境中配置 OPENAI_API_KEY 和 OPENAI_BASE_URL；不要把密钥写入代码。")
    agent = Agent(
        client=OpenAI(api_key=api_key, base_url=base_url),
        model=args.model,
        tools=[add, compare, count_letter_in_string],
    )
    if args.prompt:
        print(agent.get_completion(args.prompt))
        return
    while True:
        prompt = input("\033[94mUser (输入 exit 退出): \033[0m").strip()
        if prompt.lower() == "exit":
            break
        print("\033[92mAssistant: \033[0m", agent.get_completion(prompt))


if __name__ == "__main__":
    main()
