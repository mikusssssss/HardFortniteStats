FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -e .

# create data directory
RUN mkdir -p /data

# variablles + prefix
CMD redbot-setup --instance-name "$BOT_INSTANCE_NAME" --data-path /data --backend JSON --token "$BOT_TOKEN" --prefix "$BOT_PREFIX" --no-prompt && redbot "$BOT_INSTANCE_NAME" --no-prompt --token "$BOT_TOKEN" --prefix "$BOT_PREFIX"
