from httpx import AsyncClient

# Init testsuites
from testsuites.base import BaseTestClass, BaseTestSuite
from testsuites.utils import load_testsuites, extract_test_classes
from app.src.modules import modules

testsuites: list[BaseTestSuite] = load_testsuites(modules)
test_classes: list[BaseTestClass] = extract_test_classes(testsuites)


class TestMain(*test_classes, BaseTestClass):
    async def test_ping(self, client: AsyncClient):
        response = await client.get(self.url("/ping"))
        assert response.status_code == 200
