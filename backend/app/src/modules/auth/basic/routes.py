from fastapi import APIRouter, Body, Depends, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from app.db.connection import get_session
from ..settings import settings
from .utils import UserDependency, authenticate_user, register_user
from ..jwt import create_token
from .schemas import (
    RegistrationForm,
    RegistrationSuccess,
    TestAuthorizationResponse,
    Token,
)
from app.db.models import User
from .exceptions import IncorrectCredentialsException, UserAlreadyExist

router = APIRouter(prefix="/basic", tags=["Basic Authentication"])


@router.post(
    "/authentication",
    status_code=status.HTTP_200_OK,
    response_model=Token,
    responses={
        "401": {"description": "Incorrect credentials"},
    },
)
async def authentication(
    _: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
):
    user: User = await authenticate_user(
        session, form_data.username, form_data.password
    )

    if not user:
        raise IncorrectCredentialsException()

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(
        payload={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post(
    "/registration",
    status_code=status.HTTP_201_CREATED,
    response_model=RegistrationSuccess,
    responses={
        "400": {"description": "User with such username already exists."},
    },
)
async def registration(
    _: Request,
    registration_form: RegistrationForm = Body(...),
    session: AsyncSession = Depends(get_session),
):
    is_success, message = await register_user(session, registration_form)
    if is_success:
        return {"message": message}
    raise UserAlreadyExist()


@router.get(
    "/test",
    status_code=status.HTTP_200_OK,
    response_model=TestAuthorizationResponse,
    responses={
        "401": {"description": "Unauthorized"},
    },
)
async def test_authorization(_: Request, user: UserDependency):
    return {"message": f"You are authorized as {user.username}!"}
