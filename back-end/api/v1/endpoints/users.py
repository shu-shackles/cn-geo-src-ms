from fastapi import APIRouter, Response
from pydantic import BaseModel

from models import user
from core import get_password_hash

users = APIRouter(tags=["用户相关"])


# class InfoItem(BaseModel):
#   offset: int
#   count: int
class SetInfoItem(BaseModel):
    type: int
    password: str
    area: str
    uid: int


class SetInfoTypeAreaItem(BaseModel):
    type: int
    area: str
    uid: int


class SetInfoTypeItem(BaseModel):
    type: int
    uid: int


class SetInfoPasswordItem(BaseModel):
    password: str
    check_pass: str
    uid: int


class SetInfoAreaItem(BaseModel):
    area: str
    uid: int


class DeleteItem(BaseModel):
    uid: int


@users.get("/info/{offset}/{count}", summary="当前用户")
async def user_info(offset, count):
    sql_result = user.user_info(offset, count)
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


@users.post('/setinfo', summary="修改用户")
async def user_setinfo(item: SetInfoItem):
    if item.password == user.get_password_uid(item.uid):
        if user.user_setinfotype(item.type, item.uid) and user.user_setinfoarea(item.area, item.uid):
            return "修改成功"
        else:
            return "修改失败"
    if len(item.password) > 16:
        return "密码长度大于16位"
    if len(item.password) < 6:
        return "密码长度小于6位"
    item.password = get_password_hash(item.password)
    if user.user_setinfo(item.type, item.password, item.area, item.uid):
        return "修改成功"
    else:
        return "修改失败"


@users.post('/setinfo_type_area', summary="修改用户类型和地区")
async def user_setinfo_type_area(item: SetInfoTypeAreaItem):
    if user.user_setinfotype(item.type, item.uid) and user.user_setinfoarea(item.area, item.uid):
        return "修改成功"
    else:
        return "修改失败"


@users.post('/setinfotype', summary="修改用户类型")
async def user_setinfotype(item: SetInfoTypeItem):
    if user.user_setinfotype(item.type, item.uid):
        return "修改成功"
    else:
        return "修改失败"


@users.post('/setinfopassword', summary="修改用户密码")
async def user_setinfopassword(item: SetInfoPasswordItem, response: Response):
    if not item.password == item.check_pass:
        response.status_code = 234
        return "两次密码输入不一致"
    if len(item.password) > 16:
        response.status_code = 230
        return "密码长度大于16位"
    if len(item.password) < 6:
        response.status_code = 231
        return "密码长度小于6位"
    item.password = get_password_hash(item.password)
    if user.user_setinfopassword(item.password, item.uid):
        return "修改成功"
    else:
        return "修改失败"


@users.post('/setinfoarea', summary="修改用户地区")
async def user_setinfoarea(item: SetInfoAreaItem):
    if user.user_setinfoarea(item.area, item.uid):
        return "修改成功"
    else:
        return "修改失败"


@users.delete('/deleteuser', summary="删除用户")
async def user_delete(item: DeleteItem):
    if user.user_delete(item.uid):
        return "删除成功"
    else:
        return "删除失败"


@users.post('/allusers', summary="所有用户信息")
async def user_all():
    sql_result = user.user_all()
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data
