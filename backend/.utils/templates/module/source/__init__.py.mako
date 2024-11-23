from ..base import BaseModule
from .routes import router

try:  # Tests are not included in Docker container
    from tests.testsuites.${module_name.lower()} import testsuites
except ImportError:
    testsuites = []

class ${module_name}Module(BaseModule):
    NAME: str = "${module_name} module"
    DESCRIPTION: str = "${module_description}"
    VERSION: str = "${version}"
    EXPORTS: dict = {}
    DEPENDENCIES: list = []
    TAGS: list = []
    ROUTERS: list = [router]
    TESTSUITES: list = testsuites

__all__ = ["${module_name}Module", *${module_name}Module.EXPORTS.keys()]
