from fastapi import APIRouter

user = APIRouter(tags=["用户相关"])


@user.get("/user", summary="当前用户")
async def user_info():
    pass


@user.put("/user", summary="修改信息")
async def user_update():
    pass
