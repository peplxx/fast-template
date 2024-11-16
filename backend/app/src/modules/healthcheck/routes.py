from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from app.config import get_settings
from .health import database_healthcheck
from .schemas import PingResponse
from ...modules.time import TimeModule, str_utcnow

router = APIRouter(
    tags=["Healthcheck"],
)
settings = get_settings()


@router.get(
    "/ping",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    response_model=PingResponse,
)
async def ping(request: Request):
    """Simple endpoint to check if the server is up"""
    return {
        "message": "The server is up!",
        "uptime": TimeModule.UPTIME,
        "client_ip": request.client.host,
        "environment": settings.ENV,
        "server_time": str_utcnow(),
        "services": {
            "database": "Ok" if await database_healthcheck() else "Down",
        },
    }
