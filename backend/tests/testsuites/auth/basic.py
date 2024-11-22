from httpx import AsyncClient
from tests.fixtures import url
from app.db.models import User


class TestBasicAuth:
    async def test_login(self, client: AsyncClient, test_user: User, user_data: dict):
        response = await client.post(url("/auth/basic/authentication"), data=user_data)
        assert response.status_code == 200
        assert response.json()["access_token"] is not None
        assert response.json()["token_type"] is not None

    async def test_login_invalid_credentials(self, client: AsyncClient):
        invalid_data = {"username": "nonexistent", "password": "wrongpassword"}
        response = await client.post(
            url("/auth/basic/authentication"), data=invalid_data
        )
        assert response.status_code == 401

    async def test_registration(self, client: AsyncClient):
        new_user_data = {
            "username": "newuser",
            "password": "newpassword123",
            "email": "newuser@example.com",
        }
        response = await client.post(
            url("/auth/basic/registration"), json=new_user_data
        )
        assert response.status_code == 201
        assert "message" in response.json()

    async def test_registration_existing_user(
        self, client: AsyncClient, test_user: User, user_data: dict
    ):
        response = await client.post(
            url("/auth/basic/registration"),
            json={
                "username": user_data["username"],
                "password": "somepassword",
                "email": "test@example.com",
            },
        )
        assert response.status_code == 400
