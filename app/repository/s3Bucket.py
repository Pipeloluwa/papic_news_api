import boto3
from loguru import logger
import os
from fastapi.responses import FileResponse
import os
from fastapi import status, Response, HTTPException
from dotenv import load_dotenv

load_dotenv()

s3= boto3.resource(
    service_name= "s3",
    region_name= "us-east-1",
    aws_access_key_id= os.getenv("aws_access_key_id"),
    aws_secret_access_key= os.getenv("aws_secret_access_key")
    )

S3_BUCKET_NAME= "fapibucket"
bucket= s3.Bucket(S3_BUCKET_NAME)
bucket_folder_path= "images"


session= boto3.session.Session()
s3_client= session.client(
    's3',
    aws_access_key_id= os.getenv("aws_access_key_id"),
    aws_secret_access_key= os.getenv("aws_secret_access_key")
)

def id_folder_split(id):
    return os.path.splitext(id)[0]

UPLOAD_DIR= os.path.join("app/media/images")
async def s3_upload(file, filename):
    logger.info(f"Uploading {file.filename} to s3")
    id_folder= id_folder_split(filename)
    s3_client.put_object(Bucket= S3_BUCKET_NAME, Key=bucket_folder_path + "/" + id_folder + "/")
    filename_and_path= f"{bucket_folder_path}/{id_folder}/{filename}"
    bucket.upload_fileobj(file.file, f"{filename_and_path}")
    uploaded_file_url= f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{filename_and_path}" 
    return uploaded_file_url

async def s3_download(id):
    id_folder= id_folder_split(id)
    filename_and_path= f"{bucket_folder_path}/{id_folder}/{id}"
    default_filename= f"downloaded{os.path.splitext(id)[1]}"
    try:
        s3_client.download_file(f"{S3_BUCKET_NAME}", f"{filename_and_path}",f"{UPLOAD_DIR}/{default_filename}")
        return FileResponse(path=f"{UPLOAD_DIR}/{default_filename}", media_type="application/octet-stream", filename= id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Either this file is no more available or the name of this file you are trying to download does not exist, trying to download again could solve the problem")

async def s3_delete(id):
    id_folder= id_folder_split(id)
    filename_and_path= f"{bucket_folder_path}/{id_folder}/{id}"
    try:
        s3.Object(bucket.name, filename_and_path).delete()
        return Response(status_code= status.HTTP_204_NO_CONTENT)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Either the file was already deleted or the file with this name does not exist")
    

