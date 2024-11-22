import pytest
from httpx import AsyncClient
from tests.fixtures import url
from app.db.models import User


class TestBasicAuth:
    @pytest.mark.asyncio
    async def test_login(self, client: AsyncClient, test_user: User, user_data: dict):
        response = await client.post(url("/auth/basic/authentication"), data=user_data)
        assert response.status_code == 200
        assert response.json()["access_token"] is not None
        assert response.json()["token_type"] is not None
