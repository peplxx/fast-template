__all__ = [
    "error_handlers",
]

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from .limiter import rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded


def http_exception_handler(request, exc: HTTPException):
    """Basic exception handler for HTTPException"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers=getattr(exc, "headers", None),
    )


error_handlers = {
    HTTPException: http_exception_handler,
    RateLimitExceeded: rate_limit_exceeded_handler,
}
