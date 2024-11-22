from datetime import timedelta
from typing import Optional

from jose import jwt
from jose.exceptions import JWTError

from ..settings import settings
from ..basic.exceptions import IncorrectCredentialsException
from app.src.modules.time import utcnow


def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        raise IncorrectCredentialsException()


def create_token(
    payload: dict,
    expires_delta: Optional[timedelta] = None,
):
    if expires_delta:
        expire = utcnow() + expires_delta
    else:
        expire = utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
