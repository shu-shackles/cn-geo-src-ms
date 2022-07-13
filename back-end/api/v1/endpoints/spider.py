import os
from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
import uvicorn
import json
from fastapi import Depends, FastAPI, HTTPException

from models.spider import get_main_article, get_news_by_key_word

spider = APIRouter(tags=["爬虫"])


# 输入关键字、数量、页数，返回前page页的num个包含关键字的新闻相关内容，以列表形式返回(列表长度<=num)
@spider.get("/news/geological_survey")
def get_news_from_geological_survey(key: str, nums: int, pages: int):
    result = ""
    # 调用爬虫函数，获取新闻列表
    newsList = get_news_by_key_word(key, nums, pages)
    first = True

    # 转换为json格式返回
    for news in newsList:
        if first:
            first = False
        else:
            result += ",\n"
        result += '{\n"title": "' + news[0]
        result += '",\n"first paragraph": "' + news[1]
        result += '",\n"url": "' + news[2]
        result += '",\n"date": "' + news[3] + '"\n}'
    result = '[' + result + ']'
    result = json.loads(result)
    return result


# 传入某个新闻的url地址，返回其正文(之后还会返回图片)
@spider.get("/news/Chinese geography/{chapter_url:path}")
def get_article_and_picture(chapter_url: str):
    main_article = get_main_article(chapter_url)
    result = "{"+'"main_article": "'+main_article+'"}'
    result = json.loads(result)
    return result
