## Build Docker Image

Go to the project directory and run:

**docker build -t node-docker-app .**

```
| Command         | Meaning        |
| --------------- | -------------- |
| docker build    | builds image   |
| -t              | tag name       |
| node-docker-app | image name     |
| .               | current folder |
```

## Run Container

**docker run -p 3000:3000 node-docker-app**

```
Host Port → Container Port
3000      → 3000
```

## Test in Browser

```
Open:

http://localhost:3000

Output:

Hestabit Welcomes You.
```

## Run Container in Background

**docker run -d -p 3000:3000 --name node-container node-docker-app**

## Enter container to run commands

**docker exec -it <container> /bin/sh**

## Explore Linux Commands

Inside container run:

```
Check files
ls

Check running processes
ps

Monitor CPU
top

Check disk usage
df -h

Check folder size
du -h
```

## Container Logs

**docker logs <container>**
