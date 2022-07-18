from fastapi import APIRouter, Response, status
from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordRequestForm

# from models import Users
# from core import verify_password, create_access_token
# from scheams import UserIn_Pydantic
from models import user

login = APIRouter(tags=["认证相关"])


class LoginItem(BaseModel):
    username: str
    password: str


class RegisterItem(BaseModel):
    username: str
    password: str
    check_pass: str
    ID: str
    IDNAME: str


@login.post("/login", summary="用户登录")
async def user_login(item: LoginItem, response: Response):
    if user.confirm_user(item.username):
        if user.is_password(item.username, item.password):
            response.status_code = status.HTTP_200_OK
            return "密码正确"
        else:
            response.status_code = 230
            return "密码错误"
    else:
        response.status_code = 231
        return "用户名不存在"


@login.post("/register", summary="用户注册")
async def user_register(item: RegisterItem, response: Response):
    if not item.password == item.check_pass:
        response.status_code = 234
        return "两次密码输入不一致"
    if len(item.password) > 16:
        response.status_code = 230
        return "密码长度大于16位"
    if len(item.password) < 6:
        response.status_code = 231
        return "密码长度小于6位"
    if user.confirm_user(item.username):
        response.status_code = 232
        return "用户名重复"
    else:
        if user.insert(item.username, item.password, item.ID, item.IDNAME):
            return "插入成功"
        else:
            response.status_code = 233
            return "插入失败"
