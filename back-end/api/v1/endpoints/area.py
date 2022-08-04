from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.db import con

area = APIRouter(tags=["区域"])

# 按列表方式返回所有区域
@area.get("/areas", summary="区域划分")
def get_all():
    sql_result = con.execute(f'SELECT * FROM areas')
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data

# 确定区域信息
def confirm_area(area):
    sql_result = con.execute(f'SELECT * FROM areas WHERE area=\'{area}\'')
    if sql_result.all():
        return True
    else:
        return False

# 新增区域
@area.post("/areaAdd", summary="新增区域")
def add_area(area, lng, lat):
    if confirm_area(area):
        return "区域名重复"
    else:
        con.execute(
            f'INSERT INTO areas (area, lng, lat) VALUES (\'{area}\', {lng}, {lat})')
        sql_result = con.execute(
            f'SELECT * FROM areas WHERE area = \'{area}\' AND lng = {lng} AND lat = {lat}')
        if sql_result.all():
            return "增加成功"
        else:
            return "增加失败"

# 修改区域
@area.put("/areaEdit", summary="修改区域信息")
def edit_area(area, lng, lat):
    if confirm_area(area):
        con.execute(f'UPDATE areas SET lng={lng}, lat={lat} WHERE area=\'{area}\'')
        sql_result = con.execute(
            f'SELECT * FROM areas WHERE area = \'{area}\' AND lng = {lng} AND lat = {lat}')
        if sql_result.all():
            return "修改成功"
        else:
            return "修改失败"
    else:
        return "区域不存在"

# 删除区域
@area.delete("/areaDelete", summary="删除区域信息")
def delete_area(area):
    if confirm_area(area):
        con.execute(f'DELETE FROM areas WHERE area=\'{area}\'')
        sql_result = con.execute(f'SELECT * FROM areas WHERE area=\'{area}\'')
        if sql_result.all():
            return "删除失败"
        else:
            return "删除成功"
    else:
        return "区域不存在"

