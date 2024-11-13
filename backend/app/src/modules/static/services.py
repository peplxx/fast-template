import os
import mimetypes
from typing import AsyncIterator
from uuid import uuid4
from fastapi import HTTPException, UploadFile

from app.config import get_settings
from .exceptions import FileNotFoundException, InvalidFileException
from starlette import status


class FileService:
    STORAGE_PATH: str = get_settings().STATIC_FILES_PATH
    @staticmethod
    def _get_filename(filename: str) -> str:
        if "/" in filename:
            raise InvalidFileException("Invalid filename")
        return os.path.join(FileService.STORAGE_PATH, filename)
    @staticmethod
    def _check_file_exists(path: str) -> bool:
        if not os.path.exists(path):
            raise FileNotFoundException()
        return True
    
    @staticmethod
    async def get_content_file(path: str) -> AsyncIterator[bytes]:
        
        with open(path, "rb") as file:
            while chunk := file.read(1024):
                yield chunk

    @staticmethod
    def get_unique_filename(parent_dir: str, file: UploadFile) -> str:
        ext = file.filename.rsplit(".", 1)[-1]
        filename = str(uuid4()) + "." + ext
        return os.path.join(parent_dir, filename)

    @staticmethod
    async def save_uploaded_file(file: UploadFile) -> str:
        os.makedirs(FileService.STORAGE_PATH, exist_ok=True)
        
        path_to_file = FileService.get_unique_filename(FileService.STORAGE_PATH, file)
        contents = file.file.read()
        
        with open(path_to_file, "wb") as f:
            f.write(contents)
            
        return os.path.basename(path_to_file) 