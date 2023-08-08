import os
import uuid
from .import s3Bucket
import time
from . import s3Bucket
import uuid


timestr= time.strftime("%Y%m%d-%H%M%S")
async def upload_image_modern(file):
    
    filename=f"{uuid.uuid4()}-{timestr}{os.path.splitext(file.filename)[1]}" 
    return await s3Bucket.s3_upload(file, filename)


