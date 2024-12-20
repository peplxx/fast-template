from functools import reduce
import importlib
import pkgutil
import os

from .base import BaseTestSuite, BaseTestClass
from app.src.modules.base import BaseModule


def load_testsuites(modules: list[BaseModule]) -> list[BaseTestSuite]:
    testsuites: list[BaseTestSuite] = []
    imported_module_names = [module.NAME for module in modules]
    testsuites_dir = os.path.join(
        os.path.dirname(__file__),
    )
    for _, module_name, is_pkg in pkgutil.iter_modules([testsuites_dir]):
        if not is_pkg:
            continue

        module = importlib.import_module(f"testsuites.{module_name}")
        testsuite: BaseTestSuite = getattr(module, f"{module_name.title()}TestSuite")
        if testsuite.MODULE_NAME in imported_module_names:
            testsuites.append(testsuite)
    return testsuites


def extract_test_classes(testsuites: list[BaseTestSuite]) -> list[BaseTestClass]:
    return (
        reduce(lambda x, y: x + y, [testsuite.TEST_CLASSES for testsuite in testsuites])
        if len(testsuites)
        else []
    )
