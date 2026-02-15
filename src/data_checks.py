import json
from pathlib import Path
from collections import Counter

from datasets import load_from_disk

from .config import DATASETS_DIR, RESULTS_DIR


def summarize_dataset(name: str, ds) -> dict:
    summary = {
        "name": name,
        "num_rows": len(ds),
        "features": list(ds.features.keys()),
        "missing_values": {},
        "duplicates": 0,
        "samples": [],
    }
    # Missing values
    for feat in ds.features.keys():
        missing = sum(1 for x in ds[feat] if x is None)
        summary["missing_values"][feat] = missing
    # Duplicates (naive on string fields)
    if "prompt" in ds.features:
        values = ds["prompt"]
    elif "Goal" in ds.features:
        values = ds["Goal"]
    elif "turns" in ds.features:
        values = ["|".join(x) for x in ds["turns"]]
    else:
        values = []
    if values:
        counts = Counter(values)
        summary["duplicates"] = sum(1 for v in counts.values() if v > 1)
    # Samples
    for i in range(min(3, len(ds))):
        summary["samples"].append(ds[i])
    return summary


def main() -> None:
    jbb = load_from_disk(DATASETS_DIR / "jbb_behaviors")
    mt = load_from_disk(DATASETS_DIR / "mt_bench")
    wj = load_from_disk(DATASETS_DIR / "wildjailbreak")

    summaries = {
        "jbb_harmful": summarize_dataset("jbb_harmful", jbb["harmful"]),
        "jbb_benign": summarize_dataset("jbb_benign", jbb["benign"]),
        "mt_bench": summarize_dataset("mt_bench", mt["train"]),
        "wildjailbreak": summarize_dataset("wildjailbreak", wj["train"]),
    }

    out_path = RESULTS_DIR / "data_summary.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2)
    print(f"Saved data summary to {out_path}")


if __name__ == "__main__":
    main()
