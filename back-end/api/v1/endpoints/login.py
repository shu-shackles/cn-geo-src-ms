from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models import User
from core import verify_password, create_access_token
from scheams import UserIn_Pydantic

login = APIRouter(tags=["认证相关"])


@login.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if user := await User.get(username=form_data.username):
        if verify_password(form_data.password, user.password):
            return {"access_token": create_access_token({"id": user.pk}), "token_type": "bearer"}
    return {"msg": "账号或密码错误"}


@login.post("/user", summary="用户新增")
async def user_create(user: UserIn_Pydantic):
    await User.create(**user.dict())
    return 1
