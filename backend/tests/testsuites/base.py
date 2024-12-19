from abc import ABC

from app.config import get_settings


class BaseTestSuite(ABC):
    """Baseclass for defining testsuites for module"""

    MODULE_NAME: str
    TEST_CLASSES: list


class BaseTestClass(ABC):
    def url(self, path: str) -> str:
        return f"{get_settings().PATH_PREFIX}{path}"
