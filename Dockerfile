FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -e .

# create data directory
RUN mkdir -p /data

# variablles + prefix
CMD redbot-setup --instance-name "$BOT_INSTANCE_NAME" --data-path /data --backend json --no-prompt --overwrite-existing-instance && redbot "$BOT_INSTANCE_NAME" --no-prompt --token "$BOT_TOKEN" --prefix "$BOT_PREFIX" --owner "$BOT_OWNER_ID" --co-owner "$BOT_COOWNER_ID"
