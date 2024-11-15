import pytest
from httpx import AsyncClient
from tests.conftest import url


@pytest.mark.asyncio
async def test_ping(client: AsyncClient):
    response = await client.get(url("/ping"))
    assert response.status_code == 200
