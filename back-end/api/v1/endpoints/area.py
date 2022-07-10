from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.db import con

area = APIRouter(tags=["区域"])

# 按列表方式返回所有区域
@area.get("/areas", summary="区域划分")
def get_all():
    sql_result = con.execute(f'SELECT * FROM areas')
    return sql_result.all()

# 确定区域信息
def confirm_area(area):
    sql_result = con.execute(f'select * from areas where area=\'{area}\'')
    if sql_result.all():
        return True
    else:
        return False

# 新增区域
@area.post("areaAdd", summary="新增区域")
def add_area(area, lng, lat):
    if confirm_area(area):
        return "区域名重复"
    else:
        con.execute(
            f'insert into areas (area, lng, lat) values (\'{area}\', {lng}, {lat})')
        sql_result = con.execute(
            f'select * from areas where area = \'{area}\' and lng = {lng} and lat = {lat}')
        if sql_result.all():
            return "增加成功"
        else:
            return "增加失败"

# 修改区域
@area.put("areaEdit", summary="修改区域信息")
def edit_area(area, lng, lat):
    if confirm_area(area):
        con.execute(f'UPDATE areas SET lng={lng}, lat={lat} WHERE area=\'{area}\'')
        sql_result = con.execute(
            f'select * from areas where area = \'{area}\' and lng = {lng} and lat = {lat}')
        if sql_result.all():
            return "修改成功"
        else:
            return "修改失败"
    else:
        return "区域不存在"

# 根据获取到的区域名称按列表方式返回区域内所有点位
@area.get("/boundaries", summary="区域内点位")
def get_single(Area):
    sql_result = con.execute(
        f'SELECT lng, lat FROM boundaries WHERE area=\'{Area}\' ORDER BY `order`')
    return sql_result.all()
