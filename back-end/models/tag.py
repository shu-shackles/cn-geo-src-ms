from models.db import con


def tag_upload(area, uid, time,  lng, lat, etype, title, desc, imgSrc):
  con.execute(f'insert into tags (area, uid, lng, lat, title, "desc", etype, "time", imgSrc) '
              f'values (\'{area}\', {uid}, {lng}, {lat}, \'{title}\', \'{desc}\', {etype}, \'{time}\', \'{imgSrc}\')')
  sql_result=con.execute(f'select * from tags where area = \'{area}\' and uid = {uid} and lng = {lng} and lat = {lat} '
                         f'and title =\'{title}\' and desc = \'{desc}\' and etype = {etype} and time = \'{time}\' and '
                         f'imgSrc = \'{imgSrc}\'')
  if sql_result.all():
    return True
  else:
    return False


def tag_upload_informal(area, uid, time,  lng, lat, etype, title, desc, imgSrc):
  con.execute(f'insert into informal_tags (area, uid, lng, lat, title, "desc", etype, "time", imgSrc) '
              f'values (\'{area}\', {uid}, {lng}, {lat}, \'{title}\', \'{desc}\', {etype}, \'{time}\', \'{imgSrc}\')')
  sql_result = con.execute(
    f'select * from informal_tags where area = \'{area}\' and uid = {uid} and lng = {lng} and lat = {lat} '
    f'and title =\'{title}\' and desc = \'{desc}\' and etype = {etype} and time = \'{time}\' and '
    f'imgSrc = \'{imgSrc}\'')
  if sql_result.all():
    return True
  else:
    return False
