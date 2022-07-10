from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.db import con

mineral = APIRouter(tags=["矿产资源"])


# 按列表方式返回所有数据
@mineral.get("/mineralAll", summary="所有矿产数据")
def get_all():
    sql_result = con.execute(f'SELECT * FROM mineral_resources')
    return sql_result.all()


# 根据获取到的省份名称按列表方式返回对应数据
@mineral.get("/mineralProvince", summary="省市矿产数据")
def get_single(province):
    sql_result = con.execute(
        f'SELECT * FROM mineral_resources WHERE province=\'{province}\'')
    return sql_result.all()
