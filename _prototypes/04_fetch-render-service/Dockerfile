FROM mcr.microsoft.com/playwright/python:v1.49.0-noble

ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 HOME=/tmp
RUN pip install fastapi "uvicorn[standard]" httpx trafilatura playwright==1.49.0
WORKDIR /srv
COPY app /srv/app
USER pwuser
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
