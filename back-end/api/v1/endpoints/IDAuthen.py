from fastapi import APIRouter
from models.IDAuthen import idMatches

import json

IDAuthen = APIRouter(tags=["身份匹配"])

@IDAuthen.get("/IDAuthen")
def mathches_ID_and_names(cardID, realName):
  result = idMatches(cardID, realName)
  result = '{\n"result": "'+result+'"\n}'
  result = json.loads(result)
  return result
