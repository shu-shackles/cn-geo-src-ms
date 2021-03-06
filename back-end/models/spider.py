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
def get_news_title_1(key, pages=""):
    url = 'http://mnr.gov.cn/dt/ywbb/'+pages
    base_url = 'http://mnr.gov.cn/dt/ywbb/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    result = []

    # chapter_info_list获取所有新闻的日期、地址、标题
    chapter_info_list = re.findall(r'<li><span>(.*?)</span><a href="(.*?)" target="_blank">(.*?)</a></li>', html, re.S)
    # 将网站信息改为list
    chapter_info_list = list(map(list, chapter_info_list))

    for i in range(len(chapter_info_list)):
        if chapter_info_list[i][2].find(key) == -1 or not chapter_info_list[i][1].startswith("./"):
            continue
        # 先获取新闻首段
        firstParagraph = get_main_article_1(base_url + chapter_info_list[i][1][2:], chapter_info_list[i][2], True)
        # 记录标题、新闻首段、url、发布日期(有时候首段格式奇怪，就跳过)
        if firstParagraph:
            result.append([chapter_info_list[i][2], firstParagraph, base_url + chapter_info_list[i][1][2:],
                          chapter_info_list[i][0][:]])

    return result


# 输入一个url，返回该网址的正文
def get_main_article_1(chapter_url, title, firstParagraph=False):
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'

    # chapter_html是这个新闻中的html文本
    chapter_html = chapter_response.text
    # 获取正文
    main_article = re.findall(r'[\u4e00-\u9fa5\d，。：“”；：？！（）]{30,}', chapter_html)
    if len(main_article) < 1:
        return False
    for i in range(1, len(main_article)):
        main_article[0] += main_article[i]
    if firstParagraph:
        while main_article[0].startswith(title):
            main_article[0] = main_article[0][len(title):]
        if len(main_article[0]) >= 50:
            return main_article[0][:50]
        if len(main_article[0]) >= 15:
            return main_article[0]
        return ""
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
    result = re.sub('\<.*?\>', '', result)
    result = result.replace('"', '\\"')
    return result


# 输入关键字、数量、页数，返回前page页的num个包含关键字的新闻相关内容，以列表形式返回(列表长度<=num)
def get_news_title_2(key, pages, num):
    # 网站主页的url
    base_url = "http://www.zgdztk.com/"

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
                firstParagraph = get_main_article_2(base_url + chapter_info_list[i][0], chapter_info_list[i][1], True)
                # 记录标题、新闻首段、url、发布日期(有时候首段格式奇怪，就跳过)
                if firstParagraph:
                    result.append([chapter_info_list[i][1], firstParagraph, base_url + chapter_info_list[i][0],
                                   chapter_info_list[i][3][14:]])
            if len(result) >= num:
                return result

    return result


def get_main_article_2(url, title, firstParagraph=False):
    chapter_response = requests.get(url)
    chapter_response.encoding = 'gbk'

    # chapter_html是这个新闻中的html文本
    chapter_html = chapter_response.text
    # 获取正文
    main_article = re.findall(r'[\u4e00-\u9fa5\d，。：“”；：？！（）]{25,}', chapter_html)
    if main_article[0].startswith("“中国地勘行业网”"):
        main_article.pop(0)
        main_article.pop(0)
    # 如果无匹配，返回False
    if len(main_article) < 2:
        return False
    for j in range(1, len(main_article)):
        main_article[0] += main_article[j]
    # 要求只返回前部分内容
    if firstParagraph:
        while main_article[0].startswith(title):
            main_article[0] = main_article[0][len(title):]
        # 将其中的"与<>内容删除
        firstSentence = re.sub('\<.*?\>', '', main_article[0])
        firstSentence = firstSentence.replace("&nbsp;", "")
        if len(firstSentence) >= 50:
            return firstSentence.replace('"', '\\"')[:50]
        return firstSentence.replace('"', '\\"')
    result = "  " + main_article[0]

    # 返回数据
    if len(main_article) > 1:
        for i in range(1, len(main_article)):
            if not main_article[i].isdigit():
                result += "\\n" + main_article[i]

    # 图片获取部分
    """picurl1 = get_picurl_images('%s.txt' % title)
    picurl2 = get_picurl_local('%s.txt' % title)
    download_image(picurl1, '..\\..\\..\\images')
    download_local(picurl2, '..\\__local')"""
    result = result.replace('"', '\\"')
    result = result.replace('\n', '\\n')
    result = result.replace("&nbsp;", "")
    return result


