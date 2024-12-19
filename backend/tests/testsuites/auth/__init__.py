# Import your TestClasses here!
from .default import TestBasicAuth
from ..base import BaseTestSuite


class AuthTestSuite(BaseTestSuite):
    MODULE_NAME: str = "Auth"
    TEST_CLASSES: list = [
        TestBasicAuth,
    ]


__all__ = ["AuthTestSuite"]
