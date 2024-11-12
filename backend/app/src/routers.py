__all__ = ['routers']
from ..modules.healthcheck import router as healthcheck_router
from ..modules.static import router as static_router

routers = [
    healthcheck_router,
    static_router,

]