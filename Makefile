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



run-local: ##@Run application locally
	$(MAKE) -C backend run-local

test: ##@Tests Run tests
	$(MAKE) -C backend test

psql:##@Database Connect to database via psql
	psql -d $(POSTGRES_DB) -U $(POSTGRES_USER)

gen-ssl: ##@Generators SSL key and certificate to ./certs directory
	openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=localhost" \
	&& mv cert.pem certs/cert.pem && mv key.pem certs/key.pem

help: ##@Help Show this help
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

%::
	echo $(MESSAGE)