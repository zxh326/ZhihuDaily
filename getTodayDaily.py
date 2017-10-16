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
	except Exception as e:
		log(e).Logerror()

def inSertSql(host,port,user,passw,db,tb,id,title,today):
	sql = "INSERT INTO " + str(tb) + " VALUES (%s,%s,%s)"
	try:
		tmp = pymysql.connect(host = host,port = int(port),user = user,passwd=passw,db = db,use_unicode = True,charset ='utf8')
		cur = tmp.cursor()
		cur.execute(sql,(id,title,today))
		tmp.commit()
		tmp.close()
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
	inSertSql(getSqlAddr(),getSqlPort(),getSqlUser(),getSqlPass(),getDb(),getTb(),id,title,today)

if __name__ == '__main__':
	run()
