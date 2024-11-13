from fastapi import HTTPException, status


class IncorrectCredentialsException(HTTPException):
    def __init__(self, detail: str = "Incorrect credentials"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class UserAlreadyExist(HTTPException):
    def __init__(self, detail: str = "User with such username already exists."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
