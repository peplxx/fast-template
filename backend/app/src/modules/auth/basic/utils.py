from fastapi import Depends

from app.db.connection.session import SessionDependency
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, Optional
from sqlalchemy import select
from app.db.models import User
from uuid import UUID

from .schemas import RegistrationForm


from .exceptions import IncorrectCredentialsException
from ..settings import settings
from ..jwt import decode_token


async def get_user(session: AsyncSession, username: str) -> Optional[User]:
    return await session.scalar(select(User).where(User.username == username))


async def authenticate_user(
    session: AsyncSession,
    username: str,
    password: str,
):
    user = await get_user(session, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def verify_password(
    plain_password: str,
    hashed_password: str,
):
    pwd_context = settings.PWD_CONTEXT
    return pwd_context.verify(plain_password, hashed_password)


async def get_current_user(
    session: SessionDependency,
    token: str = Depends(settings.OAUTH2_SCHEME),
) -> User:
    payload = decode_token(token)
    user: Optional[User] = await User.find_by_id(session, UUID(payload.get("sub")))
    if user is None:
        raise IncorrectCredentialsException()
    return user


async def register_user(
    session: AsyncSession, potential_user: RegistrationForm
) -> tuple[bool, str]:
    existing_user = await session.scalar(
        select(User).where(User.username == potential_user.username)
    )
    if existing_user:
        return False, "User with such username already exists."

    user = User(**potential_user.model_dump(exclude_unset=True))
    session.add(user)
    await session.commit()

    return True, "Successful registration!"


UserDependency = Annotated[User, Depends(get_current_user)]
