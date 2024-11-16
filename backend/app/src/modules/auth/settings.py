import secrets
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from os import environ

from app.config import get_settings


class AuthSettings:
    # Auth settings
    def generate_secret_key() -> str:
        return secrets.token_hex(32)

    # To get a string run: "openssl rand -hex 32"
    SECRET_KEY: str = environ.get("SECRET_KEY", generate_secret_key())
    ALGORITHM: str = environ.get("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 1440)
    )
    PWD_CONTEXT: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
    OAUTH2_SCHEME: OAuth2PasswordBearer = OAuth2PasswordBearer(
        tokenUrl=get_settings().auth_basic_authentication_url
    )


settings: AuthSettings = AuthSettings()
__all__ = ["settings", "AuthSettings"]
