import ssl
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pathlib import Path


env_path = Path(__file__).parents[3] / '.env'
load_dotenv(dotenv_path=env_path)


class DefaultSettings(BaseSettings):
    ENV: str = "default"
    PATH_PREFIX: str = "/api/v1"
    APP_HOST: str = "0.0.0.0"
    PROTOCOL: str = "http"
    CURRENT_HOST: str = "0.0.0.0"
    APP_PORT: int = 5000

    POSTGRES_DB: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_PORT: int = 5432
    DB_CONNECT_RETRY: int = 20
    DB_POOL_SIZE: int = 15
    DB_USE_SSL: bool = False
    DB_SSL_KEY_PATH: Optional[str] = None

    SWAGGER_PATH: Optional[str] = "/swagger"
    REDOC_PATH: Optional[str] = None
    
    @property
    def current_host_url(self) -> str:
        return f"{self.PROTOCOL}://{self.CURRENT_HOST}:{self.APP_PORT}"
    
    @property
    def auth_basic_authentication_url(self) -> str:
        return f"{self.current_host_url}{self.PATH_PREFIX}/auth/basic/authentication"
    
    # Module-defined settings
    STATIC_FILES_PATH: str = '/tmp/static'

    @property
    def database_settings(self) -> dict:
        return {
            "database": self.POSTGRES_DB,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
        }

    @property
    def database_uri(self) -> str:
        """ Async database uri"""
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(**self.database_settings)

    @property
    def database_uri_sync(self) -> str:
        """ Sync database uri """
        return "postgresql://{user}:{password}@{host}:{port}/{database}".format(**self.database_settings)

    @property
    def db_context(self) -> dict:
        if not self.DB_USE_SSL: return {}
        ssl_context = ssl.create_default_context(cafile=self.DB_SSL_KEY_PATH)
        ssl_context.verify_mode = ssl.CERT_REQUIRED
        return {"ssl": ssl_context}
