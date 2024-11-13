import os
import mimetypes
from typing import AsyncIterator
from uuid import uuid4
from fastapi import HTTPException, UploadFile

from app.config import get_settings
from .exceptions import FileNotFound

class FileService:
    @staticmethod
    def _get_private_filename(filename: str) -> str:
        if "/" in filename:
            raise HTTPException(status_code=400, detail="Path should not include directories")
        return os.path.join(get_settings().STATIC_FILES_PATH, filename)

    @staticmethod
    async def get_private_content_file(path: str) -> AsyncIterator[bytes]:
        mime_type = mimetypes.guess_type(path)[0]
        if not os.path.exists(path):
            raise FileNotFound()
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
        settings = get_settings()
        parent_dir = settings.STATIC_FILES_PATH
        os.makedirs(parent_dir, exist_ok=True)
        
        path_to_file = FileService.get_unique_filename(parent_dir, file)
        contents = file.file.read()
        
        with open(path_to_file, "wb") as f:
            f.write(contents)
            
        return os.path.basename(path_to_file) 