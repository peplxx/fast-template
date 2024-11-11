__all__ = ["middlewares"]
from .cors import settings as cors_middleware

middlewares = [
    cors_middleware,
]
