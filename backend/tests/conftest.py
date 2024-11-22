from asyncio import get_event_loop_policy
from logging import getLogger

import pytest
from httpx import AsyncClient, Cookies

from app.config import get_settings
from app.src.app import app
from fixtures import *  # noqa : F403

settings = get_settings()


def url(path: str) -> str:
    return f"{settings.PATH_PREFIX}{path}"


clients_params = {
    "app": app,
    "base_url": "http://test",
    "follow_redirects": True,
    "max_redirects": 3,
    "cookies": Cookies(),
}


@pytest.fixture(scope="session")
def logger():
    return getLogger("[pytest] logger")


@pytest.fixture(scope="module")
def event_loop():
    policy = get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def client():
    """Create async test client"""
    async with AsyncClient(**clients_params) as client:
        yield client
