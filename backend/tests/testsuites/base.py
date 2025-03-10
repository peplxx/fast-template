from abc import ABC
from app.src.settings import settings


class BaseTestSuite(ABC):
    """Class that defines testing enviroment for module"""

    MODULE_NAME: str
    TEST_CLASSES: list


class BaseTestClass(ABC):
    """Base class for test class
    You can implement here shared methods
    """

    def url(self, path: str) -> str:
        return f"{settings.PATH_PREFIX}{path}"
