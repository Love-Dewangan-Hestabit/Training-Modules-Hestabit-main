#!/bin/bash
set -e

echo "Deploying Inventory App..."

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d

echo "Deployment complete"
