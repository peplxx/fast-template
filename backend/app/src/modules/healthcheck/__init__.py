from .routes import router
from ..base import BaseModule

class HealthcheckModule(BaseModule):
    NAME = "healthcheck"
    DESCRIPTION = "Healthcheck module"
    VERSION = "0.1.0"
    ROUTERS = [router]

    EXPORTS = {
        "router": router
    }
    TAGS = [{
        "name": "Healthcheck",
        "description": "Health status of the application and services",
    }]