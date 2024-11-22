FROM python:3.12-slim

RUN pip install poetry --timeout 120


WORKDIR /workdir/

COPY ./poetry.lock .
COPY ./pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --without test,dev

COPY . /backend/

WORKDIR /backend/

EXPOSE 5000

CMD  ["poetry", "run", "python3", "-m", "app"]
