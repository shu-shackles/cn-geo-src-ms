from fastapi import APIRouter, Response, status, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm

from core import get_password_hash, verify_password, create_access_token, get_current_user
from core.security import oauth2_scheme
from models import user

login = APIRouter(tags=["认证相关"])


class LoginItem(BaseModel):
    username: str
    password: str


class LoginItemAccess(BaseModel):
    username: str
    password: str


class RegisterItem(BaseModel):
    username: str
    password: str
    # 两次输入密码保证内容正确
    check_pass: str
    # 身份证号
    ID: str
    # 姓名
    IDNAME: str


@login.post("/login", summary="用户登录")
async def user_login(item: LoginItem, response: Response):
    sql_result = user.get_password(item.username)
    # 将数据库查询结果转换为字典列表
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    # 确认用户存在
    if user.confirm_user(item.username):
        # 确认密码是否正确
        if verify_password(item.password, data[0]["password"]):
            response.status_code = status.HTTP_200_OK
            sql_result = user.get_user(item.username)
            data = [dict(zip(result.keys(), result)) for result in sql_result]
            return data
        else:
            response.status_code = 230
            return "密码错误"
    else:
        response.status_code = 231
        return "用户名不存在"


@login.post("/login_access", summary="用户登录，返回token")
async def user_login_access(response: Response, item: OAuth2PasswordRequestForm = Depends()):
    sql_result = user.get_password(item.username)
    # 将数据库查询结果转换为字典列表
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    # 确认用户存在
    if user.confirm_user(item.username):
        # 确认密码是否正确
        if verify_password(item.password, data[0]["password"]):
            response.status_code = status.HTTP_200_OK
            sql_result = user.get_user(item.username)
            # 提取用户资料字典
            data = [dict(zip(result.keys(), result)) for result in sql_result]
            data_node = data[0]
            data_node["username"] = item.username
            # 打包token并返回
            return {"access_token": create_access_token(data_node), "token_type": "bearer"}
        else:
            response.status_code = 230
            return "密码错误"
    else:
        response.status_code = 231
        return "用户名不存在"


@login.post("/login_get_user", summary="根据token返回用户信息")
async def user_get_token(token: str = Depends(oauth2_scheme)):
    # 解码token
    sql_result = get_current_user(token)
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


@login.post("/register", summary="用户注册")
async def user_register(item: RegisterItem, response: Response):
    # 确认格式
    if not item.password == item.check_pass:
        response.status_code = 234
        return "两次密码输入不一致"
    if len(item.password) > 16:
        response.status_code = 230
        return "密码长度大于16位"
    if len(item.password) < 6:
        response.status_code = 231
        return "密码长度小于6位"
    # 用户名查重
    if user.confirm_user(item.username):
        response.status_code = 232
        return "用户名重复"
    else:
        # 加密密码并保存
        item.password = get_password_hash(item.password)
        if user.insert(item.username, item.password, item.ID, item.IDNAME):
            return "插入成功"
        else:
            response.status_code = 233
            return "插入失败"
