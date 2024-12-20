# FastAPI App Template

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Tests](https://github.com/peplxx/fast-template/actions/workflows/main.yaml/badge.svg)](https://github.com/peplxx/fast-template/actions/workflows/main.yaml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791.svg?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C.svg?style=flat&logo=prometheus&logoColor=white)](https://prometheus.io)
[![Grafana](https://img.shields.io/badge/Grafana-F46800.svg?style=flat&logo=grafana&logoColor=white)](https://grafana.com)
[![Docker](https://img.shields.io/badge/Docker-0096ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com)
[![Nginx](https://img.shields.io/badge/Nginx-009639.svg?style=flat&logo=nginx&logoColor=white)](https://nginx.org)

A production-ready FastAPI template with comprehensive integrations for modern web development.

## Overview

This template provides a solid foundation for building production-ready web services with FastAPI. It combines modern tools and best practices to help you get started quickly:

- **Core Stack**: FastAPI + PostgreSQL + SQLAlchemy
- **Deployment**: Docker + Nginx + Certs configuration ready to go
- **Monitoring**: Prometheus metrics and Grafana dashboards
- **Development**: Poetry for dependencies, Ruff for linting, pytest for testing
- **CI/CD**: GitHub Actions workflow included
- **Tooling**: Custom module system to automate routine tasks
- **Pre-configured**: App-logging, api-limiter, openapi-specification, metrics and CORS middlewares, etc.
- **Testing**: Container-free testing system

Everything is pre-configured and tested to work together. Just clone, customize, and start building your application.

---
## Quick Start
### Sections
1. [Requirements](#requirements)
2. [How to navigate](#how-to-navigate-in-project)
3. [How to run](#how-to-run-app)
4. [How to develop](#how-to-develop)
5. [How to use dev tools](#how-to-use-dev-tools)


---
### Requirements

You'll need these tools installed:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/)

>**Quick Install:** run `./deploy/dependencies.sh` to install requirements
---
### How to navigate in project

Use `make help` to see all available commands:

```bash
make help
```
---
### How to run app

#### 1. Setup `.env` file
```bash
make env # Creates .env from .env.example
```

> **Note:** View supported env-variables in `backend/app/config/default.py`

> **Note:** `env.example` contains minimal required variables

#### 2. Run app
Choose your configuration:

- `run-local` - Local development: `backend[local] + database[docker]`
- `run-dev1` - Basic deployment: `nginx[http] + backend + database`
- `run-dev2` - Full development: `nginx[http] + backend + database + grafana + prometheus`
- `run-prod` - Production: `nginx[https + http] + backend + database + grafana + prometheus + pgbackups`

```bash
make <target-config>
```
> **Local setup:** starts database, setup poetry and make migrations besides runing app itself.

> **Production:** Also there is script to run prod setup as linux-unit: `/deploy/deploy-service.sh`.
---
#### 3. Avaliability
Assume, that you run app on localhost:
 - **Backend/Swagger** : `localhost/swagger`
 - **Backend/Scalar** : `localhost/scalar`
 - **Graphana** :  `localhost:3333`, admin/admin
---
### How to develop

#### 1. Setup poetry environment
```bash
make poetry  # Installs all dependency groups (test, dev)
```

#### 2. Pre-commit hooks
```bash
pre-commit install
```
> **Note**: ruff formatting works only for `/backend` dir

**Now you're ready to develop!**

---

### How to use dev tools

#### Project Architecture & Tools

This project is built using [layered architecture](https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch01.html) pattern, which provides clear separation of concerns and maintainable codebase.

To accelerate development process, I provide automated tools located in `/backend/.utils/` directory.


#### Tools list:

#### 1. Module Generator
Generate a new module:
```bash
make module name=<module-name>
```

The generator will:
1. Create module structure in `backend/app/src/modules/{module-name}`
2. Setup testsuite in `backend/tests/testsuites/{module-name}`
3. Add necessary base classes and metadata

> **Note:** Import your new module in `backend/app/src/modules/__init__.py`
---
