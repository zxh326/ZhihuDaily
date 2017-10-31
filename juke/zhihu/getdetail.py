# coding:utf-8
import re
import requests
from zhihu.models import Daily
from zhihu.apps import ua, ApiConfig
from datetime import timedelta
from bs4 import BeautifulSoup
result = {}
questionlist = []
nextday = ''


def checkdate(s):
    return not re.search(r'[^-\d]', s)


def getAnswer(question):
    tmpquestion = {}
    answers = []
    answer = {}
    title = question.select('h2.question-title')[0].text

    try:
        url = question.select('div.view-more > a')[0]['href']
    except:
        return None

    answerpool = question.select('div.answer')

    for an in answerpool:
        answer = {}
        tmpcontent = ''
        for i in an.select('div.content'):
            tmpcontent += str(i)
        answer['body'] = tmpcontent
        answer['Author'] = an.select('span.author')[0].text
        answer['Author_image'] = an.select('img')[0]['src']
        try:
            answer['Author_bio'] = an.select('span.bio')[0].text
        except:
            answer['Author_bio'] = ' '

        answers.append(answer)

    tmpquestion['title'] = title
    tmpquestion['answer'] = answers
    tmpquestion['url'] = url

    return tmpquestion


def getQuestion(idlist):
    global result, questionlist
    result = {}
    questionlist = []
    head = {}

    head['User-Agent'] = ua.UserAgent

    for ID in idlist:
        data = requests.get(ApiConfig.news + str(ID), headers=head)
        body = data.json()['body']

        soup = BeautifulSoup(body, 'lxml')
        data = soup.select('div.question')

        for divquestion in data:
            question = getAnswer(divquestion)
            if question is not None:
                questionlist.append(question)
            else:
                pass
    result['question'] = questionlist
    result['nextday'] = nextday
    return result


def getIdList(ydate):
    idlist = []
    global nextday
    sql = "select * from daily where date = " + '\'' + str(ydate) + '\''
    Tmp = Daily.objects.raw(sql)
    for raw in Tmp:
        idlist.append(raw.id)
        nextday = str(raw.date - timedelta(1))
    return idlist


def getrandid(count=1):
    idlist = []
    global nextday
    sql = "select * from daily order by rand() limit " + str(count)
    Tmp = Daily.objects.raw(sql)
    for raw in Tmp:
        idlist.append(raw.id)
        nextday = str(raw.date - timedelta(1))
    return getQuestion(idlist)


def getToday():
    idlist = []
    global nextday
    sql = "select * from daily order by date desc limit 1"
    Tmp = Daily.objects.raw(sql)
    for raw in Tmp:
        idlist.append(raw.id)
        nextday = str(raw.date - timedelta(1))
    return getQuestion(idlist)


def getInfo():
    head = {}

    head['User-Agent'] = ua.UserAgent
    data = requests.get(ApiConfig.last, headers=head)
    data = data.json()
    todaydate = data['date'][0:4] + '-' + data['date'][4:6] + '-' + data['date'][6:]
    todaytitle = data['stories'][-1]['title']
    todayid = data['stories'][-1]['id']
    daily = Daily(id=todayid,title=todaytitle,date=todaydate)
    daily.save()

def run(ydate):
    # 请求数据验证
    if not checkdate(ydate):
        return '{\'ms\':400}'
    try:
        if ydate < date(2013, 5, 23):
            return '{\'ms\':401}'
    except:
        if ydate < '2013-05-23':
            return '{\'ms\':401}'

    return getQuestion(getIdList(ydate))
