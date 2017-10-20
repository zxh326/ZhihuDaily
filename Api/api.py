import re
import sys
from getConfig import *
from flask_cors import *
from datetime import date,timedelta
from flask import Flask,jsonify,request,abort
from getDailyDetail import run as getDetail,getRandomDate


app = Flask(__name__)

CORS(app,supports_credentials=True)

def check(s):

    return re.search(r'[^-\d]',s)

@app.route('/')
def index():
	return jsonify(api_list)

@app.route('/api',methods=['GET','POST'])
def gp():
	if request.method == "POST":
	    yourdate = request.form.get('date')
	else:
	    yourdate = request.args.get('date')

	if yourdate == None or yourdate > str(date.today()) or yourdate == '' or check(yourdate):
	    abort(400)
	else:
	    return jsonify(getDetail(yourdate))


@app.route('/mail',methods=['GET'])
def orderMail():
	useremail = request.args.get('subr')
	if useremail == None:
		abort(400)
	else:
		if inSqldata(str(useremail)):
			return 'Success!'
		else:
			return 'Failed!'


@app.route('/today/')
def getToday():

    if getTodayStatus():
        jsontmp = getDetail(today)
    else:
        jsontmp = getDetail(today-timedelta(1))

    return jsonify(jsontmp)

#随机日期
@app.route('/random',methods=['GET','POST'])
def getRandom():
	if request.method == "POST":
	    count = request.form.get('count')
	else:
	    count = request.args.get('count')
	if count == None :
		count = 1

	return jsonify(getRandomDate(count))


def run(host = '127.0.0.1',port = '5000',isdebug = True):
	app.debug = isdebug
	app.run(host = host,port = port)