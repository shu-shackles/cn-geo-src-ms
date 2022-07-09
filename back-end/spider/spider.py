# coding:utf-8
import requests
import re
import os
import urllib
import http.cookiejar
import ssl

width = 300
height = 300


def get_picurl_images(fname):
    patt = r'/images/(.*?).(jpg|jpeg|png|gif)'  # 利用正则匹配出图片url
    repatt = re.compile(patt)
    resutle = []  # 定义空列表存储图片url

    with open('../%s' % fname, 'r', encoding='utf-8') as fobj:  # 打开爬取的数据
        for line in fobj:  # 循环读取爬取的数据
            data = repatt.search(line)  # 进行正则
            if data:
                print(data)
                resutle.append('http://news.shu.edu.cn%s' % data.group())
    return resutle


def get_picurl_local(fname):
    patt = r'/__local/(.*?).(jpg|jpeg|png|gif)'  # 利用正则匹配出图片url
    repatt = re.compile(patt)
    resutle = []  # 定义空列表存储图片url

    with open('../%s' % fname, 'r', encoding='utf-8') as fobj:  # 打开爬取的数据
        for line in fobj:  # 循环读取爬取的数据
            data = repatt.search(line)  # 进行正则
            if data:
                resutle.append('http://news.shu.edu.cn%s' % data.group())
    return resutle


def get_web(url, fname):
    r = requests.get(url)  # 返回url请求的数据
    data = r.content
    with  open(fname, 'wb') as fobj:  # 将数据存储在指定位置
        fobj.write(data)

    return fname


def download_image(url, dir):
    pic_dir = dir  # 创建存储图片的文件夹
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)

    for pic_url in url:  # 循环读取读取出来的图片url
        pic_name = pic_dir
        for src in pic_url.split('/')[4:]:
            pic_name = os.path.join(pic_name, src)
        try:
            get_web(pic_url, pic_name)  # 将图片url跟文件回传给get_web执行批量下载
        except:
            pass


def download_local(url, dir):
    pic_dir = dir  # 创建存储图片的文件夹
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)

    for pic_url in url:  # 循环读取读取出来的图片url
        pic_name = pic_dir
        pic_name_dir = pic_name
        for src in pic_url.split('/')[4:]:
            pic_name = os.path.join(pic_name, src)
        for src in pic_url.split('/')[4:-1]:
            pic_name_dir = os.path.join(pic_name_dir, src)
            if not os.path.exists(pic_name_dir):
                os.mkdir(pic_name_dir)
        # print(pic_url)
        try:
            get_web(pic_url, pic_name)
        except:
            print('failed')


# 获取新闻的发行时间、链接、标题
def get_news_title():
    url = 'http://mnr.gov.cn/dt/ywbb/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    print(html)
    # chapter_info_list获取所有新闻的日期、地址、标题
    chapter_info_list = re.findall(r'<li><span>(.*?)</span><a href="(.*?)" target="_blank">(.*?)</a></li>', html, re.S)
    # 将网站信息改为list
    chapter_info_list = list(map(list, chapter_info_list))
    # 对地址奇怪的新闻进行清洗，并将相对地址改为绝对地址
    for i in range(len(chapter_info_list) - 1, -1, -1):
        if not chapter_info_list[i][1].startswith("./"):
            chapter_info_list.pop(i)
        else:
            chapter_info_list[i][1] = "http://mnr.gov.cn/dt/ywbb/" + chapter_info_list[i][1][2:]

    return chapter_info_list


# 输入一个url，返回该网址的正文
def get_main_article(chapter_url):
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'

    # chapter_html是这个新闻中的html文本
    chapter_html = chapter_response.text
    # 获取正文
    main_article = re.findall(r'[\u4e00-\u9fa5\d，。：“”；：？！（）]{25,}', chapter_html)
    if len(main_article) == 0:
        raise Exception("url error")
    result = "  " + main_article[0]
    if len(main_article) > 1:
        for i in range(1, len(main_article)):
            if not main_article[i].isdigit():
                result += "\n  " + main_article[i]

    # 图片获取部分，主要是二维码
    """picurl1 = get_picurl_images('%s.txt' % title)
    picurl2 = get_picurl_local('%s.txt' % title)
    download_image(picurl1, '..\\..\\..\\images')
    download_local(picurl2, '..\\__local')"""

    return result


# 输入关键字、数量、页数，返回前page页的num个包含关键字的新闻相关内容，以列表形式返回(列表长度<=num)
def get_news_by_province(key, nums, pages):
    # 网站主页的url
    base_url = "http://www.zgdztk.com/"
    # 新闻列表url
    url = 'http://mnr.gov.cn/dt/ywbb/'

    result = []

    for page in range(1, pages + 1):
        url = "http://www.zgdztk.com/news_list-1.asp?page=" + str(page) + "&bh=2&sh="
        response = requests.get(url)
        response.encoding = 'gbk'
        html = response.text

        # chapter_info_list获取所有新闻的日期、地址、标题
        chapter_info_list = re.findall(
            r'<TD align=left width=600><a href="(.*?)" target="_blank" title="(.*?)">(.*?)'
            r'</a></TD>\r\n                                          (.*?)</TD>', html,
            re.S)
        # 将网站信息改为list
        chapter_info_list = list(map(list, chapter_info_list))
        # 对地址奇怪的新闻进行清洗，并将相对地址改为绝对地址
        for i in range(len(chapter_info_list)):
            if chapter_info_list[i][1].find(key) != -1:
                # 先获取新闻首段
                firstParagraph = get_main_article_from_geological_survey(base_url + chapter_info_list[i][0], True)
                # 记录标题、新闻首段、url、发布日期(有时候首段格式奇怪，就跳过)
                if firstParagraph:
                    result.append([chapter_info_list[i][1], firstParagraph, base_url + chapter_info_list[i][0],
                                   chapter_info_list[i][3][14:]])
                if len(result) >= nums:
                    return result

    return result


def get_main_article_from_geological_survey(url, firstParagraph=False):
    chapter_response = requests.get(url)
    chapter_response.encoding = 'gbk'

    # chapter_html是这个新闻中的html文本
    chapter_html = chapter_response.text
    # 获取正文
    main_article = re.findall(r'2;">&nbsp; &nbsp; &nbsp; &nbsp;(.*?)</span><br />', chapter_html)
    # 如果无匹配，返回False
    if len(main_article) == 0:
        return False
    # 要求只返回前部分内容
    elif firstParagraph:
        # 将其中的"与<>内容删除
        firstSentence = re.sub('\<.*?\>', '', main_article[0])
        return firstSentence.replace('"', '\\"')[:20]
    result = "  " + main_article[0]

    # 返回数据
    if len(main_article) > 1:
        for i in range(1, len(main_article)):
            if not main_article[i].isdigit():
                result += "\n  " + main_article[i]

    # 图片获取部分
    """picurl1 = get_picurl_images('%s.txt' % title)
    picurl2 = get_picurl_local('%s.txt' % title)
    download_image(picurl1, '..\\..\\..\\images')
    download_local(picurl2, '..\\__local')"""

    return result


if __name__ == "__main__":
    print(get_news_by_province("山东", 2, 1))
