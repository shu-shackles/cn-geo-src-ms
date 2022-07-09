from fastapi import APIRouter
from pydantic import BaseModel
import json

from models import tag

tags = APIRouter(tags=["标点相关"])


class TagsUploadItem(BaseModel):
  type: int
  area: str
  uid: int
  time: str
  lng: float
  lat: float
  etype: int
  title: str
  desc: str
  imgSrc: str


@tags.post("/upload/:userType", summary="上传标记")
async def tag_upload(item: TagsUploadItem):
  sql_result = tag.tag_upload(item.offset, item.count)
  data = [dict(zip(result.keys(), result)) for result in sql_result]
  result = json.dumps(data)
  return result


@tags.get("/areainformaltags/:area", summary="区域未审核标记")
async def tag_area_informal():
  pass


@tags.get("/areatags/:area", summary="区域审核标记")
async def tag_area():
  pass


@tags.post('/finishaudit/:area', summary="")
async def tag_audit():
  pass
