#!/bin/bash
# This script runs on the database container startup
# You can use it to create databases, tables, etc.

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE "$POSTGRES_DB";
EOSQL
