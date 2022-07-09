from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.db import con

mineral = APIRouter(tags=["矿产资源"])


@mineral.get("/mineralAll", summary="所有矿产数据")
def get_all():
    sql_result = con.execute(f'select * from mineral_resources')
    return sql_result.all()


@mineral.get("/mineralSingle", summary="单条矿产数据")
def get_single(province):
    sql_result = con.execute(
        f'select * from mineral_resources where province=\'{province}\'')
    return sql_result.all()