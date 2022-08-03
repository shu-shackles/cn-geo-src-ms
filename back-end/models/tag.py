from models.db import con


# 处理字符串%
def change_desc(desc: str):
    desc_list = list(desc)
    i = 0
    while i < len(desc_list):
        if desc_list[i] == '%':
            desc_list.insert(i, '%')
            i = i+1
        i = i+1
    desc = ''.join(desc_list)
    return desc


# 上传到已审核表
def tag_upload(area, uid, time, lng, lat, etype, title, desc, imgSrc):
    con.execute(f'insert into tags (area, uid, lng, lat, title, `desc`, etype, time, imgSrc) '
                f'values (\'{area}\', {uid}, {lng}, {lat}, \'{title}\', \'{desc}\', \'{etype}\', \'{time}\', \'{imgSrc}\')')
    # 检验数据库中是否存在
    sql_result = con.execute(
        f'select * from tags where area = \'{area}\' and uid = {uid} and lng = {lng} and lat = {lat} '
        f'and title =\'{title}\' and `desc` = \'{desc}\' and etype = \'{etype}\' and time = \'{time}\' and '
        f'imgSrc = \'{imgSrc}\'')
    if sql_result.all():
        return True
    else:
        return False


# 上传到待审核表
def tag_upload_informal(area, uid, time, lng, lat, etype, title, desc, imgSrc):
    con.execute(f'insert into informal_tags (area, uid, lng, lat, title, `desc`, etype, time, imgSrc) '
                f'values (\'{area}\', {uid}, {lng}, {lat}, \'{title}\', \'{desc}\', \'{etype}\', \'{time}\', \'{imgSrc}\')')
    # 检验数据库中是否存在
    sql_result = con.execute(
        f'select * from informal_tags where area = \'{area}\' and uid = {uid} and lng = {lng} and lat = {lat} '
        f'and title =\'{title}\' and `desc` = \'{desc}\' and etype = \'{etype}\' and time = \'{time}\' and '
        f'imgSrc = \'{imgSrc}\'')
    if sql_result.all():
        return True
    else:
        return False


# 查询区域内已审核标记
def tag_get_area(area):
    return con.execute(f'select eid, area, uid, lng, lat, title, tags.`desc` as "tag_sesc", eventype.`desc` '
                       f'as "enentype", time, imgSrc from tags,eventype where area like \'{area}%%\' '
                       f'and tags.etype = eventype.etype')


# 查询区域内未审核标记
def tag_get_area_informal(area):
    return con.execute(f'select eid, area, uid, lng, lat, title, informal_tags.`desc` as "tag_sesc", eventype.`desc` as '
                       f'"enentype", time, imgSrc from informal_tags,eventype where area like \'{area}%%\' and '
                       f'informal_tags.etype = eventype.etype')


# 删除未审核标记（用于审核过程）
def tag_delete_informal(eid):
    con.execute(f'delete from informal_tags where eid = {eid}')
    # 检验数据库中是否存在
    sql_result = con.execute(f'select * from informal_tags where eid = {eid}')
    if sql_result.all():
        return False
    else:
        return True


# 查询某区域内一标记是否存在
def tag_area_exist(eid, area):
    sql_result = con.execute(f'select * from informal_tags where eid = {eid} and area like \'{area}\'%%')
    if sql_result.all():
        return True
    else:
        return False


# 查询某标记是否待审核
def tag_get_eid_informal(eid):
    return con.execute(f'select * from informal_tags where eid = {eid} ')
