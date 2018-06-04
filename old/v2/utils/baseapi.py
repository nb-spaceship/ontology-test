# -*- coding: utf-8 -*-
from utils.config import Config
from utils.multithread import MyThread
from abc import ABCMeta, abstractmethod
import json
import time
import os
import urllib
import urllib.request
import requests

class BaseApi:
	def __init__(self):
		self.TYPE = None
		pass

	def load_cfg(self, cfg):
		cfg_file = open(cfg, "rb")
		cfg_json = json.loads(cfg_file.read().decode("utf-8"))
		cfg_file.close()
		return cfg_json

	def multithread_run(self, cfg_request, cfg_response):
		result = True
		thread_list = []
		response = None

		for i in range(Config.THREAD):
			t = MyThread(self.connnetweb, args=cfg_request)
			thread_list.append(t)
			t.start()

		for t in thread_list:
			t.join()
			result = result and self.judge_result(cfg_response, t.get_result())
			response = t.get_result()
			print("[ THREAD %d ]" % thread_list.index(t))
			print("[ RESULT   ]" + json.dumps(response, indent = 4))

		return (result, response)

	@abstractmethod
	def judge_result(self, except_respons, real_respones):
		for key in except_respons.keys():
			if real_respones:
				if key in real_respones:
					self.assertTrue(real_respones[key] == except_respons[key])
				elif key.capitalize() in real_respones:
					self.assertTrue(real_respones[key.capitalize()] == except_respons[key])
			else:
				self.assertEqual(0, 1)
		return True

	def connnetweb(self, request):
		if self.TYPE == "restful":
			return self.connnet_restful(request)
		elif self.TYPE == "ws":
			return self.connnet_ws(request)
		elif self.TYPE == "rpc":
			return self.connnet_rpc(Config.RPC_URL, request)
		elif self.TYPE == "clirpc":
			return self.connnet_rpc(Config.CLIRPC_URL, request)

	def connnet_restful(self, api_request):
		api_url = Config.RESTFUL_URL + api_request["api"]
		api_command = "GET"
		if "command" in api_request:
			api_command = api_request["command"]

		if api_command == "POST":
			api_post_data = None
			if "params" in api_request:
				api_post_data = api_request["params"]
			#api_post_data_encode = urllib.urlencode(json.dumps(api_post_data))
			data = urllib.parse.urlencode(api_post_data).encode(encoding='UTF8')
			req = urllib.request.Request(url = api_url, data = data)
			response = urllib.request.urlopen(req)
			return json.loads(response.read().decode("utf-8"))
		else:
			response = urllib.request.urlopen(api_url)
			return json.loads(response.read().decode("utf-8"))

	def connnet_rpc(self, url, api_request):
		response = requests.post(url, data=json.dumps(api_request), headers=Config.RPC_HEADERS)
		return response.json() 

	def connnet_ws(self, api_request):
		ws = create_connection(Config.WS_URL)
		ws.send(json.dumps(api_request))
		response = ws.recv()
		ws.close()
		return json.loads(response)

	@abstractmethod
	def runsingle(self, api_name):
		start_time = time.time()
		print("[-------------------------------]")
		print("[ RUN      ] "+ self.TYPE + "." +api_name.split('.')[0])
		cfg_content = self.load_cfg(api_name)
		cfg_request = cfg_content["REQUEST"]
		cfg_response = cfg_content["RESPONSE"]
		print("[ PARAMS   ]" + json.dumps(cfg_content, indent = 4))

		(result, response) = self.multithread_run(cfg_request, cfg_response)
		end_time = time.time()
		time_consumed = (end_time - start_time) * 1000
		
		if result:
			print("[ OK       ] " + self.TYPE + "."+api_name.split('.')[0]," (%d ms)" % (time_consumed))
		else:
			print("[ Failed   ] " + self.TYPE + "."+api_name.split('.')[0]," (%d ms)"% (time_consumed))
		print("[-------------------------------]")
		print("")
		