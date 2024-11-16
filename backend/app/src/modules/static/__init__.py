from ..base import BaseModule
from .routes import router
from .services import FileService
from .exceptions import FileNotFoundException, InvalidFileException
from .settings import StaticFileSettings, settings


class StaticModule(BaseModule):
    NAME = "static"
    DESCRIPTION = "Module for handling static files and file upload s"
    VERSION = "0.1.0"
    ROUTERS = [router]

    EXPORTS = {
        "router": router,
        "exceptions": [FileNotFoundException, InvalidFileException],
    }

    DEPENDENCIES = []  # If you have a storage module

    # OpenAPI tags for documentation
    TAGS = [
        {
            "name": "Static Files",
            "description": "Operations with static files including upload and retrieval",
        }
    ]
    AUTH_SETTINGS: StaticFileSettings = settings

    # Module configuration and health checks
    def __init__(self):
        self.storage_path = FileService.STORAGE_PATH


__all__ = ["router"]
