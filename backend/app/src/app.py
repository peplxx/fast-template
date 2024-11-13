__all__ = ['app']

import logging
from fastapi import FastAPI

from .common.logger import logging_settings, setup_logging  

from .common.exceptions import error_handlers

from .docs import project
from .middlewares import middlewares
from .routers import routers
from ..config import get_settings
from .lifespan import lifespan
settings = get_settings()

app = FastAPI(
    **project.specification,
    lifespan=lifespan,
    docs_url=settings.SWAGGER_PATH,
    redoc_url=settings.REDOC_PATH,
)

for router in routers:
    app.include_router(prefix=settings.PATH_PREFIX, router=router)

for middleware in middlewares:
    app.add_middleware(**middleware)

for error_type, handler in error_handlers.items():
    app.add_exception_handler(error_type, handler)

logger = setup_logging()

if logging_settings.ENABLE_SQLALCHEMY_LOGGING: 
    logger.warning("Enable sqlalchemy logging")
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

