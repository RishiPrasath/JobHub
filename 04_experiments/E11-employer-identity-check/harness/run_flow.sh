#!/usr/bin/env bash
# Runs the UNCHANGED P05 image's `cases` command over data/run_input.json. Usage: harness/run_flow.sh <run-label e.g. runA> [workers]
# Mounts only this experiment's folders; P05 files are not touched. The repo-root .env supplies GROQ_* (never printed).
set -e
E="$(cd "$(dirname "$0")/.." && pwd)"; REPO="$(cd "$E/../.." && pwd)"
LABEL="$1"; W="${2:-2}"
WE="$(cygpath -m "$E")"; WREPO="$(cygpath -m "$REPO")"
OUT="$E/runs/2026-11-10-run-001/outputs/$LABEL"; mkdir -p "$OUT"
NAME="e11-$LABEL"; docker rm -f "$NAME" >/dev/null 2>&1 || true
MSYS_NO_PATHCONV=1 docker create --name "$NAME" --init --env-file "$WREPO/.env" \
  -e REGISTRY_URL=http://registry:8090 -e OPENSERP_URL=http://openserp:7000 -e FETCH_URL=http://fetch:8080 -e FETCH_TOKEN=local-dev-token -e READER=fetch -e READ_POLICY=conservative \
  -v "$WE/runs/2026-11-10-run-001/outputs/$LABEL:/outputs" -v "$WE/data/run_input.json:/in/run_input.json:ro" \
  --read-only --tmpfs /tmp --cap-drop ALL --security-opt no-new-privileges:true --memory 512m --pids-limit 128 \
  --network 03_company-research-pipeline_default jobhub-company-research-flow:dev cases /in/run_input.json /outputs --workers "$W" >/dev/null
docker network connect 09_openserp-company-research_default "$NAME"
docker network connect 04_fetch-render-service_default "$NAME"
docker start -a "$NAME" 2>&1 | tee "$OUT/console.log"
docker rm "$NAME" >/dev/null
