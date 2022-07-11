from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.db import con

mineral = APIRouter(tags=["矿产资源"])


# 按列表方式返回所有数据
@mineral.get("/mineralAll", summary="所有矿产数据")
def get_all():
    sql_result = con.execute(f'SELECT * FROM mineral_resources')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


# 根据获取到的省份名称返回对应数据
@mineral.get("/mineralProvince", summary="省市矿产数据")
def get_single(province):
    sql_result = con.execute(
        f'SELECT * FROM mineral_resources WHERE province=\'{province}\'')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


# 根据获取到的资源名称返回对应数据
@mineral.get("/mineralType", summary="指定矿产数据")
def get_type(type):
    sql_result = con.execute(
        f'SELECT province, `{type}` as "value" FROM mineral_resources ORDER BY ABS(`{type}`) DESC')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


# coal(100M tons)


# sql_result = con.execute(f'SELECT * FROM mineral_resources')
# data_list = sql_result.all()
# result1 = []
# result2 = []
# for data in data_list:
#     result1.append(data[0])
#     result2.append(data[type])
# result3 = list(zip(result1, result2))
# return result3
