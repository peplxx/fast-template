from httpx import AsyncClient
from tests.fixtures import url

# Init testsuites
from functools import reduce
from app.src.modules import modules

testsuites = reduce(
    lambda x, y: x + y, [module.TESTSUITES for module in modules]
)  # Get all testsuites from all modules


class TestMain(*testsuites):
    async def test_ping(self, client: AsyncClient):
        response = await client.get(url("/ping"))
        assert response.status_code == 200
