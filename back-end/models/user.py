# from typing import Optional, Iterable
#
# from tortoise import Model, BaseDBAsyncClient
# from tortoise import fields
#
# from core import get_password_hash
#
#
# class Users(Model):
#     uid = fields.IntField(max_length=10, null=False, description="用户id")
#     name = fields.CharField(max_length=20, null=False, description="用户名称")
#     password = fields.CharField(max_length=128, null=False, description="密码")
#     type = fields.IntField(max_length=1, null=False, description="权限等级")
#     area = fields.CharField(max_length=5, null=True, description="地区")
#
#     async def save(
#         self,
#         using_db: Optional[BaseDBAsyncClient] = None,
#         update_fields: Optional[Iterable[str]] = None,
#         force_create: bool = False,
#         force_update: bool = False,
#     ) -> None:
#         if force_create or "password" in update_fields:
#             self.password = get_password_hash(self.password)
#         await super(Users, self).save(using_db, update_fields, force_create, force_update)
from models.db import con


def confirm_user(name):
    sql_result = con.execute(f'select uid from users where name=\'{name}\'')
    if sql_result.all():
        return True
    else:
        return False


def is_password(name, password):
    sql_result = con.execute(f'select uid from users where name=\'{name}\' and password = \'{password}\'')
    if sql_result.all():
        return True
    else:
        return False


def insert(name, password, _id, id_name):
    con.execute(f'insert into users(name, password, type, ID, IDNAME) values(\'{name}\', \'{password}\', 2 ,\'{_id}\','
                f' \'{id_name}\')')
    sql_result = con.execute(f'select uid from users where name=\'{name}\' and password= \'{password}\'')
    if sql_result.all():
        return True
    else:
        return False


def user_info(offset, count):
    return con.execute(f'select * from users limit {offset}, {count}')


def user_setinfotype(_type, uid):
    con.execute(f'UPDATE users SET type = \'{_type}\' WHERE uid = {uid}')
    sql_result = con.execute(f'select * from users where uid = {uid} and type = \'{_type}\'')
    if sql_result.all():
        return True
    else:
        return False


def user_setinfopassword(password, uid):
    con.execute(f'UPDATE users SET password = \'{password}\' WHERE uid = {uid}')
    sql_result = con.execute(f'select * from users where password = \'{password}\' and uid = {uid}')
    if sql_result.all():
        return True
    else:
        return False


def user_setinfoarea(area, uid):
    con.execute(f'UPDATE users SET AREA = \'{area}\'  WHERE uid = {uid}')
    sql_result = con.execute(f'select * from users where area=\'{area}\'and uid = {uid}')
    if sql_result.all():
        return True
    else:
        return False


def user_delete(uid):
    con.execute(f'delete from users where uid = {uid}')
    sql_result = con.execute(f'select * from users where uid= {uid}')
    if sql_result.all():
        return False
    else:
        return True


def user_all():
    return con.execute(f'select * from users')
