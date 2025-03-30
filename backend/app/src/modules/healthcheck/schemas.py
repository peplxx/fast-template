from datetime import datetime
from typing import Dict

from pydantic import BaseModel


class PingResponse(BaseModel):
    message: str
    uptime: datetime
    client_ip: str
    server_time: str
    services: Dict[str, str]
