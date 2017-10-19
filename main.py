import json
from datetime import date,timedelta

from cron import addCron

from flask_cors import *

from threading import Thread

from getDailyDetail import run as getDeail

from flask import Flask,render_template,jsonify,request
from getConfig import *

app = Flask(__name__)
CORS(app,supports_credentials=True)
@app.route('/')
def index():
    today = date.today()
    if getTodayStatus():
        jsontmp = getDeail(today)
    else:
        jsontmp = getDeail(today-timedelta(1))

    return jsonify(jsontmp)


# 暂时先放这
@app.route('/api/',methods=['GET','POST'])
@app.route('/api/')
def api():

    if request.method == "POST":
        yourdate = request.form.get('date')
    else:
        yourdate = request.args.get('date')

    if yourdate ==None:
        return 'Error date'
    else:
        return jsonify(getDeail(yourdate))

# 仅程序第一次运行
def run():
    tlist = []
    t1 = Thread(target=addCron)
    tlist.append(t1)
    for t in tlist:
        t.start()
    for t in tlist:
        t.join()

if __name__ == '__main__':
    app.run(debug=True)
