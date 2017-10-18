import os
import sys
import json
import pymysql
import requests
from datetime import *
from getConfig import *
from printlog import printLog as log


os.chdir(sys.path[0])

#获取daily
def getToday(apiUrl,head):
    try:
        data = requests.get(apiUrl,headers=head)

        data = json.loads(data.text)
        
        with open('Apptmp/daily.log','w+') as f:
            f.write(str(data['stories'][-1]))
        log('get daily detail Success!').Loginfo()
        UpdateTodayStatus('True')
    except Exception as e:
        UpdateTodayStatus('False')
        log(e).Logerror()

def inSertSql(conn,tb,id,title,today):
    sql = "INSERT INTO " + str(tb) + " VALUES (%s,%s,%s)"
    try:
    #    print (type(conn))
        cur = conn.cursor()
        cur.execute(sql,(id,title,today))
        conn.commit()
        conn.close()
        log('insert Mysql Success!').Loginfo()
    except Exception as e:
        log(e).Logerror()

def run():
    head={}
    head['User-Agent'] = getHead()

    today = date.today()

    getToday(getLastApi(),head)

    with open('Apptmp/daily.log','r') as f:
        data = eval(f.readlines()[0])
        title = data['title']
        id = data['id']
    

    #TODO: 尝试失败重连
    conn = getConn()
    if(conn == -1):
        log('failed').Logerror()
        exit(-1)
    else:
        inSertSql(conn,getTb(),id,title,today)

if __name__ == '__main__':
    run()
