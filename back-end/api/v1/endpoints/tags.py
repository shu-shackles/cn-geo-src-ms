from fastapi import APIRouter
from pydantic import BaseModel
import json

from models import tag
from models.location import coords_to_city

tags = APIRouter(tags=["标点相关"])


class TagsUploadItem(BaseModel):
    type: int
    uid: int
    time: str
    lng: float
    lat: float
    etype: int
    title: str
    desc: str
    imgSrc: str


class TagsGetAreaInformal(BaseModel):
    area: str


class TagsGetArea(BaseModel):
    area: str


class TagAudit(BaseModel):
    eid: int
    auditStatus: int


@tags.post("/upload", summary="上传标记")
async def tag_upload(item: TagsUploadItem):
    if item.type == 1:
        if tag.tag_upload("A1", item.uid, item.time, item.lng, item.lat, item.etype,
                          item.title, item.desc, item.imgSrc):
            return "不需审核，添加成功"
        else:
            return "不需审核，添加失败"
    else:
        if item.type == 2:
            if tag.tag_upload_informal("A1", item.uid, item.time, item.lng, item.lat, item.etype,
                                       item.title, item.desc, item.imgSrc):
                return "需要审核，添加成功"
            else:
                return "需要审核，添加失败"
        else:
            return "人员权限错误"


@tags.get("/areainformaltags/:area", summary="区域未审核标记")
async def tag_area_informal(item: TagsGetAreaInformal):
    sql_result = tag.tag_get_area_informal(item.area)
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    for data_node in data:
        data_node["area"] = coords_to_city(data_node["lng"], data_node["lat"])
    result = json.dumps(data)
    return result


@tags.get("/areatags/:area", summary="区域已审核标记")
async def tag_area(item: TagsGetArea):
    sql_result = tag.tag_get_area(item.area)
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    for data_node in data:
        data_node["area"] = coords_to_city(data_node["lng"], data_node["lat"])
    result = json.dumps(data)
    return result


@tags.post('/finishaudit/{area}', summary="审核标记结果")
async def tag_audit(item: TagAudit, area):
    if not tag.tag_area_exist(item.eid, area):
        return "区域内不存在此标记"
    if item.auditStatus == -1:
        if tag.tag_delete_informal(item.eid):
            return "审核不通过，删除成功"
        else:
            return "审核不通过，删除失败"
    else:
        if item.auditStatus == 1:
            sql_result = tag.tag_get_eid_informal(item.eid)
            data_list = [dict(zip(result.keys(), result)) for result in sql_result]
            data = data_list[0]
            if tag.tag_upload(data['area'], data['uid'], data['time'], data['lng'], data['lat'], data['etype'],
                              data['title'], data['desc'], data['imgSrc']) and tag.tag_delete_informal(item.eid):
                return "审核通过，插入成功"
            else:
                return "审核通过，插入失败"
        else:
            return "审核标志位错误"
