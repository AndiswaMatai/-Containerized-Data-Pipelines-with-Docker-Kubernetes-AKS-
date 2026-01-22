FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pipelines/ pipelines/

CMD ["python", "pipelines/etl_job.py"]


Why This Matters

Ensures the same runtime across all environments

Makes pipelines portable and CI/CD-ready

Simplifies dependency management
