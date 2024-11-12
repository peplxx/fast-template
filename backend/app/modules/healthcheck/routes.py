from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from app.config import get_settings
from app.src.docs import project
from .health import database_healthcheck
from .schemas import PingResponse
from ...modules.time import utcnow, str_utcnow

router = APIRouter(
    tags=["System"],

)
settings = get_settings()


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
