#!/bin/bash
# Reruns a stage until it exits cleanly (all calls are cached, so reruns only do the missing calls).
cd /c/Users/prasa/Documents/Github/JobHub
stage="$1"; run="${2:-1}"; extra="$3"
log=04_experiments/E18-profile-comparison/runs/2026-11-10-run-001/logs/${stage}_run${run}.log
for i in $(seq 1 30); do
  python 04_experiments/E18-profile-comparison/harness/run_methods.py "$stage" "$run" $extra >> "$log" 2>&1 && { echo "STAGE-COMPLETE $stage $run" >> "$log"; exit 0; }
  sleep 5
done
echo "STAGE-FAILED $stage $run" >> "$log"
