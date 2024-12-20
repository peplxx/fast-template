import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.src.modules.auth.basic.utils import register_user
from app.src.modules.auth.basic.schemas import RegistrationForm


@pytest.fixture
def user_data():
    return {"username": "test", "password": "test_test"}


@pytest.fixture
async def test_user(session: AsyncSession, user_data: dict):
    user = await register_user(session, RegistrationForm(**user_data))
    return user
