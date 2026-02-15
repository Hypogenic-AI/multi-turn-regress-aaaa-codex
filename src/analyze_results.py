import json
from pathlib import Path
from typing import Dict, Any

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

from .config import RESULTS_DIR
from .utils import read_jsonl


def load_safety_df() -> pd.DataFrame:
    rows = read_jsonl(RESULTS_DIR / "evaluations" / "safety_scores.jsonl")
    def judge_field(row, key, default=None):
        return row.get("judge", {}).get(key, default)
    data = []
    for r in rows:
        data.append(
            {
                "dataset": r["dataset"],
                "sample_id": r["sample_id"],
                "turn_count": r["turn_count"],
                "heuristic_refusal": bool(r.get("heuristic_refusal")),
                "judge_refusal": bool(judge_field(r, "refusal", False)),
                "judge_compliance": bool(judge_field(r, "compliance", False)),
                "severity": judge_field(r, "severity", "none"),
            }
        )
    return pd.DataFrame(data)


def load_mt_df() -> pd.DataFrame:
    rows = read_jsonl(RESULTS_DIR / "evaluations" / "mt_bench_scores.jsonl")
    data = []
    for r in rows:
        score = r.get("judge", {}).get("score")
        if isinstance(score, str):
            try:
                score = int(score)
            except ValueError:
                score = None
        data.append(
            {
                "question_id": r["question_id"],
                "category": r["category"],
                "turn_index": r["turn_index"],
                "score": score,
            }
        )
    df = pd.DataFrame(data)
    df = df.dropna(subset=["score"])
    df["score"] = df["score"].astype(int)
    return df


def paired_stats(df: pd.DataFrame, dataset: str, turn_a: int, turn_b: int) -> Dict[str, Any]:
    subset = df[df["dataset"] == dataset]
    pivot = subset.pivot_table(index="sample_id", columns="turn_count", values="judge_compliance", aggfunc="mean")
    if turn_a not in pivot.columns or turn_b not in pivot.columns:
        return {"n": 0}
    a = pivot[turn_a].dropna()
    b = pivot[turn_b].dropna()
    common = a.index.intersection(b.index)
    a = a.loc[common]
    b = b.loc[common]
    if len(common) < 10:
        return {"n": len(common)}
    # Normality check
    diff = b - a
    stat, p_normal = stats.shapiro(diff)
    if p_normal > 0.05:
        t_stat, p_val = stats.ttest_rel(b, a)
        test = "paired_t"
    else:
        t_stat, p_val = stats.wilcoxon(b, a)
        test = "wilcoxon"
    effect = (diff.mean() / (diff.std(ddof=1) + 1e-8))
    return {
        "n": len(common),
        "test": test,
        "stat": float(t_stat),
        "p_value": float(p_val),
        "mean_diff": float(diff.mean()),
        "cohens_d": float(effect),
    }


def analyze_safety(df: pd.DataFrame) -> Dict[str, Any]:
    summary = df.groupby(["dataset", "turn_count"])["judge_compliance"].mean().reset_index()
    summary_refusal = df.groupby(["dataset", "turn_count"])["judge_refusal"].mean().reset_index()

    stats_out = {}
    for ds in df["dataset"].unique():
        turns = sorted(df[df["dataset"] == ds]["turn_count"].unique())
        if len(turns) >= 2:
            stats_out[ds] = paired_stats(df, ds, turns[0], turns[-1])
        else:
            stats_out[ds] = {"n": 0}

    # Plot compliance by turn
    plt.figure(figsize=(6, 4))
    sns.lineplot(data=summary, x="turn_count", y="judge_compliance", hue="dataset", marker="o")
    plt.title("Compliance Rate by Turn Count (Safety)")
    plt.ylabel("Compliance Rate")
    plt.xlabel("Turn Count")
    plt.tight_layout()
    out_path = RESULTS_DIR / "plots" / "safety_compliance_by_turn.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150)
    plt.close()

    # Plot refusal by turn
    plt.figure(figsize=(6, 4))
    sns.lineplot(data=summary_refusal, x="turn_count", y="judge_refusal", hue="dataset", marker="o")
    plt.title("Refusal Rate by Turn Count (Safety)")
    plt.ylabel("Refusal Rate")
    plt.xlabel("Turn Count")
    plt.tight_layout()
    out_path2 = RESULTS_DIR / "plots" / "safety_refusal_by_turn.png"
    plt.savefig(out_path2, dpi=150)
    plt.close()

    return {
        "summary": summary.to_dict(orient="records"),
        "summary_refusal": summary_refusal.to_dict(orient="records"),
        "stats": stats_out,
        "plots": [str(out_path), str(out_path2)],
    }


def analyze_mt(df: pd.DataFrame) -> Dict[str, Any]:
    summary = df.groupby(["turn_index"])["score"].mean().reset_index()
    # t-test between first and last turn
    turn_min = df["turn_index"].min()
    turn_max = df["turn_index"].max()
    pivot = df.pivot_table(index="question_id", columns="turn_index", values="score", aggfunc="mean")
    if turn_min in pivot.columns and turn_max in pivot.columns:
        common = pivot[[turn_min, turn_max]].dropna()
        if len(common) >= 10:
            diff = common[turn_max] - common[turn_min]
            stat, p_normal = stats.shapiro(diff)
            if p_normal > 0.05:
                t_stat, p_val = stats.ttest_rel(common[turn_max], common[turn_min])
                test = "paired_t"
            else:
                t_stat, p_val = stats.wilcoxon(common[turn_max], common[turn_min])
                test = "wilcoxon"
            mt_stats = {
                "n": len(common),
                "test": test,
                "stat": float(t_stat),
                "p_value": float(p_val),
                "mean_diff": float(diff.mean()),
            }
        else:
            mt_stats = {"n": len(common)}
    else:
        mt_stats = {"n": 0}

    plt.figure(figsize=(6, 4))
    sns.lineplot(data=summary, x="turn_index", y="score", marker="o")
    plt.title("MT-Bench Success Rate by Turn")
    plt.ylabel("Success Rate")
    plt.xlabel("Turn Index")
    plt.tight_layout()
    out_path = RESULTS_DIR / "plots" / "mt_bench_success_by_turn.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150)
    plt.close()

    return {
        "summary": summary.to_dict(orient="records"),
        "stats": mt_stats,
        "plots": [str(out_path)],
    }


def main() -> None:
    safety_df = load_safety_df()
    mt_df = load_mt_df()

    safety_out = analyze_safety(safety_df)
    mt_out = analyze_mt(mt_df)

    report = {
        "safety": safety_out,
        "mt_bench": mt_out,
    }

    out_path = RESULTS_DIR / "evaluations" / "analysis_summary.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Saved analysis summary to {out_path}")


if __name__ == "__main__":
    main()
