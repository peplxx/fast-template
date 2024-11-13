from fastapi import APIRouter, UploadFile
from starlette import status
from starlette.responses import JSONResponse
from fastapi.responses import StreamingResponse
import mimetypes

from .services import FileService

router = APIRouter(
    tags=["Static Files"],
    prefix="/static"
)

@router.get(
    "/{filename}",
    response_class=StreamingResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Return the file content"},
        404: {"description": "File not found"},
        400: {"description": "Invalid filename"}
    }
)
async def get_file(filename: str):
    path = FileService._get_private_filename(filename)
    return StreamingResponse(
        FileService.get_private_content_file(path),
        media_type=mimetypes.guess_type(path)[0]
    )

@router.post(
    "/upload_file",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "File uploaded successfully"},
        400: {"description": "Invalid file"}
    }
)
async def upload_file(file: UploadFile):
    file_link = await FileService.save_uploaded_file(file)
    return JSONResponse(
        content={"message": "File added successfully", "file_link": file_link},
        status_code=status.HTTP_201_CREATED,
    )
