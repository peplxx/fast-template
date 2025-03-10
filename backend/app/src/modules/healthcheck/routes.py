from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from app.src.settings import settings
from .health import database_healthcheck
from .schemas import PingResponse
from ...modules.time import TimeModule, str_utcnow
from ...common.limiter import limiter

router = APIRouter(
    tags=["Healthcheck"],
)


@router.get(
    "/ping",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    response_model=PingResponse,
)
@limiter.limit("1/second")
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
