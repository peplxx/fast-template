# Import your TestClasses here!
from .default import Test${module_name.title()}Module
from ..base import BaseTestSuite

class {module_name.title()}TestSuite(BaseTestSuite):
    MODULE_NAME: str = {module_name.title()}
    TEST_CLASSES: list[type] = [
        Test${module_name.title()}Module,

    ]

__all__ = ["{module_name.title()}TestSuite"]
