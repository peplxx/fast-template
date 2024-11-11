from datetime import timedelta
from typing import Dict

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
from starlette import status
from starlette.responses import JSONResponse

from app.config import get_settings
from app.db.connection import database_healthcheck
from app.modules.time import utcnow, str_utcnow
from app.src.docs import project

router = APIRouter(
    tags=["System"],

)
settings = get_settings()

class PingResponse(BaseModel):
    message: str
    app: str = Field(..., alias='app.version')
    uptime: timedelta
    client_ip: str
    environment: str
    server_time: str
    services: Dict[str, str]


@router.get(
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