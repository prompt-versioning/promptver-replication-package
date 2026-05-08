# PROMPTVER Replication Package

This package supports the paper:  
"PROMPTVER: Semantic Versioning for Prompt Edits"

## What this package contains

- Controlled prompt-edit benchmark.
- Prompt edit catalog.
- Operator taxonomy.
- Raw executor outputs.
- Paraphrastic noise-floor data.
- Stable witness sets.
- Empirical reference labels.
- PROMPTVER predictions.
- Simple-LLM baseline predictions.
- Scripts to regenerate Tables II and III.

## Main claims supported

C1. PROMPTVER reaches 0.718 exact agreement with the empirical reference labels.  
C2. PROMPTVER reduces dangerous misses compared with always-PATCH.  
C3. The simple LLM baseline is competitive, especially on XSum.  
C4. PROMPTVER provides auditable decision traces.

## Reproducing the paper results

The main results can be reproduced without calling external LLM APIs because the raw executor outputs and judge predictions used in the paper are included.

To reproduce the tables:

```bash
pip install -r requirements.txt
bash scripts/run_all_analysis.sh
```

Expected outputs:

- `results/tables/table2_controlled_benchmark_results.csv`
- `results/tables/table3_baseline_comparison.csv`
- summary printed to terminal
