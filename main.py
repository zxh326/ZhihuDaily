import sys
sys.path.append('Api/')
sys.path.append('util/')

from cron import addCron
from threading import Thread

# from getDailyDetail import run as getDeail

# from flask import Flask,render_template,jsonify,request
from getConfig import *
from api import run as getDetail

# 仅程序第一次运行
def run():
    tlist = []
    t1 = Thread(target=getDetail,args=(hostIp(),hostPort(),isDebug(),))
    tlist.append(t1)

    if isFirstRun():
        t2 = Thread(target=addCron)
        tlist.append(t2)
    for t in tlist:
        t.start()
    for t in tlist:
        t.join()

if __name__ == '__main__':
    run()
