import json
import requests
import pymysql
from getConfig import *
from bs4 import BeautifulSoup
from datetime import timedelta,date
result = {}
questionlist = []
# TODO:缓存机制 内存先存30-100
nextday = ''
def getId(conn,date):
    IDlist = []
    global nextday
    cur = conn.cursor()
    sql = "select * from daily where date = " + "\'" +str(date) + "\'"# + "order by date desc limit 2"
    cur.execute(sql)
    for r in cur:  
        IDlist.append(r[0])
        nextday = str(r[2]-timedelta(1))
    cur.close()
    # print (nextday)
    return IDlist
def getJson(question):
    tmpquestion={}
    answers = []
    answer = {}

    title = question.select('h2.question-title')[0].text
    url = question.select('div.view-more > a')[0]['href']
    answerpool = question.select('div.answer')
    for an in answerpool:
        answer = {}
        answer['body'] = an.select('div.content')[0].text
        answer['Author'] = an.select('span.author')[0].text
        answer['Author_image'] = an.select('img')[0]['src']
        try:
            answer['Author_bio'] = an.select('span.bio')[0].text
        except :
            answer['Author_bio'] = " "
            continue
        answers.append(answer)

    tmpquestion['title'] = title
    tmpquestion['answer'] = answers
    tmpquestion['url'] = url
    
    return tmpquestion

def getBody(body):
    soup = BeautifulSoup(str(body),'html.parser')
    data = soup.select('div.question')
    
    for divquestion in data:
        questionlist.append(getJson(divquestion))

    result['question'] = questionlist
    # print (json.dumps(result))
    
    result['nextday'] = nextday
    
    return result

# TODO:暂时只做处理一个ID / json处理起来麻烦
def getDetail(head,IDlist):
    for ID in IDlist:
        ID = IDlist[0]
        data = requests.get(getNewsApi()+str(ID),headers=head)
        data = json.loads(data.text)
        return getBody(data['body'])


#这里的date 要大于 2013-5-23,知乎日报的生日为 2013-5-19

def run(ydate):
    try:
       if ydate < date(2013,5,23):
            return 'Error date'
    except:
        if ydate < '2013-05-23':
            return 'Error date'
    head={}
    global result
    global questionlist
    questionlist = []
    result = {}
    head['User-Agent'] = getHead()
    conn = getConn()
    IDlist = getId(conn,ydate)
    conn.close()
    return getDetail(head,IDlist)