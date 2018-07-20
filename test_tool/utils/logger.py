# -*- coding: utf-8 -*-
import time
import os

class Logger():
	def __init__(self):
		self.prefix = LOG_PATH + "/" + time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
		self.prefixFul = self.prefix;
		self.init = False
		#self.prefix = "logs/" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
		self.logfile = None

	def __del__(self):
		if self.init:
			self.collectionfile.close()

	def setSubFolder(self, folder):
		self.prefixFul = self.prefixFul + "/" + folder

	def open(self, filepath, title = None):
		if not self.init:
			if not os.path.exists(self.prefixFul):
				os.makedirs(self.prefixFul)
			self.collectionfile = open(self.prefixFul + "/collection_log.csv", "w")  # 打开文件
			self.collectionfile.write("NAME,STATUS,LOG PATH\n")
			self.init = True

		logdir = self.prefixFul + "/" + os.path.dirname(filepath)
		if not os.path.exists(logdir):
			os.makedirs(logdir)

		self.logpath = self.prefixFul + "/" + filepath
		self.logfile = open(self.logpath, "w")  # 打开文件
		self.logtitle = title if title else os.path.splitext(filepath)[0]
	#write
	def print(self, str):
		print(str)
		if self.logfile:
			self.logfile.write(str + "\n")

	def error(self, str):
		str = "[ ERROR ]  " + str
		print(str)
		if self.logfile:
			self.logfile.write(str + "\n")

	def close(self, result = None, msg = None):
		if not result is None:
			if result:
				self.print("[ OK       ] ")
				self.append_record(self.logtitle, "pass", self.logpath)
			else:
				self.print("[ Failed   ] ")
				self.append_record(self.logtitle, "fail", self.logpath)
		if self.logfile:
			self.logfile.close()
			self.logfile = None

	def append_record(self, name, status, logpath):
		self.collectionfile.write(name + "," + status + "," + logpath + "\n")


LoggerInstance = Logger()