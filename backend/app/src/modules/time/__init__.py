""" Module for managing time-related functionalities """
from ..base import BaseModule
from .now import *

__all__ = ["now", "utcnow", "str_utcnow", 'str_now']
class TimeModule(BaseModule):
    NAME: str = "time"
    DESCRIPTION: str = "Time module"
    VERSION: str = "0.1.0"
    EXPORTS: dict = {
        "now": now,
        "utcnow": utcnow,
        "str_utcnow": str_utcnow,
        "str_now": str_now,
    }
    DEPENDENCIES: list = []
    TAGS: list = []
    ROUTERS: list = []
    
    UPTIME: timedelta = utcnow()