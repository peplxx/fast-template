from fastapi import APIRouter
from .basic.routes import router as basic_router

routers = [
    basic_router,
]
router = APIRouter(prefix="/auth")

for route in routers:
    router.include_router(route)

__all__ = ["router"]
