from fastapi import APIRouter, Depends
from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordRequestForm

# from models import Users
# from core import verify_password, create_access_token
# from scheams import UserIn_Pydantic
from models import user

login = APIRouter(tags=["认证相关"])


class Login_Item(BaseModel):
  name: str
  password: str


class Register_Item(BaseModel):
  name: str
  password: str


@login.post("/login", summary="用户登录")
async def user_login(item: Login_Item):
  if user.confirm_user(item.name):
    if user.is_password(item.name, item.password):
      return "密码正确"
    else:
      return "密码错误"
  else:
    return "用户名不存在"


@login.post("/register", summary="用户注册")
async def user_register(item: Register_Item):
  if user.confirm_user(item.name):
    return "用户名重复"
  else:
    if user.insert(item.name, item.password):
      return "插入成功"
    else:
      return "插入失败"
