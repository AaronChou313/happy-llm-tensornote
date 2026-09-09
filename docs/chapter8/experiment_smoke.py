"""Offline structural and numerical checks for chapter 8."""
import ast
import json
import math
from pathlib import Path


def group_advantages(rewards):
    mean = sum(rewards) / len(rewards)
    variance = sum((reward - mean) ** 2 for reward in rewards) / len(rewards)
    scale = math.sqrt(variance) or 1.0
    return [(reward - mean) / scale for reward in rewards]


def main():
    root = Path(__file__).resolve().parent
    scripts = sorted(
        path for folder in ("grpo", "opd", "search-r1", "retool")
        for path in (root / folder).glob("*.py")
    )
    for path in scripts:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path.relative_to(root)))
    rewards = [1.0, 0.0, 1.0, 0.0]
    advantages = group_advantages(rewards)
    if abs(sum(advantages)) > 1e-9:
        raise SystemExit("GRPO advantage normalization failed")
    report = {
        "status": "ok",
        "scripts_checked": [str(path.relative_to(root)) for path in scripts],
        "reward_example": rewards,
        "normalized_advantages": advantages,
        "network": False,
        "training_started": False,
        "generated_code_executed": False,
    }
    output = root / ".tensornote-runs/chapter8-smoke.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
