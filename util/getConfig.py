# coding:utf-8
import os
import sys
import pymysql
from printlog import printLog as log
from configparser import ConfigParser

cp = ConfigParser()

os.chdir(sys.path[0])

cp.read('config.ini')

def hostIp():
    return cp['HOST']['ip']

def hostPort():
    return cp['HOST']['port']

def isDebug():
    return cp['HOST']['debug'] == str(True)

# 获取头
def getHead():
    return cp['UA']['User-Agent']

# 获取Api
def getLastApi():
    return cp['Api']['LAST']

def getNewsApi():
    return cp['Api']['NEWS']

# 获取Sql 地址
def getSqlAddr():
    return cp['Sql']['ADDR']

# 获取Sql 端口
def getSqlPort():
    return cp['Sql']['PORT']

# 获取Sql user
def getSqlUser():
    return cp['Sql']['USER']

# 获取Sql pass
def getSqlPass():
    return cp['Sql']['PASS']

# 获取Sql database
def getDb():
    return cp['Sql']['DATABASE']

# 获取Sql TABLE
def getTb():
    return cp['Sql']['TABLE']

def getTodayStatus():
    cp.read('config.ini')
    return str(True)==cp['Status']['today']

def UpdateTodayStatus(status):
    cp['Status']['today'] = status
    with open('config.ini','w+') as f:
        cp.write(f)

def isFirstRun():
    return cp['Status']['firstrun'] == str('True')

def UpdateFirstRunStatus(status):
    cp['Status']['firstrun'] = status
    with open('config.ini','w+') as f:
        cp.write(f)

def getConn():
    try:
        conn = pymysql.connect(host = getSqlAddr() ,port = int(getSqlPort()),user = getSqlUser(),passwd=getSqlPass(),db = getDb(),use_unicode = True,charset ='utf8')
        return conn
    except Exception as e:
        log("数据库连接错误！"+ str(e)).Logerror()
        return -1
def inSqldata(mailaccount):
    conn = getConn()
    cur = conn.cursor()
    sql = "INSERT INTO subscriber VALUES (%s)"
    try:
        cur.execute(sql,mailaccount)
        log("Insert Success " + mailaccount ).Loginfo()
        conn.commit()
        return True
    except Exception as e:
        log("InsertFailed！"+ str(Exception(e))).Logerror()
        log("InsertFailed！"+ mailaccount ).Logerror()
        return False
    cur.close()
    conn.close()

