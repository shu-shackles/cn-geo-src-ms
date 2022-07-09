import os
from typing import List

from uvicorn import run
# from api import app
import uvicorn
import json
from fastapi import Depends, FastAPI, HTTPException

from spider.spider import get_news_title, get_main_article, get_news_by_province

app = FastAPI()


# 获取新闻的发布日期、url地址、标题
@app.get("/new/Chinese_geography")
def get_news_list():
    result = ""
    # 调用爬虫函数，获取新闻列表
    newsList = get_news_title()
    first = True

    # 转换为json格式返回
    for news in newsList:
        if first:
            first = False
        else:
            result += ",\n"
        result += '{\n"date": "' + news[0]
        result += '",\n"url": "' + news[1]
        result += '",\n"title": "' + news[2] + '"\n}'
    result = '[' + result + ']'
    result = json.loads(result)
    return result


# 传入某个新闻的url地址，返回其正文(之后还会返回图片)
@app.get("/news/Chinese geography/{chapter_url:path}")
def get_article_and_picture(chapter_url: str):
    main_article = get_main_article(chapter_url)
    return main_article


# 输入关键字、数量、页数，返回前page页的num个包含关键字的新闻相关内容，以列表形式返回(列表长度<=num)
@app.get("/news/geological_survey")
def get_news_from_geological_survey(key: str, nums: int, pages: int):
    result = ""
    # 调用爬虫函数，获取新闻列表
    newsList = get_news_by_province(key, nums, pages)
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


if __name__ == '__main__':
    run('main:app', reload=True)
