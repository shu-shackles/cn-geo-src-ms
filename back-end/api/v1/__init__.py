from fastapi import APIRouter

from .endpoints import *

v1 = APIRouter(prefix="/v1")

v1.include_router(login)
v1.include_router(users)
v1.include_router(tags)

v1.include_router(area)
v1.include_router(forest)
v1.include_router(mineral)
