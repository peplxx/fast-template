from abc import ABC, abstractmethod


class BaseModule(ABC):
    NAME: str
    DESCRIPTION: str
    VERSION: str
    EXPORTS: dict
    DEPENDENCIES: list = []
    TAGS: list = []
    ROUTERS: list = []
    TESTSUITES: list = []

    @abstractmethod
    def upgrade(self) -> bool:
        """Set up module dependencies and infrastructure"""
        pass

    @abstractmethod
    def downgrade(self) -> bool:
        """Remove module dependencies and cleanup infrastructure"""
        pass
