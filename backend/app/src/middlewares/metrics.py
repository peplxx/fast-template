from time import perf_counter

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.metrics.metrics import metrics


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = perf_counter()
        route_path = request.url.path
        if request.scope.get("route"):
            route_path = request.scope["route"].path
        response = await call_next(request)
        metrics.general.responses.labels(
            method=request.method,
            endpoint=route_path,
            status_code=str(response.status_code),
        ).inc(1)
        request_time = (perf_counter() - start_time) * 1000  # Convert to milliseconds
        metrics.general.request_latency_ms.labels(
            method=request.method,
            endpoint=route_path,
            status_code=str(response.status_code),
        ).observe(request_time)
        return response


settings = {
    "middleware_class": MetricsMiddleware,
}
