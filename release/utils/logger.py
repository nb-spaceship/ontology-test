# -*- coding: utf-8 -*-
import time
import os

class Logger():
	def __init__(self):
		#pathstr = "logs/" + time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
		pathstr = "logs/" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
		for subpath in ["rpc", "restful", "ws", "cli"]:
			if not os.path.exists(pathstr + "/" + subpath):
				os.makedirs(pathstr + "/" + subpath)		
		self.prefix = pathstr

		self.collectionfile = open(pathstr + "/collection_log.csv", "w")  # 打开文件
		self.collectionfile.write("NAME,STATUS,LOG PATH\n")

	def __del__(self):
		self.collectionfile.close()

	def open(self, filepath):
		self.logpath = self.prefix + "/" + filepath + ".log"
		self.logfile = open(self.logpath, "w")  # 打开文件

	#write
	def print(self, str):
		print(str)
		self.logfile.write(str + "\n")

	def close(self):
		self.logfile.close()

	def append_record(self, name, status, logpath):
		self.collectionfile.write(name + "," + status + "," + logpath + "\n")


LoggerInstance = Logger()