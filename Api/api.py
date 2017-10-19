import re
import sys
from getConfig import *
from flask_cors import *
from datetime import date,timedelta
from flask import Flask,jsonify,request,abort
from getDailyDetail import run as getDetail
app = Flask(__name__)
CORS(app,supports_credentials=True)


api_list = {
	'POST': 'POST date=xxxx-xx-xx to localhost:5000:/api',
	'GET' : 'GET localhost:5000:/api?date=xxxx-xx-xx'
}

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
    today = date.today()
    if getTodayStatus():
        jsontmp = getDetail(today)
    else:
        jsontmp = getDetail(today-timedelta(1))

    return jsonify(jsontmp)

def run(host = '127.0.0.1',port = '5000',debug = True):
	app.run(host=host,port=port,debug=debug)