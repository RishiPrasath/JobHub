# JobHub company-research pipeline. Python standard library only; no pip install step.
FROM python:3.12-slim

RUN useradd --create-home --uid 10001 app
WORKDIR /app
COPY pipeline/ /app/pipeline/

# ACRA CSVs and the SQLite index live on a mounted volume, not in the image.
ENV JOBHUB_DATA=/data PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
RUN mkdir /data && chown app /data
USER app
VOLUME ["/data"]

ENTRYPOINT ["python", "-m", "pipeline.cli"]
CMD ["--help"]
