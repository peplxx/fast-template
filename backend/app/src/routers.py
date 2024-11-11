__all__ = ['routers']
from ..modules.healthcheck import router as healthcheck_router
routers = [
    healthcheck_router,

]