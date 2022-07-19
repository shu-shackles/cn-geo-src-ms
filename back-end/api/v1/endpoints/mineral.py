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


@mineral.get("/mineralHistory", summary="历史矿产数据")
def get_type():
    sql_result = con.execute(
        f'SELECT `ore` AS "name", ABS(`2011`) AS "2011", ABS(`2012`) AS "2012", ABS(`2013`) AS "2013", ABS(`2014`) AS "2014",'
        f'ABS(`2015`) AS "2015", ABS(`2016`) AS "2016", ABS(`2017`) AS "2017", ABS(`2018`) AS "2018", ABS(`2019`) AS "2019"'
        f'FROM mineral_history')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


@mineral.get("/mineralTypeHistory", summary="指定矿产历史数据")
def get_type(type):
    sql_result = con.execute(
        f'SELECT `ore` AS "name", ABS(`2011`) AS "2011", ABS(`2012`) AS "2012", ABS(`2013`) AS "2013", ABS(`2014`) AS "2014",'
        f'ABS(`2015`) AS "2015", ABS(`2016`) AS "2016", ABS(`2017`) AS "2017", ABS(`2018`) AS "2018", ABS(`2019`) AS "2019"'
        f'FROM mineral_history WHERE `ore`=\'{type}\'')
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
