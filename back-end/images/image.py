from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import os

image = APIRouter(tags=["图片相关"])


class SelectImageItem(BaseModel):
    file_name: str


@image.post("/upload_image", summary="上传图片")
async def image_upload(file: UploadFile):
    image_bytes = file.file.read()
    image_name = file.filename
    # 避免重名
    i = 1
    while os.path.exists(f'images/{image_name}({i})'):
        i = i + 1
    fout = open(f'images/{image_name}({i})', 'wb')
    fout.write(image_bytes)
    fout.close()
    return {f'images/{image_name}({i})'}


@image.post("/seek_image", summary="查找图片")
async def user_login(item: SelectImageItem):
    file_like = open(f'{item.file_name}', mode="rb")
    return StreamingResponse(file_like, media_type="image/jpg")
