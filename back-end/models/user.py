from typing import Optional, Iterable

from tortoise import Model, BaseDBAsyncClient
from tortoise import fields

from core import get_password_hash


class User(Model):
    uid = fields.CharField(max_length=10, null=False, description="用户id")
    username = fields.CharField(max_length=20, null=False, description="用户名称")
    password = fields.CharField(max_length=128, null=False, description="密码")
    type = fields.CharField(max_length=1, null=False, description="权限等级")
    area = fields.CharField(max_length=5, null=True, description="地区")

    async def save(
        self,
        using_db: Optional[BaseDBAsyncClient] = None,
        update_fields: Optional[Iterable[str]] = None,
        force_create: bool = False,
        force_update: bool = False,
    ) -> None:
        if force_create or "password" in update_fields:
            self.password = get_password_hash(self.password)
        await super(User, self).save(using_db, update_fields, force_create, force_update)