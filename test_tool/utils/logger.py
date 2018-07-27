# -*- coding: utf-8 -*-
import time
import os
from utils.config import Config

class Logger():
	def __init__(self):
		self.prefix = Config.LOG_PATH + "/" + time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
		self.prefixFul = self.prefix;
		self.init = False
		#self.prefix = "logs/" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
		self.logfile = None
		self.logpath = ""
		self.collectionfile = None

	def __del__(self):
		if self.init:
			pass

	def setPath(self, path):
		self.prefixFul = self.prefix + "/" + path

	def logPath(self):
		return self.logpath

	def open(self, filepath, title = None):
		self.logpath = self.prefixFul + "/" + filepath
		logdir = self.prefixFul + "/" + os.path.dirname(filepath)
		if not os.path.exists(logdir):
			os.makedirs(logdir)
			
		if not self.init:
			if not os.path.exists(self.prefixFul):
				os.makedirs(self.prefixFul)
			self.append_record("NAME", "STATUS", "LOG PATH")
			self.init = True


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
			if result == "pass":
				self.print("[ OK       ] ")
				self.append_record(self.logtitle, "pass", self.logpath.replace(self.prefix, ""))
			elif result == "fail":
				self.print("[ Failed   ] ")
				self.append_record(self.logtitle, "fail", self.logpath.replace(self.prefix, ""))
			elif result == "block":
				self.print("[ Block    ] ")
				self.append_record(self.logtitle, "block", self.logpath.replace(self.prefix, ""))
		if self.logfile:
			self.logfile.close()
			self.logfile = None

	def append_record(self, name, status, logpath):
		self.collectionfile = open(os.path.dirname(self.logpath) + "/collection_log.csv", "a+")  # 打开文件
		self.collectionfile.write(name + "," + status + "," + logpath + "\n")
		self.collectionfile.close()

LoggerInstance = Logger()