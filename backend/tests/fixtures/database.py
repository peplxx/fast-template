from app.config import get_settings
from uuid import uuid4
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database
from types import SimpleNamespace
from os import environ
from alembic.config import Config
from alembic.command import upgrade
from .utils import make_alembic_config

__all__ = ["postgres", "async_engine", "session"]

settings = get_settings()


@pytest.fixture(scope="session")
def postgres():
    """Create a temporary database for testing"""
    tmp_name = uuid4().hex
    settings.POSTGRES_DB = tmp_name
    environ["POSTGRES_DB"] = tmp_name
    tmp_url = get_settings().database_uri_sync
    if not database_exists(tmp_url):
        create_database(tmp_url)
    try:
        yield get_settings().database_uri
    finally:
        drop_database(tmp_url)


def run_upgrade(connection, cfg):
    """Run the alembic upgrade"""
    cfg.attributes["connection"] = connection
    upgrade(cfg, "head")


async def run_async_upgrade(config: Config, engine_async, logger):
    """Run the alembic upgrade in async way"""
    logger.debug("Starting upgrade")
    async with engine_async.begin() as conn:
        await conn.run_sync(run_upgrade, config)
    logger.debug("Upgrade completed")


@pytest.fixture(scope="session")
async def async_engine(postgres, logger):
    """Create an async engine for testing"""
    cmd_options = SimpleNamespace(
        config="", name="alembic", pg_url=postgres, raiseerr=False, x=None
    )
    alembic_config = make_alembic_config(cmd_options)
    engine = create_async_engine(postgres, future=True, echo=True)
    await run_async_upgrade(alembic_config, engine, logger)
    yield engine
    await engine.dispose()


@pytest.fixture(scope="session")
async def session(async_engine):
    """Create a new session for each test session"""
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    session = Session()
    try:
        yield session
    finally:
        await session.close()
