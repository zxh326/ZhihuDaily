import os
import sys
import logging

os.chdir(sys.path[0])
class printLog():
	log_file = "Apptmp/logger.log"
	log_level = logging.DEBUG
	 
	logger = logging.getLogger("loggingmodule.NomalLogger")
	handler = logging.FileHandler(log_file)
	formatter = logging.Formatter("[%(levelname)s] %(asctime)s %(message)s")
	 
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(log_level)


	def __init__(self,aggr):
		self.log = aggr

	def Logdebug(self):
		self.logger.debug(self.log)

	def Loginfo(self):
		self.logger.info(self.log)

	def Logwarn(self):
		self.logger.warn(self.log)

	def Logerror(self):
		self.logger.error(self.log)
