from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.db import con

forest = APIRouter(tags=["森林资源"])


# 按照森林覆盖率从高到低按列表方式返回所有数据
@forest.get("/forestAll", summary="所有森林数据")
def get_all():
    sql_result = con.execute(
        f'SELECT * FROM forest ORDER BY ABS(`forest coverage`) DESC')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


# 根据获取到的省份名称返回对应数据
@forest.get("/forestProvince", summary="省市森林数据")
def get_single(province):
    sql_result = con.execute(
        f'SELECT * FROM forest WHERE `province/company`=\'{province}\'')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


# 根据获取到的资源名称返回对应数据，按资源量降序排列
@forest.get("/forestType", summary="指定森林数据")
def get_type(type):
    sql_result = con.execute(
        f'SELECT `province/company`, `{type}` as "value" FROM forest ORDER BY ABS(`{type}`) DESC')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data