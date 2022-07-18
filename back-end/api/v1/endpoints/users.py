from fastapi import APIRouter
from pydantic import BaseModel

from models import user

users = APIRouter(tags=["用户相关"])


# class InfoItem(BaseModel):
#   offset: int
#   count: int


class SetInfoItem(BaseModel):
    password: str
    type: int
    area: str
    uid: int


class DeleteItem(BaseModel):
    uid: int


@users.get("/info/{offset}/{count}", summary="当前用户")
async def user_info(offset, count):
    sql_result = user.user_info(offset, count)
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


@users.put('/setinfo', summary="修改用户")
async def user_setinfo(item: SetInfoItem):
    if user.user_setinfo(item.password, item.type, item.area, item.uid):
        return "修改成功"
    else:
        return "修改失败"


@users.delete('/deleteuser', summary="删除用户")
async def user_delete(item: DeleteItem):
    if user.user_delete(item.uid):
        return "删除成功"
    else:
        return "删除失败"


@users.post('allusers', summary="所有用户信息")
async def user_all():
    sql_result = user.user_all()
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data
