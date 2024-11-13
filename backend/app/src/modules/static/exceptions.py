from fastapi import HTTPException
from starlette import status


class FileNotFoundException(HTTPException):
    def __init__(self, detail: str = "File not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class InvalidFileException(HTTPException):
    def __init__(self, detail: str = "Invalid filename"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)




