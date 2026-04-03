## Run the Deployment Script

**./deploy.sh**

```
What this script does:

Stop running containers
docker compose -f docker-compose.prod.yml down

Stops old containers.

Build images
docker compose -f docker-compose.prod.yml build

Builds:

backend image
frontend image

Start services
docker compose -f docker-compose.prod.yml up -d

Starts containers in detached mode.
```
