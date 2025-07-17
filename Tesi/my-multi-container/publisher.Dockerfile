FROM python:3.11

WORKDIR /scripts

COPY scripts/requirements.txt .
COPY scripts/publisher.py .

RUN pip install --no-cache-dir -r requirements.txt