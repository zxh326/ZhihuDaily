import os

import sys

from configparser import ConfigParser
cp = ConfigParser()

os.chdir(sys.path[0])

cp.read('config.ini')

# 获取头
def getHead():
	return cp['UA']['User-Agent']

# 获取Api
def getLastApi():
	return cp['Api']['LAST']

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



