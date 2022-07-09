from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.db import con

forest = APIRouter(tags=["森林资源"])


@forest.get("/forestAll", summary="所有森林数据")
def get_all():
    sql_result = con.execute(f'select * from forest')
    return sql_result.all()


@forest.get("/forestSingle", summary="单条森林数据")
def get_single(province):
    sql_result = con.execute(
        f'select * from forest where `province/company`=\'{province}\'')
    return sql_result.all()