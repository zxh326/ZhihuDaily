import os
import sys
import json
import pymysql
import requests
from datetime import *
from getConfig import *

os.chdir(sys.path[0])

#获取daily
def getToday(apiUrl,head):
	data = requests.get(apiUrl,headers=head)

	data = json.loads(data.text)
	
	with open('Apptmp/daily.log','w+') as f:
		f.write(str(data['stories'][-1]))

def inSertSql(host,port,user,passw,db,tb,url,title,today):
	sql = "INSERT INTO " + str(tb) + " VALUES (%s,%s,%s)"
	try:
		tmp = pymysql.connect(host = host,port = int(port),user = user,passwd=passw,db = db,use_unicode = True,charset ='utf8')
		cur = tmp.cursor()
		cur.execute(sql,(url,title,today))
		tmp.commit()
		tmp.close()
	except Exception as e:
		raise e

def run():
	head={}
	head['User-Agent'] = getHead()
	print (1)
	today = date.today()

	getToday(getLastApi(),head)

	with open('Apptmp/daily.log','r') as f:
		data = eval(f.readlines()[0])
		title = data['title']
		url = "http://daily.zhihu.com/story/"+ str(data['id'])
	inSertSql(getSqlAddr(),getSqlPort(),getSqlUser(),getSqlPass(),getDb(),getTb(),url,title,today)

if __name__ == '__main__':
	run()