# 输入关键字、数量、页数，返回前page页的num个包含关键字的新闻相关内容，以列表形式返回(列表长度<=num)
def get_news_title_3(key):
    # 网站主页的url
    url = "http://www.nrsis.org.cn/portal/tzgg?pageNo=1&pageSize=20"
    base_url = "http://www.nrsis.org.cn/"

    result = []

    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    # chapter_info_list获取所有新闻的日期、地址、标题
    chapter_info_list = re.findall(r'<li><a href="(.*?)" target="_blank" class="my-link">(.*?)</a>'
                                   r'<span class="date">(.*?)</span></li>', html, re.S)
    # 将网站信息改为list
    chapter_info_list = list(map(list, chapter_info_list))
    # 对地址奇怪的新闻进行清洗，并将相对地址改为绝对地址
    for i in range(len(chapter_info_list)):
        if chapter_info_list[i][1].find(key) != -1:
            # 先获取新闻首段
            if chapter_info_list[i][0].startswith("http"):
                firstParagraph = get_main_article_1(chapter_info_list[i][0], chapter_info_list[i][1], True)
            else:
                firstParagraph = get_main_article_1(base_url + chapter_info_list[i][0], chapter_info_list[i][1], True)
            # 记录标题、新闻首段、url、发布日期(有时候首段格式奇怪，就跳过)
            if firstParagraph:
                if chapter_info_list[i][0].startswith("http"):
                    result.append([chapter_info_list[i][1], firstParagraph, chapter_info_list[i][0],
                                   chapter_info_list[i][2]])
                else:
                    result.append([chapter_info_list[i][1], firstParagraph, base_url + chapter_info_list[i][0],
                                   chapter_info_list[i][2]])

    return result


def get_news_title_4(key, pages, num):
  # 网站主页的url
  base_url = "https://www.cgsi.cn/xwdt"

  result = []

  for page in range(0, pages):
    if page == 0:
      url = "https://www.cgsi.cn/xwdt/index.htm"
    else:
      url = "https://www.cgsi.cn/xwdt/index_"+str(pages+1)+".htm"
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    # chapter_info_list获取所有新闻的地址、标题、标题、日期
    chapter_info_list = re.findall('<span class="art-caption"><a href="(.*?)" title="(.*?)" target="_blank">(.*?)</a>'
                                   '</span><span class="art-date">(.*?)</span>', html, re.S)
    # 将网站信息改为list
    chapter_info_list = list(map(list, chapter_info_list))
    # 对地址奇怪的新闻进行清洗，并将相对地址改为绝对地址
    for i in range(len(chapter_info_list)):
      if chapter_info_list[i][1].find(key) != -1:
        # 先获取新闻首段
        firstParagraph = get_main_article_1(base_url + chapter_info_list[i][0][5:], chapter_info_list[i][1], True)
        # 记录标题、新闻首段、url、发布日期(有时候首段格式奇怪，就跳过)
        if firstParagraph:
          result.append([chapter_info_list[i][1], firstParagraph, base_url + chapter_info_list[i][0][5:],
                         chapter_info_list[i][3]])
      if len(result) >= num:
        return result

  return result


def get_news_by_key_word(key, num):
    result = get_news_title_2(key, 3, num)
    result += get_news_title_4(key, 3, num-len(result))
    result += get_news_title_3(key)
    if len(result) < num:
        return result
    return result[:num]


def get_main_article(url):
    if "http://www.zgdztk.com/" in url:
        return get_main_article_2(url)
    return get_main_article_1(url)


if __name__ == "__main__":
    print(get_news_title_4("实物资料", 1, 3))
