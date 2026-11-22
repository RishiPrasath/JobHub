#!/bin/sh
# Completion of run-001 cells that the 2026-11-10 daily token limit cut off. Same prompts and parameters; only missing cells cost tokens (shared cache).
# usage: run_complete_2026-11-11.sh MODEL
cd "$(dirname "$0")/.."
M=$1
case "$M" in
  qwen*)
    python -u harness/run_suggestions.py --model $M --method M1 --run 1 --max-tokens 700 --tag d2
    python -u harness/run_suggestions.py --model $M --method M3 --run 1 --max-tokens 600 --tag d2
    python -u harness/run_suggestions.py --model $M --method M2 --run 2 --max-tokens 1000 --tag d2 ;;
  openai/gpt-oss-20b)
    python -u harness/run_suggestions.py --model $M --method M2 --run 1 --max-tokens 1000 --tag d2
    python -u harness/run_suggestions.py --model $M --method M1 --run 1 --max-tokens 700 --tag d2
    python -u harness/run_suggestions.py --model $M --method M3 --run 1 --max-tokens 600 --tag d2
    python -u harness/run_suggestions.py --model $M --method M2 --run 2 --max-tokens 1000 --tag d2 ;;
  openai/gpt-oss-120b)
    S=P01-A,P02-A,P04-A,P06-A,P09-B,P03-A,P05-B,P08-B,P07-B,P10-A
    python -u harness/run_suggestions.py --model $M --method M2 --run 1 --max-tokens 1000 --sets $S --tag d2
    python -u harness/run_suggestions.py --model $M --method M1 --run 1 --max-tokens 700 --sets $S --tag d2 ;;
esac
