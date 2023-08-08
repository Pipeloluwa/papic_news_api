from fastapi import APIRouter, status, File, UploadFile
from ..import schemas, database
from ..repository import file_uploads
from ..repository import s3Bucket


router= APIRouter(prefix="/upload-files", tags=["Files Upload"])
get_db= database.get_database

@router.post("/picture-upload-modern", status_code= status.HTTP_201_CREATED)
async def upload_image_modern2(file: UploadFile= File(...)):
    return await file_uploads.upload_image_modern(file)

@router.post("/picture-download-modern", status_code= status.HTTP_200_OK)
async def download_image_modern2(id: schemas.Media2):
    return await s3Bucket.s3_download(id.filename)

@router.post("/picture-delete-modern")
async def delete_image_modern2(id: schemas.Media2):
    return await s3Bucket.s3_delete(id.filename)


