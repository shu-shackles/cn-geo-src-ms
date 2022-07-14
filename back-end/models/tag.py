from models.db import con


def tag_upload(area, uid, time, lng, lat, etype, title, desc, imgSrc):
    con.execute(f'insert into tags (area, uid, lng, lat, title, `desc`, etype, time, imgSrc) '
                f'values (\'{area}\', {uid}, {lng}, {lat}, \'{title}\', \'{desc}\', {etype}, \'{time}\', \'{imgSrc}\')')
    sql_result = con.execute(
        f'select * from tags where area = \'{area}\' and uid = {uid} and lng = {lng} and lat = {lat} '
        f'and title =\'{title}\' and `desc` = \'{desc}\' and etype = {etype} and time = \'{time}\' and '
        f'imgSrc = \'{imgSrc}\'')
    if sql_result.all():
        return True
    else:
        return False


def tag_upload_informal(area, uid, time, lng, lat, etype, title, desc, imgSrc):
    con.execute(f'insert into informal_tags (area, uid, lng, lat, title, `desc`, etype, time, imgSrc) '
                f'values (\'{area}\', {uid}, {lng}, {lat}, \'{title}\', \'{desc}\', {etype}, \'{time}\', \'{imgSrc}\')')
    sql_result = con.execute(
        f'select * from informal_tags where area = \'{area}\' and uid = {uid} and lng = {lng} and lat = {lat} '
        f'and title =\'{title}\' and `desc` = \'{desc}\' and etype = {etype} and time = \'{time}\' and '
        f'imgSrc = \'{imgSrc}\'')
    if sql_result.all():
        return True
    else:
        return False


def tag_get_area(area):
    return con.execute(f'select area, uid, lng, lat, title, tags.`desc`, eventype.`desc`, time, imgSrc '
                       f'from tags,eventype where area like \'{area}%%\' and tags.etype = eventype.etype')


def tag_get_area_informal(area):
    return con.execute(f'select area, uid, lng, lat, title, informal_tags.`desc`, eventype.`desc`, time, imgSrc '
                       f'from informal_tags,eventype where area like \'{area}%%\' '
                       f'and informal_tags.etype = eventype.etype')


def tag_delete_informal(eid):
    con.execute(f'delete from informal_tags where eid = {eid}')
    sql_result = con.execute(f'select * from informal_tags where eid = {eid}')
    if sql_result.all():
        return False
    else:
        return True


def tag_area_exist(eid, area):
    sql_result = con.execute(f'select * from informal_tags where eid = {eid} and area like \'{area}\'%%')
    if sql_result.all():
        return True
    else:
        return False


def tag_get_eid_informal(eid):
    return con.execute(f'select * from informal_tags where eid = {eid} ')
