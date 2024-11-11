__all__ = ['app']

from fastapi import FastAPI

from .docs import project
from .middlewares import middlewares
from .routers import routers
from ..config import get_settings

settings = get_settings()

app = FastAPI(
    **project.specification,
    # lifespan=lifespan,
    docs_url=settings.SWAGGER_PATH,
    redoc_url=settings.REDOC_PATH,
)

for router in routers:
    app.include_router(prefix=settings.PATH_PREFIX, router=router)

for middleware in middlewares:
    app.add_middleware(**middleware)
