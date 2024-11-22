import pytest
from httpx import AsyncClient
from tests.conftest import url
from app.db.models import User


@pytest.mark.asyncio
class TestMain:
    class TestAuth:
        async def test_login(
            self, client: AsyncClient, test_user: User, user_data: dict
        ):
            response = await client.post(
                url("/auth/basic/authentication"), data=user_data
            )
            assert response.status_code == 200
            assert response.json()["access_token"] is not None
            assert response.json()["token_type"] is not None

    @pytest.mark.asyncio
    async def test_ping(self, client: AsyncClient):
        response = await client.get(url("/ping"))
        assert response.status_code == 200
