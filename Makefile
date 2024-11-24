ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif

BLUE := \033[34m
GREEN := \033[32m
YELLOW := \033[33m
RESET := \033[0m

HELP_FUN = \
    %help; \
    printf "\n${BLUE}Usage:${RESET}\n  make ${YELLOW}<target>${RESET}\n\n"; \
    while(<>) { \
        if(/^([a-zA-Z0-9_-]+):.*\#\#(?:@([a-zA-Z0-9_-]+))?\s(.*)$$/) { \
            push(@{$$help{$$2 // 'Other'}}, [$$1, $$3]); \
        } \
    }; \
    printf "${BLUE}Targets:${RESET}\n"; \
    for (sort keys %help) { \
        printf "${GREEN}%s:${RESET}\n", $$_; \
        printf "  %-20s %s\n", $$_->[0], $$_->[1] for @{$$help{$$_}}; \
        print "\n"; \
    }

args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
	MESSAGE = "No such command (or you pass two or many targets to ). List of possible commands: make help"
else
	MESSAGE = "Done"
endif


run-local: ##@Run Run app in local mode (backend(local) + database(docker))                         [docker-compose.yaml]
	make run-db && make -C backend run-local

run-dev1: ##@Run Run app in dev1 mode  (nginx(http) + backend + database)                          [docker-compose.yaml]
	docker compose up --build database backend nginx

run-dev2: ##@Run Run app in dev2 mode  (nginx(http) + backend + database + graphana + prometheus)  [docker-compose.yaml]
	docker compose up --build

run-prod: ##@Run Run app in prod mode  (nginx(https) + backend + database + graphana + prometheus) [docker-compose-prod.yaml]
	docker compose -f docker-compose-prod.yml up --build

test: ##@Tests Run tests
	make -C backend test

psql:##@Database Connect to database via psql
	psql -d $(POSTGRES_DB) -U $(POSTGRES_USER)

run-db: ##@Database Run database container [docker-compose.yaml]
	docker compose up --build -d database

migrate: ##@Database Apply migrations
	make -C backend migrate

revision: ##@Database Create new revision
	make -C backend revision

gen-ssl: ##@Generators SSL key and certificate to ./certs directory
	openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=localhost" \
	&& mv cert.pem certs/cert.pem && mv key.pem certs/key.pem

gen-hex32: ##@Generators Generate random hex string of 32 characters
	openssl rand -hex 32

module: ##@Generators Generate a new module with the given name, description (eg. make module name=users description="Users management module")
	make -C backend module name=$(name) description=$(description)

help: ##@Help Show this help
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

env: ##@Environment Create .env file from .env.example
	cp .env.example .env

poetry: ##@Environment Setup poetry environment
	cd backend && poetry install --no-root

%::
	echo $(MESSAGE)
