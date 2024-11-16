__all__ = ["lifespan"]
import asyncio
from fastapi import FastAPI

from ..metrics.collectors import collectors
from prometheus_client import start_http_server
from app.config import get_settings

settings = get_settings()


async def lifespan(app: FastAPI):
    start_http_server(settings.PROMETHEUS_PORT)
    event_loop = asyncio.get_event_loop()
    for collector in collectors:
        event_loop.create_task(collector())
    yield
