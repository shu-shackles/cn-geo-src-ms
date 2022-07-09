from fastapi import APIRouter
from pydantic import BaseModel
import json

from models import user

users = APIRouter(tags=["用户相关"])


class InfoItem(BaseModel):
  offset: int
  count: int


class SetInfoItem(BaseModel):
  password: str
  type: int
  area: str
  uid: int


class DeleteItem(BaseModel):
  uid: int

@users.get("/info/:offset/:count", summary="当前用户")
async def user_info(item: InfoItem):
  sql_result = user.user_info(item.offset, item.count)
  data = [dict(zip(result.keys(), result)) for result in sql_result]
  result = json.dumps(data)
  return result


@users.put('/setinfo', summary="修改用户")
async def user_setinfo(item: SetInfoItem):
  if user.user_setinfo(item.password, item.type, item.area, item.uid):
    return "修改成功"
  else:
    return "修改失败"


@users.delete('/deleteuser', summary="")
async def user_delete(item:DeleteItem):
  if user.user_delete(item.uid):
    return "删除成功"
  else:
    return "删除失败"
