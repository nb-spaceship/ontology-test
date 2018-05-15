from config import Config
from MultiThread import MyThread
from abc import ABCMeta, abstractmethod
import json
import time
import os


class BaseApi:
	def __init__(self):
		self.TYPE = None
		self.CONFIG_PATH = None
		pass

	def load_cfg(self, cfg):
		cfg_file = open(cfg, "rb")
		cfg_json = json.load(cfg_file)
		return cfg_json

	def multithread_run(self, api_name, cfg_request, cfg_response):
		result = True
		thread_list = []
		response = None

		for i in range(Config.THREAD):
			t = MyThread(self.connnet, args=cfg_request)
			thread_list.append(t)
			t.start()

		for t in thread_list:
			t.join()
			result = result and self.judge_result(api_name, cfg_response, t.get_result())
			response = t.get_result()
			print "[ THREAD %d ]" % thread_list.index(t)
			print "[ RESULT   ]" + json.dumps(response, indent = 4)

		return (result, response)

	@abstractmethod
	def judge_result(self, api_name, except_respons, real_respones):
		for key in except_respons.keys():
			if real_respones.has_key(key) and real_respones[key] == except_respons[key]:
				continue
			elif real_respones.has_key(key.capitalize()) and real_respones[key.capitalize()] == except_respons[key]:
				continue
			else:
				return False
		return True

	@abstractmethod
	def connnet(self, request):
		pass

	@abstractmethod
	def run(self, api_name):
		start_time = time.time()
		print "[-------------------------------]"
		print "[ RUN      ] "+ self.TYPE + "." +api_name.split('.')[0]
		cfg_content = self.load_cfg(self.CONFIG_PATH + "/" + api_name)
		cfg_request = cfg_content["REQUEST"]
		cfg_response = cfg_content["RESPONSE"]
		print "[ PARAMS   ]" + json.dumps(cfg_content, indent = 4)

		(result, response) = self.multithread_run(api_name, cfg_request, cfg_response)
		end_time = time.time()
		time_consumed = (end_time - start_time) * 1000
		
		if result:
			print "[ OK       ] " + self.TYPE + "."+api_name.split('.')[0]," (%d ms)" % (time_consumed)
		else:
			print "[ Failed   ] " + self.TYPE + "."+api_name.split('.')[0]," (%d ms)"% (time_consumed)
		print "[-------------------------------]"
		print ""

	@abstractmethod
	def runAll(self):
		for root, dirs, files in os.walk(self.CONFIG_PATH):  
			for file in files:
				self.run(file)
