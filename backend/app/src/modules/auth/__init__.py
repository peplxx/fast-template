from ..base import BaseModule
from .settings import AuthSettings, settings
from .routes import router
from .basic.utils import UserDependency


class AuthModule(BaseModule):
    NAME: str = "Auth"
    DESCRIPTION: str = "Authentication module"
    VERSION: str = "0.1.0"
    EXPORTS: dict = {"UserDependency": UserDependency}
    DEPENDENCIES: list = []
    TAGS: list = [
        {
            "name": "Basic Authentication",
            "description": "Basic authentication endpoints",
        },
        {
            "name": "Token Authentication",
            "description": "Token authentication endpoints",
        },
    ]
    ROUTERS: list = [router]

    AUTH_SETTINGS: AuthSettings = settings
    TESTSUITES = []


__all__ = ["AuthModule", *AuthModule.EXPORTS.keys()]
