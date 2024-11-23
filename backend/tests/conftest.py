from asyncio import get_event_loop_policy
from logging import getLogger

import pytest
from httpx import AsyncClient, Cookies
from httpx import ASGITransport
from app.config import get_settings
from app.src.app import app
from fixtures import *  # noqa : F403

get_settings().TESTING = True
settings = get_settings()


clients_params = {
    "transport": ASGITransport(app=app),
    "base_url": "http://test",
    "follow_redirects": True,
    "max_redirects": 3,
    "cookies": Cookies(),
}


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for tests"""
    loop = get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def logger():
    return getLogger("[pytest] logger")


@pytest.fixture(scope="module")
async def client():
    """Create async test client"""
    async with AsyncClient(**clients_params) as client:
        yield client
