#!/bin/sh
# usage: run_rest.sh MODEL  -- finishes M2, then M3 and M1 on a priority subset (10 sets), then the rest
cd "$(dirname "$0")/.."
MODEL=$1
S1=P01-A,P02-A,P04-A,P06-A,P09-B,P03-A,P05-B,P08-B,P07-B,P10-A
S2=P01-B,P02-B,P03-B,P04-B,P05-A,P06-B,P07-A,P08-A,P09-A,P10-B
python -u harness/run_suggestions.py --model $MODEL --method M2 --run 1 --max-tokens 1000
python -u harness/run_suggestions.py --model $MODEL --method M3 --run 1 --max-tokens 600 --sets $S1 --tag s1
python -u harness/run_suggestions.py --model $MODEL --method M1 --run 1 --max-tokens 700 --sets $S1 --tag s1
python -u harness/run_suggestions.py --model $MODEL --method M3 --run 1 --max-tokens 600 --sets $S2 --tag s2
python -u harness/run_suggestions.py --model $MODEL --method M1 --run 1 --max-tokens 700 --sets $S2 --tag s2
