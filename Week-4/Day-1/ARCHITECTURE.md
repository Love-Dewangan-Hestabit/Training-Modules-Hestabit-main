## Week 4 (Day 1) - NODE and PROJECT ARCHITECTURE

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

In this task I created a basic Node.js project structure using Express.
The main goal was to understand how a project starts and how different parts
like config, database, routes and logging are loaded step by step.

## Folder Structure

The project follows a layered folder structure:

```text
src/

- config
- loaders
- routes
- models
- controllers
- services
- repositories
- middlewares
- utils
- jobs
- logs
```

## App Loader

The app loader is responsible for starting the application.

App Loader:

1. Load middlewares
2. Connect Databases
3. Load Routes
4. Start HTTP Server

So App Loader basically Bootstraps the app step by step.

## Config Loader

Here the configuration is managed using environment variables.

Here I have used:

- .env.local
- .env.dev
- .env.prod

## Database Loader

Here I have implemented Database connection logic which I have kept in separate loader.

## Logging

Logging is implemented using Winston.

Logs are here used to show when middleware are loaded, when database is connected, when routes are mounted, when server is started.

## Routes

Here I have added a simple health route to check if server is running.

## Node.js

Node.js runs on a single thread and uses an event loop.
The event loop helps in handling async operations.

I also understood that Node.js uses clustering to use multiple CPU cores for basically improving throughout, resillience and scalability.

## Learnings and Outcomes

This task helped me in understanding:

- The project structure required for managing Backend.
- Backend Application Workflow
- Environment based configuration
- Basic logging
- The importance of separation of responsibilities
