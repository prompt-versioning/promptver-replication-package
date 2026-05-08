#!/usr/bin/env bash
set -euo pipefail
python scripts/00_check_environment.py
python scripts/09_generate_tables.py
echo "Replication analysis completed."
