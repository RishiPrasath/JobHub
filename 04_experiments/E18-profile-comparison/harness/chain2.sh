#!/bin/bash
cd /c/Users/prasa/Documents/Github/JobHub
R=04_experiments/E18-profile-comparison/runs/2026-11-10-run-001
until [ $(ls $R/outputs/raw/extract | grep -v "__.*run2" | wc -l) -ge 16 ]; do sleep 10; done
sleep 20
python 04_experiments/E18-profile-comparison/harness/run_methods.py evid 1 >> $R/logs/evid_run1.log 2>&1 &
python 04_experiments/E18-profile-comparison/harness/run_methods.py extract 2 >> $R/logs/extract_run2.log 2>&1 &
wait
echo CHAIN2-DONE >> $R/logs/evid_run1.log
