__all__ = ["app"]

import logging
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from .common.logging import logging_settings, setup_logging

from .common.exceptions import error_handlers

from .docs import project
from .middlewares import middlewares
from .routers import routers
from .settings import settings
from .lifespan import lifespan

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

if settings.SCALAR_PATH:

    @app.get(settings.SCALAR_PATH, include_in_schema=False)
    async def scalar_html():
        return get_scalar_api_reference(
            openapi_url=app.openapi_url,
            title=app.title,
            hide_models=True,
        )
