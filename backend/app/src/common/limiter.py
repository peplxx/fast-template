from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.src.settings import settings
from fastapi import Request
from fastapi.responses import JSONResponse

# How to limit an endpoint?
# HB: Enpoint should have a request in args
# -----------------------------------------
# @router.get("/endpoint")
# @limiter.limit("10/second")
# async def endpoint(request: Request):
#     return {"message": "Hello, world!"}
# -----------------------------------------


async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"},
    )


class DummyLimiter:
    """Dummy limiter that does nothing, used to disable rate limiting when needed"""

    def limit(self, *args, **kwargs):
        def decorator(func):
            return func

        return decorator


limiter = DummyLimiter()
if settings.limiter_enabled:
    limiter = Limiter(
        key_func=get_remote_address,
        # default_limits=["200 per day", "50 per hour"]
    )


__all__ = ["limiter", "rate_limit_exceeded_handler"]
