"""Prepare chapter 5 pretraining and SFT JSONL files reproducibly."""
import argparse
import json
from pathlib import Path


def split_text(text, chunk_size=512):
    return [text[index:index + chunk_size] for index in range(0, len(text), chunk_size)]


def read_jsonl(path):
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if line.strip():
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as error:
                    raise ValueError(f"{path}:{number}: invalid JSON") from error


def write_pretrain(source, destination, chunk_size):
    count = 0
    with destination.open("w", encoding="utf-8") as output:
        for row in read_jsonl(source):
            text = row.get("text")
            if not isinstance(text, str):
                raise ValueError(f"{source} contains a record without string field 'text'")
            for chunk in split_text(text, chunk_size):
                if chunk.strip():
                    output.write(json.dumps({"text": chunk}, ensure_ascii=False) + "\n")
                    count += 1
    return count


def write_sft(source, destination):
    count = 0
    with destination.open("w", encoding="utf-8") as output:
        for row in read_jsonl(source):
            conversations = row.get("conversations")
            if not isinstance(conversations, list):
                raise ValueError(f"{source} contains a record without list field 'conversations'")
            output.write(json.dumps({"conversations": conversations}, ensure_ascii=False) + "\n")
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pretrain-input", type=Path, required=True)
    parser.add_argument("--sft-input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=".tensornote-runs/dataset")
    parser.add_argument("--chunk-size", type=int, default=512)
    args = parser.parse_args()
    if args.chunk_size < 1:
        parser.error("--chunk-size must be positive")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pretrain_count = write_pretrain(args.pretrain_input, args.output_dir / "pretrain.jsonl", args.chunk_size)
    sft_count = write_sft(args.sft_input, args.output_dir / "sft.jsonl")
    print(json.dumps({"pretrain_records": pretrain_count, "sft_records": sft_count}, ensure_ascii=False))


if __name__ == "__main__":
    main()
