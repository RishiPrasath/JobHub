#!/bin/bash
# usage: bash harness/run_set.sh run1   (from the experiment folder). P05 image and code unchanged; only this folder is mounted.
N=$1; E=$(pwd -W 2>/dev/null || pwd)
export MSYS_NO_PATHCONV=1
docker rm -f e11-$N >/dev/null 2>&1
docker create --name e11-$N --env-file ../../.env \
 -e REGISTRY_URL=http://registry:8090 -e OPENSERP_URL=http://openserp:7000 -e FETCH_URL=http://fetch:8080 -e FETCH_TOKEN=local-dev-token -e READER=fetch -e READ_POLICY=conservative \
 --network 03_company-research-pipeline_default -v "$E/data:/in:ro" -v "$E/runs/2026-11-10-run-001/outputs:/outputs" \
 jobhub-company-research-flow:dev cases /in/run_input.json /outputs/$N --workers 2 >/dev/null
docker network connect 09_openserp-company-research_default e11-$N
docker network connect 04_fetch-render-service_default e11-$N
docker start -a e11-$N > runs/2026-11-10-run-001/outputs/$N.console.txt 2>&1
