.PHONY: run-local, test, migrate, revision

run-local:
	poetry run python3 -m app

test:
	poetry run python -m pytest

migrate:
	alembic upgrade head

revision:
	alembic revision --autogenerate
