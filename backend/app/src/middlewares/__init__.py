__all__ = ["middlewares"]
from .cors import settings as cors_middleware
from .metrics import settings as metrics_middleware

middlewares = [
    cors_middleware,
    metrics_middleware,
]
