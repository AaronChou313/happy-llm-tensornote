"""Dependency-free validation for the chapter 5 project experiment."""

import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED_SCRIPTS = [
    "k_model.py",
    "dataset.py",
    "train_tokenizer.py",
    "ddp_pretrain.py",
    "ddp_sft_full.py",
    "model_sample.py",
    "export_model.py",
]


def main() -> None:
    missing = [name for name in REQUIRED_SCRIPTS if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit(f"Missing chapter files: {missing}")

    parsed = []
    for name in REQUIRED_SCRIPTS:
        ast.parse((ROOT / name).read_text(encoding="utf-8"), filename=name)
        parsed.append(name)

    samples = [json.loads(line) for line in (ROOT / "smoke-data.jsonl").read_text(encoding="utf-8").splitlines()]
    if not samples or any(not isinstance(row.get("text"), str) or not row["text"].strip() for row in samples):
        raise SystemExit("smoke-data.jsonl must contain nonempty text records")

    result = {
        "status": "ok",
        "parsed": parsed,
        "sampleRecords": len(samples),
        "network": False,
        "trainingStarted": False,
    }
    output = ROOT / ".tensornote-runs/chapter5-smoke.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
