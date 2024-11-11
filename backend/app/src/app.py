__all__ = ['app']

from datetime import datetime, timedelta
from typing import Dict

from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from starlette import status
from starlette.responses import JSONResponse

from ..config import get_settings
from .docs import project
from .middlewares import middlewares
from .routers import routers
from ..db.connection import database_healthcheck
from ..modules.time import utcnow, str_utcnow

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


class PingResponse(BaseModel):
    message: str
    app: str = Field(..., alias='app.version')
    uptime: timedelta
    client_ip: str
    environment: str
    server_time: str
    services: Dict[str, str]


@app.get(
    settings.PATH_PREFIX + '/ping',
    response_class=JSONResponse,
    tags=["System"],
    status_code=status.HTTP_200_OK,
    response_model=PingResponse,
)
async def ping(request: Request):
    """ Simple endpoint to check if the server is up """
    return {
        "message": "The server is up!",
        "app.version": project.specification['version'],
        "uptime": utcnow() - settings.UPTIME,
        "client_ip": request.client.host,
        "environment": settings.ENV,
        "server_time": str_utcnow(),
        "services": {
            "database": "Ok" if await database_healthcheck() else "Down",
        }
    }
