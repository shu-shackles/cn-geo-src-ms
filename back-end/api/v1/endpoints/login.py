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


@login.post("/login", summary="用户登录")
async def user_login(item: Login_Item):
  if user.confirm_user(item.name):
    return "有"
  else:
    return "没有"


@login.post("/register", summary="用户注册")
async def user_register():
  pass
