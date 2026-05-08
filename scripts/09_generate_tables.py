from __future__ import annotations
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
labels = ROOT / "data" / "labels"
results = ROOT / "results" / "tables"
results.mkdir(parents=True, exist_ok=True)

emp = pd.read_csv(labels / "empirical_labels_hard_violation_aware.csv")
pv = pd.read_csv(labels / "promptver_predictions.csv")
sl = pd.read_csv(labels / "simple_llm_predictions.csv")
ap = pd.read_csv(labels / "always_patch_predictions.csv")

base = emp[["edit_id", "dataset", "executor", "empirical_label"]].drop_duplicates()
pv_m = base.merge(pv[["edit_id", "dataset", "executor", "majority_label"]], on=["edit_id", "dataset", "executor"], how="left")
sl_m = base.merge(sl[["edit_id", "dataset", "executor", "majority_label"]], on=["edit_id", "dataset", "executor"], how="left")
ap_m = base.merge(ap[["edit_id", "dataset", "executor", "predicted_label"]], on=["edit_id", "dataset", "executor"], how="left")

def score(df: pd.DataFrame, col: str, method: str) -> pd.DataFrame:
    d = df.copy()
    d["correct"] = d[col].astype(str).str.upper() == d["empirical_label"].astype(str).str.upper()
    g = d.groupby("dataset", dropna=False)["correct"].mean().reset_index()
    g["method"] = method
    g = g.rename(columns={"correct": "accuracy_exact"})
    return g[["method", "dataset", "accuracy_exact"]]

t2 = pd.concat(
    [
        score(pv_m, "majority_label", "PROMPTVER"),
        score(sl_m, "majority_label", "simple_llm"),
        score(ap_m, "predicted_label", "always_patch"),
    ],
    ignore_index=True,
)
t2.to_csv(results / "table2_controlled_benchmark_results.csv", index=False)

t3 = t2.pivot(index="dataset", columns="method", values="accuracy_exact").reset_index()
t3.to_csv(results / "table3_baseline_comparison.csv", index=False)

trace = pv_m[["edit_id", "dataset", "executor", "empirical_label", "majority_label"]].head(50)
trace.to_csv(results / "table4_trace_cases.csv", index=False)
print("Wrote:", results / "table2_controlled_benchmark_results.csv")
print("Wrote:", results / "table3_baseline_comparison.csv")
