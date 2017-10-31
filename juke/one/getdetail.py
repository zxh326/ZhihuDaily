# coding:utf-8
import re
import requests
from one.apps import urlConfig
from .models import Tuwen
result = []


def getuc():
    s = requests.Session()
    data = s.get(urlConfig.Baseurl)
    php = data.cookies['PHPSESSID']
    token = re.findall('token = \'(.*)\'', data.text)

    return s, urlConfig.Apiurl + token[0], {'PHPSESSID': php}


def getinfo():
    s, url, cook = getuc()
    data = s.get(url, cookies=cook)
    con = data.json()['data'][0]
    # nextid = data[-1]['id']
    today_id = con['id']
    today_date = con['date'].replace(' / ', '-')
    today_title = con['title']
    today_url = con['url']
    today_img_url = con['img_url']
    today_picture_author = con['picture_author']
    today_content = con['content']
    today_text_authors = con['text_authors']

    # print(today_id, today_date, today_title, today_url, today_img_url,
    #       today_picture_author, today_content, today_text_authors)

    tuwen = Tuwen(id=today_id, date=today_date, title=today_title, url=today_url, img_url=today_img_url,
                  picture_author=today_picture_author, content=today_content, text_authors=today_text_authors)

    tuwen.save()


def run(count=1, israndom=0):
    global result
    result = []
    if int(israndom) == 0:
        sql = "select * from tuwen order by date desc limit " + str(count)
    else:
        sql = "select * from tuwen order by rand() limit " + str(count)

    data = Tuwen.objects.raw(sql)
    for raw in data:
        res = {}
        res['id'] = raw.id
        res['date'] = str(raw.date)
        res['title'] = raw.title
        res['img_url'] = raw.img_url
        res['img_author'] = raw.picture_author
        res['content'] = raw.content
        res['text_authors'] = raw.text_authors
        result.append(res)

    return result
