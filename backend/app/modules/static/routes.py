import mimetypes
import os
from typing import Iterable
from uuid import uuid4

from fastapi import APIRouter, HTTPException, UploadFile
from starlette import status
from starlette.responses import HTMLResponse, JSONResponse
from fastapi.responses import StreamingResponse

from app.config import get_settings
from .exceptions import FileNotFound

router = APIRouter(
    tags=["Static Files"],
    prefix="/static"
)


def get_private_content_filename(filename: str) -> str:
    if "/" in filename:
        raise HTTPException(status_code=400, detail="Path should not include directories")
    return os.path.join(get_settings().STATIC_FILES_PATH, filename)


async def get_private_content_file(path: str) -> Iterable[bytes]:
    mime_type = mimetypes.guess_type(path)[0]
    if not os.path.exists(path):
        raise FileNotFound()
    with open(path, "rb") as file:
        chunk = file.read(1024)
        while chunk:
            yield chunk
            chunk = file.read(1024)


@router.get(
    "/{filename}",
    responses={
        # TODO: Fill response types
    },
    response_class=StreamingResponse,
    status_code=status.HTTP_200_OK
)
def get_private_content(filename: str):
    path = get_private_content_filename(filename)
    return StreamingResponse(
        get_private_content_file(path),
        media_type=mimetypes.guess_type(path)[0]
    )


def get_unique_filename(parent_dir: str, file: UploadFile) -> str:
    ext = file.filename.rsplit(".", 1)[-1]
    filename = str(uuid4()) + "." + ext
    return os.path.join(parent_dir, filename)


@router.post(
    "/upload_file",
    status_code=status.HTTP_201_CREATED,
    responses={
        # TODO: Fill response types
    }
)
def upload_file(file: UploadFile):
    settings = get_settings()
    parent_dir = settings.STATIC_FILES_PATH
    os.makedirs(parent_dir, exist_ok=True)
    path_to_file = get_unique_filename(parent_dir, file)
    contents = file.file.read()
    with open(path_to_file, "wb") as f:
        f.write(contents)
    file_link = os.path.basename(path_to_file)
    return JSONResponse(
        content={"message": "File added successfully", "file_link": file_link},
        status_code=status.HTTP_201_CREATED,
    )
