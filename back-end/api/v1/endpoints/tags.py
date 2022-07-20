from fastapi import APIRouter, Depends
from pydantic import BaseModel

from core.security import oauth2_scheme
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


# class TagsGetAreaInformal(BaseModel):
#     area: str
#
#
# class TagsGetArea(BaseModel):
#     area: str


class TagAudit(BaseModel):
    eid: int
    auditStatus: int


@tags.post("/upload", summary="上传标记")
async def tag_upload(item: TagsUploadItem):
    loc = coords_to_city(item.lng, item.lat)
    if loc.startswith("黑龙江"):
        loc = "黑龙江"
    else:
        if loc.startswith("内蒙古"):
            loc = "内蒙古"
        else:
            loc = f'{loc[0]}{loc[1]}'
    if item.type == 1:
        if tag.tag_upload(loc, item.uid, item.time, item.lng, item.lat, item.etype,
                          item.title, item.desc, item.imgSrc):
            return "不需审核，添加成功"
        else:
            return "不需审核，添加失败"
    else:
        if item.type == 2:
            if tag.tag_upload_informal(loc, item.uid, item.time, item.lng, item.lat,
                                       item.etype, item.title, item.desc, item.imgSrc):
                return "需要审核，添加成功"
            else:
                return "需要审核，添加失败"
        else:
            return "人员权限错误"


@tags.post("/areainformaltags/{area}", summary="区域未审核标记")
async def tag_area_informal(area, token: str = Depends(oauth2_scheme)):
    if area == "全部":
        area = ""
    sql_result = tag.tag_get_area_informal(area)
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


@tags.post("/areatags/{area}", summary="区域已审核标记")
async def tag_area(area):
    if area == "全部":
        area = ""
    sql_result = tag.tag_get_area(area)
    data = [dict(zip(result.keys(), result)) for result in sql_result]
    return data


@tags.post('/finishaudit', summary="审核标记结果")
async def tag_audit(item: TagAudit):
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
