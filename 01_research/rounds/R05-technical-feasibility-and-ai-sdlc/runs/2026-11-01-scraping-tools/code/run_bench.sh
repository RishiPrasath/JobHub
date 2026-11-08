#!/bin/sh
# usage: run_bench.sh <tool>; installs deps in a throwaway playwright container on the bench network
export MSYS_NO_PATHCONV=1
docker run --rm --network ${BENCH_NET:-code_bench} -v "$(pwd):/work" -w /work/code mcr.microsoft.com/playwright/python:v1.49.0-noble \
  sh -c "pip install -q httpx trafilatura playwright==1.49.0 >/dev/null 2>&1; python bench.py $1"
