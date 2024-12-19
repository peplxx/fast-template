from httpx import AsyncClient
import importlib
import pkgutil
import os

# Init testsuites
from testsuites.base import BaseTestSuite
from functools import reduce

# Fetching all existing testsuites
testsuites: list[BaseTestSuite] = []
testsuites_dir = os.path.join(os.path.dirname(__file__), "testsuites")
for loader, module_name, is_pkg in pkgutil.iter_modules([testsuites_dir]):
    if is_pkg:
        module = importlib.import_module(f"testsuites.{module_name}")
        testsuite = getattr(module, f"{module_name.title()}TestSuite")
        testsuites.append(testsuite)

test_classes = reduce(
    lambda x, y: x + y, [testsuite.TEST_CLASSES for testsuite in testsuites]
)
print(vars(test_classes[0]))


# raise ImportError
class TestMain(BaseTestSuite, *test_classes):
    async def test_ping(self, client: AsyncClient):
        response = await client.get(self.url("/ping"))
        assert response.status_code == 200
