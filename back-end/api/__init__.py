# import sys
from fastapi import FastAPI
# from tortoise.contrib.fastapi import register_tortoise

from .v1 import v1

app = FastAPI()

app.include_router(v1, prefix="/api")
#
# import logging
#
# fmt = logging.Formatter(
#   fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
#   datefmt="%Y-%m-%d %H:%M:%S",
# )
# sh = logging.StreamHandler(sys.stdout)
# sh.setLevel(logging.DEBUG)
# sh.setFormatter(fmt)
#
# # will print debug sql
# logger_db_client = logging.getLogger("tortoise.db_client")
# logger_db_client.setLevel(logging.DEBUG)
# logger_db_client.addHandler(sh)
#
# logger_tortoise = logging.getLogger("tortoise")
# logger_tortoise.setLevel(logging.DEBUG)
# logger_tortoise.addHandler(sh)
#
# # register_tortoise(
# #     app,
# #     db_url="postgres://gaussdb:Ina@12358046@101.43.100.126:15432/postgres",
# #     modules={"models": ["models"]},
# #     generate_schemas=True,
# #     add_exception_handlers=True,
# # )
#
# register_tortoise(
#   app,
#   db_url="mysql://summer:shanghaiSHU@122.9.130.89:3306/summer_db",
#   modules={"models": ["models"]},
#   generate_schemas=True,
#   add_exception_handlers=True,
# )
# 从sqlalchemy导入数据库引擎


