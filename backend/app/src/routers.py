__all__ = ['routers']
from .modules import modules


routers = [
    *[router for module in modules if hasattr(module, "ROUTERS") for router in module.ROUTERS]
]