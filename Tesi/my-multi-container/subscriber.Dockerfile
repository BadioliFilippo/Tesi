FROM python:3.11

WORKDIR /scripts

COPY scripts/requirements.txt .
COPY scripts/subscriber.py .
COPY scripts/exporter.py .

RUN pip install --no-cache-dir -r requirements.txt