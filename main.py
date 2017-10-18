import json
from datetime import *

from cron import addCron

from threading import Thread

from getDailyDetail import run as getDeail

from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    today = date.today()
    jsontmp = getDeail(today)
    return str(jsontmp)


# 暂时先放这
@app.route('/api/')
@app.route('/api/<yourdate>')
def api(yourdate = None):
    if yourdate ==None:
        return 'Error date'
    else:
        return str(getDeail(yourdate))

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
