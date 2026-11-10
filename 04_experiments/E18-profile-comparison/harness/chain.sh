#!/bin/bash
cd /c/Users/prasa/Documents/Github/JobHub
L=04_experiments/E18-profile-comparison/runs/2026-11-10-run-001/logs
until grep -q "STAGE-COMPLETE extract 1" $L/extract_run1.log 2>/dev/null; do sleep 10; done
bash 04_experiments/E18-profile-comparison/harness/supervise.sh evid 1 &
bash 04_experiments/E18-profile-comparison/harness/supervise.sh extract 2 &
until grep -q "STAGE-COMPLETE free 1" $L/free_run1.log 2>/dev/null; do sleep 10; done
bash 04_experiments/E18-profile-comparison/harness/supervise.sh free 2
wait
