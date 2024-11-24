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
- **Testing**: Tests system written in way it doesn't require app to be running.

Everything is pre-configured and tested to work together. Just clone, customize, and start building your application.

## Quick Start

### Sections
1. [Requirements](#requirements)
2. [How to navigate](#how-to-navigate-in-project)
3. [How to run](#how-to-run-app)
4. [How to develop](#how-to-develop)
5. [How to use dev tools](#how-to-use-dev-tools)

### Requirements

You'll need these tools installed to enable all features of this project:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/)

### How to navigate in project

This project uses Makefile to run commands. You can use `make help` to see all supported commands.

```bash
make help
```

<details>
<summary>Command output</summary>

```bash
Usage: make [target] ...

Usage:
  make <target>

Targets:
Database:
  psql                 Connect to database via psql
  run-db               Run database container [docker-compose.yaml]
  migrate              Apply migrations
  revision             Create new revision

Environment:
  env                  Create .env file from .env.example

Generators:
  gen-ssl              SSL key and certificate to ./certs directory
  gen-hex32            Generate random hex string of 32 characters
  module               Generate a new module with the given name, description (eg. make module name=users description="Users management module")

Help:
  help                 Show this help

Run:
  run-local            Run app in local mode (backend(local) + database(docker))                         [docker-compose.yaml]
  run-dev1             Run app in dev1 mode  (nginx(http) + backend + database)                          [docker-compose.yaml]
  run-dev2             Run app in dev2 mode  (nginx(http) + backend + database + graphana + prometheus)  [docker-compose.yaml]
  run-prod             Run app in prod mode  (nginx(https) + backend + database + graphana + prometheus) [docker-compose-prod.yaml]

Tests:
  test                 Run tests
```

</details>

### How to run app

#### 1. Setup `.env` file
Firstly you need to setup `.env` file. You can do this by running `make env` command.

```bash
make env # Creating .env file from .env.example
```

> **Note:** You can see all supported env-variables in settings: `backend/app/config/default.py`

> **Note:** `env.example` has minimal-required variables to run app properly.


#### 2. Run app
This template has four configurations for running the app:

- `run-local` - run app locally `backend[local] + database[docker]`
- `run-dev1` - run app in dev1 mode `nginx[http] + backend + database`
- `run-dev2` - run app in dev2 mode `nginx[http] + backend + database + grafana + prometheus`
- `run-prod` - run app in prod mode `nginx[https + http] + backend + database + grafana + prometheus + pgbackups`

```bash
make <target-config>
```
> **Note:** Before running the app `locally`, you need to setup poetry environment by running `make poetry` command.

**Congratulations! You've set up and run the app.**


### How to develop

#### 1. Setup poetry environment
This project uses [Poetry](https://python-poetry.org/) to manage dependencies and has `test` group for running tests and `dev` group for development.
To install all groups of dependencies run `make poetry` command.
```bash
make poetry
```

#### 2. Pre-commit hooks
Also to make commits you need to setup pre-commit hooks by running `pre-commit install` command.
```bash
pre-commit install
```

**Now you are ready to develop!**

> **Note:** To automate your dev life see [How to use dev tools](#how-to-use-dev-tools) section.

### How to use dev tools

#### Overview
So, in this project I try to automate routine tasks to save your time for more important things.

This project project has [layered-modular architecture](https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch01.html), so if you want to follow this pipeline you can easily generate new templates using predefined tools.

<details>
<summary>Custom module system description</summary>
Modules in this project use base classes to automatically resolve module metadata like TESTSUITES, ROUTERS, TAGS and EXPORTS, as well as provide a brief description of each module's functionality.

</details>

**Tools sources location:** `/backend/.utils/`

#### Tools list:
<details>
<summary>1. Generating new module</summary>

#### 1. Generate new module
To generate new module you can use `make module` command. 

This command will generate new module with the given name and description, also it will setup a testsuite for this module in `backend/tests/testsuites/{module-name}` directory.

```bash
make module name=<module-name> description=<module-description>
```
> **Note:** Also you can use `module` target with only name argument to generate module.
>```bash
>make module name=<module-name>
>```
> But in this case program will ask you to enter description interactively.

Also tool checks for existing module with the same name and will not allow to override it without your confirmation. 
> **Note:** Empty named modules are not allowed!

You can check Mako templates in `backend/.utils/templates/module` directory.

#### 2. Import module

After you need to import module in `backend/app/src/modules/__init__.py` file manually.
> **Note:** Not imported modules will not be loaded, same thing with tests (testsuites will be imported with module automatically)!

#### 3. Ready to go!

Now you can start developing your module in `backend/app/src/modules/{module-name}` directory.

And tests in `backend/tests/testsuites/{module-name}` directory.

</details>
