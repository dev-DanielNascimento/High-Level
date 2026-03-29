FROM python:3.12-slim
RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY requisitos.txt .

RUN pip install --no-cache-dir -r requisitos.txt