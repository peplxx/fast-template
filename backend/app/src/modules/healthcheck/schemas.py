from datetime import timedelta
from typing import Dict

from pydantic import BaseModel, Field


class PingResponse(BaseModel):
    message: str
    app: str = Field(..., alias='app.version')
    uptime: timedelta
    client_ip: str
    environment: str
    server_time: str
    services: Dict[str, str]
