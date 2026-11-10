#!/bin/sh
# retries run_llm.py until its results file exists (cache makes retries free); needed because the shared lock can raise PermissionError on Windows
M=$1; R=$2; LAB=$3
for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
  [ -f ../runs/2026-11-10-run-001/outputs/results_$LAB.json ] && break
  python run_llm.py --model $M --run $R --label $LAB >> ../runs/2026-11-10-run-001/outputs/log_$LAB.txt 2>&1
done
