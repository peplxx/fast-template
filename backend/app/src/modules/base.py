from abc import ABC


class BaseModule(ABC):
    NAME: str
    DESCRIPTION: str
    VERSION: str
    EXPORTS: dict
    DEPENDENCIES: list = []
    TAGS: list = []
    ROUTERS: list = []
    TESTSUITES: list = []
