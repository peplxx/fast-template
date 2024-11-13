from .static import StaticModule
from .healthcheck import HealthcheckModule
from .time import TimeModule
from .auth import AuthModule


modules = [
    StaticModule,
    HealthcheckModule,
    TimeModule,
    AuthModule,
]
