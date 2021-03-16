# django-react-scaffold

Yet another scaffolding to create a React app powered by Django backend.

Heavily opinionated from my personal experience. Personally used by me.

This should save some time to organize the project folders, add some popular libraries in Django/React, and create docker-compose environment including Dockerfile organizations.

You can add a new folder in the root repository to create a new downstream service or client app.

This does not include any devops or infra code and only provide a local environment to work with. However, the local runtime should reflect cloud-environment nature.

## Philosophy

### Monolith backend app
There is nothing like Django to get up to speed for initial product development. No need to waste precious time resources in authentication logic, data modeling/migrations, excessive declarative properties to enable a feature, and balancing code consumption in reading/writing. It's a perfect web framework to start a monolith backend service then start decomposing to microservices.

I am a firm believer that no monolith app will disappear once the microservice paradigm is adopted. Instagram still use Django even this day for auth, internationalization, sessions, and many other Django features while there exists many downstream services and infra services powering Instagram.

Airbnb still has a Ruby On Rail codebase with lots of Java microservice apps intertwined to each other. Reddit is still bound by their "r2" monolith backend app while expanding its horizon to many services.

To follow their paths, I set my foot ground here and such.

### SPA frontend app
React is now a lingua franca in web client application. I admit there are still needs for traditional/server-rendered HTML templates today. However, the majority of web app platforms I have seen so far, harnesses the power of Single Page Application. A richer UI/UX demonstration, modern tooling, and an unbeaten popularity in the frontend community are the reason for React.

### Reverse Proxy
When it comes to developing a web application locally, I decided to throw away localhost domain usage. There are times when localhost domain becomes a blocker: OAuth integration, CORS, subdomain service routing, etc. For this project template, I am fully embracing subdomain request routing via nginx locally with `example.com` safe domain.

You'll see nginx configuration file in `ENV` folder name from `nginx` folder. If I were to add cloud deployment efforts, I would create a new folder for new environment in order to set a new nginx configuration set.

### Data stores
PostgreSQL and Redis are my favorites: Super-performant and easy-to-use. Django now supports table partitioning in PostgreSQL 11+ via third-party library support. You can simulate what Instagram went through for horizontal scaling. Redis can power celery, caching, and cluster-scaling support.

### Provisioning
I generally agree with 12-factor security. I have `envs` folder for dotenv files and their examples.

### Backend Services

Django settings can enable S3 and/or Sendgrid services if configured properly via dotenv.

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
- Key-value memory store
    - Redis 6.0.10

Docker images are alpine-based. Django does have ASGI file ready for async application.

## Getting Started
1. Include following domains to localhost in `/etc/hosts` file
    - app.example.com
    - api.example.com
1. You need Docker and docker-compose binaries first.
1. Copy this scaffold project to a new folder.
1. Rename all of `myapp` and `my_app` references and folders in this project. Don't forget to update meta tag for description in `web_frontend/public/index.html`

In the `envs` folder, you'll see example env files:
- `web_backend.env.example`
- `web_frontend.env.example`

Copy each example env file to `.env` notation there and adjust file variables

```
cp web_backend.env.example web_backend.env
cp web_frontend.env.example web_frontend.env
```

Examine Django settings, Graphene schema and custom User model to update to your needs.

## Running the app environment
Once docker-compose is running, access `http://app.example.com:9000` for web frontend and `http://api.example.com:9000` for web backend.

Make sure to use http instead of https as the browser may perform autocomplete for you.

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