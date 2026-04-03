## Start the Application

**docker compose up -d**

## Access the Application

**http://localhost:8080/api**

## Request Flow

```
        Browser
           |
           V
      localhost:8080
           |
           V
    NGINX container
           |
           V
    Backend containers
```

## Run the request multiple times to observe load balancing or Just run this.

```
for i in {1..10}; do curl http://localhost:8080/api; echo; done
```

## Scale Backend Containers

```
docker compose up -d --scale backend=2
```
