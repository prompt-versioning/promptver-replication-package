# REPRODUCIBILITY

## Level 1 (recommended for reviewers)

Uses cached data only:

```bash
pip install -r requirements.txt
bash scripts/run_all_analysis.sh
```

## Level 2

Recompute intermediate label artifacts from packaged raw outputs by adapting scripts in `scripts/`.

## Level 3 (optional)

API scripts in `scripts/api_runs/` require external credentials and are not needed for paper-table replication.
