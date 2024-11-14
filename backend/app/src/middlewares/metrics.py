from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import Counter, Histogram
import time
from app.metrics.metrics import metrics
from ..modules.time import utcnow

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = utcnow()
        
        route_path = request.url.path
        if request.scope.get("route"):
            route_path = request.scope["route"].path
        response = await call_next(request)
        metrics.general.responses.labels(method=request.method,
                                         endpoint=route_path, 
                                         status_code=str(response.status_code)).inc()
        metrics.general.request_latency_ms.labels(method=request.method, 
                                                  endpoint=route_path, 
                                                  status_code=str(response.status_code)).observe((utcnow() - start_time).total_seconds() * 1000)
        return response
        
settings = {
    "middleware_class": MetricsMiddleware,
}
