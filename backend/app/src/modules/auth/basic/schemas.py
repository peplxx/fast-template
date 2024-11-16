from pydantic import BaseModel, constr, field_validator, Field
from ..settings import settings


class Token(BaseModel):
    access_token: str
    token_type: str


class RegistrationForm(BaseModel):
    username: str = Field(..., description="Username")
    password: constr(min_length=8) = Field(..., description="Password")

    @field_validator("password")
    def validate_password(cls, password):
        password = settings.PWD_CONTEXT.hash(password)
        return password


class RegistrationSuccess(BaseModel):
    message: str = Field(..., examples=["Successful registration!"])


class TestAuthorizationResponse(BaseModel):
    message: str = Field(..., examples=["You are authorized as test_user!"])
