# django-react-scaffold

Yet another scaffolding to create a React app powered by Django backend.

Heavily opinionated from my personal experience. Personally used by me.

This should save some time to organize the project folders, add some popular libraries in Django/React, and create docker-compose environment including Dockerfile organizations.

You can add a new folder in the root repository to create a new internal service or client app.

This does not include any devops or infra code and only provide a local environment to work with. However, the local runtime should reflect cloud-environment nature.

## Prerequisites
- Docker & docker-compose

## High-level App Architecture
- Backend
    - Django 3.1.4/Python 3.9.1/Gunicorn 20.0.4/Graphene 2.15.0
- Frontend
    - React 17.0.1/TypeScript 4.1.3/React Relay 5.0.0
- App DB
    - PostgreSQL 13.1
- Proxy
    - Nginx 1.17
  
Docker images are alpine-based. Django does have ASGI file ready for async application.

## Getting Started
1. You need Docker and docker-compose binaries first.

2. Copy this scaffold project to a new folder.

3. Rename all of `myapp` references and folders in this project. Don't forget to update meta tag for description in `app_frontend/public/index.html`

In the `envs` folder, you'll see example env files:
- `app_backend.env.example`
- `app_frontend.env.example`

Copy each example env file to `.env` notation there and adjust file variables

```
cp app_backend.env.example app_backend.env
cp app_frontend.env.example app_frontend.env
```

Examine Django settings, Graphene schema and custom User model to update to your needs.

Run docker-compose
```
docker-compose up OR docker-compose up --build
```

To stop the environment
```
docker-compose stop
```

To destory the environment
```
docker-compose down
```