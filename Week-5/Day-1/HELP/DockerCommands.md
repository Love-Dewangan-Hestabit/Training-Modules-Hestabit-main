# Docker Useful Commands (Quick Reference)

This README contains commonly used Docker commands for building,
running, managing containers, images, and debugging.

------------------------------------------------------------------------

## 1. Docker Version & Info

    docker --version
    docker version
    docker info

------------------------------------------------------------------------

## 2. Docker Images

### List Images

    docker images

### Pull Image

    docker pull <image_name>

Example:

    docker pull nginx

### Remove Image

    docker rmi <image_id>

### Remove All Images

    docker rmi $(docker images -q)

------------------------------------------------------------------------

## 3. Docker Containers

### List Running Containers

    docker ps

### List All Containers

    docker ps -a

### Run Container

    docker run <image_name>

Example:

    docker run nginx

### Run Container in Detached Mode

    docker run -d <image_name>

### Run Container with Name

    docker run -d --name mycontainer nginx

### Run Container with Port Mapping

    docker run -p 3000:3000 <image_name>

------------------------------------------------------------------------

## 4. Container Management

### Start Container

    docker start <container_id>

### Stop Container

    docker stop <container_id>

### Restart Container

    docker restart <container_id>

### Remove Container

    docker rm <container_id>

### Remove All Containers

    docker rm $(docker ps -aq)

------------------------------------------------------------------------

## 5. Logs & Debugging

### View Logs

    docker logs <container_id>

### Follow Logs

    docker logs -f <container_id>

### Execute Command Inside Container

    docker exec -it <container_id> bash

------------------------------------------------------------------------

## 6. Building Images

### Build Image

    docker build -t <image_name> .

Example:

    docker build -t myapp .

### Build with Tag

    docker build -t myapp:v1 .

------------------------------------------------------------------------

## 7. Docker Volumes

### List Volumes

    docker volume ls

### Create Volume

    docker volume create <volume_name>

### Remove Volume

    docker volume rm <volume_name>

------------------------------------------------------------------------

## 8. Docker Networks

### List Networks

    docker network ls

### Create Network

    docker network create <network_name>

### Connect Container to Network

    docker network connect <network_name> <container>

------------------------------------------------------------------------

## 9. Cleanup

### Remove Stopped Containers

    docker container prune

### Remove Unused Images

    docker image prune

### Remove Everything

    docker system prune -a

------------------------------------------------------------------------

## 10. Docker Compose

### Start Services

    docker-compose up

### Run in Background

    docker-compose up -d

### Stop Services

    docker-compose down

### Rebuild Containers

    docker-compose up --build

------------------------------------------------------------------------

## Quick Tip

See all commands:

    docker --help
