# Registry-first company research flow. Python standard library only; nothing to pip install.
FROM python:3.12-slim

RUN useradd --create-home --uid 10001 app
WORKDIR /app
COPY flow/ /app/flow/
COPY tests/ /app/tests/
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
USER app
EXPOSE 8100
ENTRYPOINT ["python", "-m", "flow.cli"]
CMD ["serve"]
