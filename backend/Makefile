.PHONY: run-local, test, migrate, revision, module

run-local:
	poetry run python3 -m app

test:
	poetry run python -m pytest

migrate:
	alembic upgrade head

revision:
	alembic revision --autogenerate

module:
	python3 .utils/templates/module/__main__.py "$(name)" "$(description)"
