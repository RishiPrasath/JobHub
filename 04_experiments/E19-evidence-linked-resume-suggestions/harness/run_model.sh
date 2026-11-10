#!/bin/sh
# usage: run_model.sh <model> <run> <methods...>   (retries a method until its result file exists; the cache makes reruns free)
cd "$(dirname "$0")/.."
model="$1"; run="$2"; shift; shift
safe=$(echo "$model" | tr '/' '-')
for m in "$@"; do
  i=0
  until [ -f "runs/2026-11-10-run-001/outputs/results/${safe}__${m}__run${run}.json" ] || [ $i -ge 6 ]; do
    python -u harness/run_suggestions.py --model "$model" --method "$m" --run "$run" --max-tokens 1000
    i=$((i+1))
  done
done
