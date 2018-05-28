# -*- coding: utf-8 -*-
from utils.config import Config
from utils.taskthread import TaskThread
from utils.logger import Logger
from utils.taskdata import *

from abc import ABCMeta, abstractmethod
import json
import time
import os

class BaseApi:
	def __init__(self):
		self.TYPE = None
		self.CONFIG_PATH = None
		pass

	def multithread_run(self, logger, cfg_request, cfg_response):
		result = True
		thread_list = []
		response = None

		for i in range(Config.THREAD):
			t = TaskThread(self.con, args=cfg_request)
			thread_list.append(t)
			t.start()

		for t in thread_list:
			t.join()
			result = result and self.judge_result(cfg_response, t.get_result())
			response = t.get_result()
			if logger:
				logger.print("[ THREAD %d ]" % thread_list.index(t))
				logger.print("[ RESULT   ]" + json.dumps(response, indent = 4))

		return (result, response)

	@abstractmethod
	def judge_result(self, except_respons, real_respones):
		for key in except_respons.keys():
			if real_respones and key in real_respones and real_respones[key] == except_respons[key]:
				continue
			elif real_respones and key.capitalize() in real_respones and real_respones[key.capitalize()] == except_respons[key]:
				continue
			else:
				return False
		return True

	@abstractmethod
	def con(self, request):
		pass

	@abstractmethod
	def run(self, name, request, logger = None):
		start_time = time.time()
		if logger:
			logger.print("[-------------------------------]")
			logger.print("[ RUN      ] "+ self.TYPE + "." + name)
		cfg_content = request
		cfg_request = cfg_content["REQUEST"]
		cfg_response = cfg_content["RESPONSE"]
		if logger:
			logger.print("[ PARAMS   ]" + json.dumps(cfg_content, indent = 4))

		(result, response) = self.multithread_run(logger, cfg_request, cfg_response)
		end_time = time.time()
		time_consumed = (end_time - start_time) * 1000
		
		if logger:
			if result:
				logger.print("[ OK       ] " + self.TYPE + "."+ name +" (%d ms)" % (time_consumed))
			else:
				logger.print("[ Failed   ] " + self.TYPE + "."+ name +" (%d ms)"% (time_consumed))
			logger.print("[-------------------------------]")
			logger.print("")
		return (result, response)
