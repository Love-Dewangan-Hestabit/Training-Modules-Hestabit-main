# Week 5 (Day 5) - CI-Style Deployment Automation and Capstone

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To deploy a fullstack app in Docker with reverse proxy and HTTPS.

## Task Outcome

![Fullstack App](./screenshots/Inventory_App.gif)

## Production Guide - Inventory App

This document explains how to run, deploy, and maintain the Inventory full‑stack application in production.

## 1. Architecture Overview

Frontend (React + Vite)
-> Nginx (Reverse Proxy)
-> Backend (Node.js + Express)
-> MongoDB (Docker Volume)

All services are containerized using Docker and orchestrated with Docker Compose.

## 2. Requirements

- Docker (v20+)
- Docker Compose v2
- Linux / macOS / WSL recommended
- Ports required:
  - 80 (HTTP)
  - 443 (HTTPS – optional)
  - 27018 (MongoDB – local debugging only)

## 3. Environment Variables

Create a `.env` file in the project root (do NOT commit this file):

```
NODE_ENV=production
PORT=5000
MONGO_URI=mongodb://mongo:27017/inventory
```

Add `.env` to `.gitignore`.

## 4. Docker Services

### MongoDB

- Uses official `mongo:6` image
- Data persisted using Docker volume
- Healthcheck enabled
- Restart policy enabled

### Backend

- Node.js + Express
- Waits for MongoDB healthcheck
- Exposes `/health` endpoint

### Frontend

- React app built using Vite
- Served as static files via Nginx

### Nginx

- Reverse proxy
- Routes:
  - `/` -> Frontend
  - `/api` -> Backend
  - `/health` -> Backend health endpoint

## 5. Running in Production

From project root:

```
./deploy.sh
```

This script:

1. Stops existing containers
2. Builds images
3. Starts containers in detached mode

## 6. Health Checks

- MongoDB: verifies `mongod` binary
- Backend: checks `/health` endpoint

Verify status:

```
docker ps
```

Healthy containers show `healthy` status.

## 7. Log Rotation

Docker daemon is configured with log rotation:

- Max size: 10MB
- Max files: 3

Configuration location:

```
/etc/docker/daemon.json
```

## 8. MongoDB Access (Debug Only)

MongoDB is exposed on host port `27018` for debugging.

Connection string for MongoDB Compass:

```
mongodb://localhost:27018
```

In real production, this port should be removed.

## 9. Updating the Frontend

After UI or CSS changes:

```
docker compose build --no-cache frontend
docker compose up -d
```

Browser hard refresh required.

## 10. Stopping the Application

```
docker compose down
```

To remove data (destructive):

```
docker compose down -v
```

## 11. Security Notes

- Secrets are stored in `.env`
- MongoDB not publicly exposed
- Reverse proxy controls traffic
- HTTPS can be added via Certbot
