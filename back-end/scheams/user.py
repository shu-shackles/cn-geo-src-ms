from tortoise.contrib.pydantic import pydantic_model_creator
from models import User

User_Pydantic = pydantic_model_creator(User, name="Users", exclude=('password',))
UserIn_Pydantic = pydantic_model_creator(User, name="UsersIn")
