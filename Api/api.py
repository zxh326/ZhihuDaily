import re
import sys
from getConfig import *
from flask_cors import *
from datetime import date,timedelta
from flask import Flask,jsonify,request,abort,render_template
from getDailyDetail import run as getDetail,getRandomDate
from getQiubai import run as getBai

app = Flask(__name__)

CORS(app,supports_credentials=True)

def check(s):
    return re.search(r'[^-\d]',s)
api_list = {
    'daily':  '[日报接口]GET / POST [date=xxxx-xx-xx]    localhost:5000:/api/daily ',
    'Mail' :  '[邮箱接口]GET        [subr=xxxx@xx.xx]    localhost:5000:/api/mail',
    'today':  '[日报今天]GET / POST                      localhost:5000/api/daily/today',
    'random': '[日报随机]GET / POST [count = n]          localhost:5000/api/daily/random',
    'qiubai': '[糗事百科]GET / POST [page = n,count = n] localhost:5000/api/qiubai'
}

@app.route('/')
def index():
    return render_template('demo.html')

@app.route('/api/daily',methods=['GET','POST'])
def gp():
    if request.method == "POST":
        yourdate = request.form.get('date')
    else:
        yourdate = request.args.get('date')

    if yourdate == None or yourdate > str(date.today()) or yourdate == '' or check(yourdate):
        abort(400)
    else:
        return jsonify(getDetail(yourdate))

#今天的
@app.route('/api/daily/today/')
def getToday():
    today = date.today()
    if getTodayStatus():
        jsontmp = getDetail(today)
    else:
        jsontmp = getDetail(today-timedelta(1))

    return jsonify(jsontmp)

#随机日期
@app.route('/api/daily/random',methods=['GET','POST'])
def getRandom():
    global nextday
    nextday = ''
    if request.method == "POST":
        count = request.form.get('count')
    else:
        count = request.args.get('count')
    if count == None :
        count = 1

    return jsonify(getRandomDate(count))

#糗事百科
@app.route('/api/qiubai',methods= ['GET','POST'])
def qiubai():
    if request.method == "POST":
        page = request.form.get('page')
        count = request.form.get('count')
    else:
        page = request.args.get('page')
        count = request.args.get('count')

    if page == None:
        page= '1'
    if count == None:
        count = '10'
    return jsonify(getBai(page,'fresh',count))

#邮箱接口
@app.route('/api/mail',methods=['GET'])
def orderMail():
    useremail = request.args.get('subr')
    if useremail == None:
        abort(400)
    else:
        if inSqldata(str(useremail)):
            return 'Success!'
        else:
            return 'Failed!'

def run(host = '127.0.0.1',port = '5000',isdebug = True):
    app.debug = isdebug
    app.run(host = host,port = port)