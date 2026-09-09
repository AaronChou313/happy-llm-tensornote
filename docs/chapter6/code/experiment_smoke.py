"""Bounded, dependency-free check of the chapter 6 project layout."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
required = ["pretrain.py", "finetune.py", "ds_config_zero2.json"]
missing = [name for name in required if not (root / name).is_file()]
if missing:
    raise SystemExit(f"Missing chapter files: {missing}")
result = {"status": "ok", "checked": required, "network": False, "training_started": False}
out = root / ".tensornote-runs/chapter6-smoke.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
