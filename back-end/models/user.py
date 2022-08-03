from models.db import con


# 查询用户名是否存在
def confirm_user(name):
    sql_result = con.execute(f'select uid from users where name=\'{name}\'')
    if sql_result.all():
        return True
    else:
        return False


# 获取数据库中的哈希密码
def get_password(name):
    sql_result = con.execute(f'select password from users where name=\'{name}\'')
    return sql_result


# 根据用户名获取用户信息
def get_user(name):
    sql_result = con.execute(f'select * from users where name=\'{name}\'')
    return sql_result


# 根据用户名获取用户信息（支持模糊查询）
def user_info_name(name):
    sql_result = con.execute(f'select * from users where name like \'%%{name}%%\'')
    return sql_result


# 根据uid获取哈希密码
def get_password_uid(uid):
    sql_result = con.execute(f'select password from users where uid = {uid}')
    return sql_result


# 插入新用户
def insert(name, password, _id, id_name):
    con.execute(f'insert into users(name, password, type, ID, IDNAME) values(\'{name}\', \'{password}\', \'2\', '
                f'\'{_id}\', \'{id_name}\')')
    # 检查插入是否成功
    sql_result = con.execute(f'select uid from users where name=\'{name}\' and password= \'{password}\'')
    if sql_result.all():
        return True
    else:
        return False


# 按行查询用户表
def user_info(offset, count):
    return con.execute(f'select * from users limit {offset}, {count}')


# 修改用户信息
def user_setinfo(_type, password, area, uid):
    con.execute(f'UPDATE users SET type = \'{_type}\',password = \'{password}\',area = \'{area}\' WHERE uid = {uid}')
    sql_result = con.execute(f'select * from users where uid = {uid} and type = \'{_type}\' and '
                             f'password = \'{password}\' and area=\'{area}\'')
    if sql_result.all():
        return True
    else:
        return False


# 修改用户类型
def user_setinfotype(_type, uid):
    con.execute(f'UPDATE users SET type = \'{_type}\' WHERE uid = {uid}')
    sql_result = con.execute(f'select * from users where uid = {uid} and type = \'{_type}\'')
    if sql_result.all():
        return True
    else:
        return False


# 修改用户密码
def user_setinfopassword(password, uid):
    con.execute(f'UPDATE users SET password = \'{password}\' WHERE uid = {uid}')
    sql_result = con.execute(f'select * from users where password = \'{password}\' and uid = {uid}')
    if sql_result.all():
        return True
    else:
        return False


# 修改用户地区
def user_setinfoarea(area, uid):
    con.execute(f'UPDATE users SET AREA = \'{area}\'  WHERE uid = {uid}')
    sql_result = con.execute(f'select * from users where area=\'{area}\'and uid = {uid}')
    if sql_result.all():
        return True
    else:
        return False


# 删除用户
def user_delete(uid):
    con.execute(f'delete from users where uid = {uid}')
    sql_result = con.execute(f'select * from users where uid= {uid}')
    if sql_result.all():
        return False
    else:
        return True


# 查询所有用户
def user_all():
    return con.execute(f'select * from users')
