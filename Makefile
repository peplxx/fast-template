ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif

HELP_FUN = \
	%help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
	if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
    print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
    @{$$help{$$_}},"\n" for keys %help; \

args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
	MESSAGE = "No such command (or you pass two or many targets to ). List of possible commands: make help"
else
	MESSAGE = "Done"
endif


# TODO: add passing args to make commands
run-local: ##@Run Run app locally
	make -C backend run-local
 
run-dev: ##@Run Run app in dev mode (docker compose)
	docker compose up --build

run-prod: ##@Run Run app in prod mode (docker compose)
	docker compose -f docker-compose-prod.yml up --build

test: ##@Tests Run tests
	make -C backend test

psql:##@Database Connect to database via psql
	psql -d $(POSTGRES_DB) -U $(POSTGRES_USER)

run-db: ##@Database Run database container
	docker compose up --build -d database

migrate: ##@Database Run migrations
	make -C backend migrate

revision: ##@Database Create revision
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

%::
	echo $(MESSAGE)
