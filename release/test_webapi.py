# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os

from utils.config import Config
from utils.baseapi import BaseApi
from utils.rpc import RPC
from utils.websocket import WS
from utils.restful import Restful
from utils.taskdata import TaskData
from utils.logger import LoggerInstance

rpc = RPC()
ws = WS()
restful = Restful()

@ddt.ddt
class TestWebAPI(unittest.TestCase):
	def setUpClass():
		pass

	def setUp(self):
		print("setUp")

	@ddt.data(*TaskData("tasks/rpc").tasks())
	def test_rpc(self, task):
		LoggerInstance.open("rpc/" + task.name())
		(result, response) = rpc.run(task, LoggerInstance)
		LoggerInstance.close()
		if result:
			LoggerInstance.append_record(task.name(), "pass", "rpc/" + task.name())
		else:
			LoggerInstance.append_record(task.name(), "fail", "rpc/" + task.name())

	@ddt.data(*TaskData("tasks/ws").tasks())
	def test_ws(self, task):
		LoggerInstance.open("ws/" + task.name())
		(result, response) = ws.run(task, LoggerInstance)
		LoggerInstance.close()
		if result:
			LoggerInstance.append_record(task.name(), "pass", "ws/" + task.name())
		else:
			LoggerInstance.append_record(task.name(), "fail", "ws/" + task.name())

	@ddt.data(*TaskData("tasks/restful").tasks())
	def test_restful(self, task):
		LoggerInstance.open("restful/" + task.name())
		(result, response) = restful.run(task, LoggerInstance)
		LoggerInstance.close()
		if result:
			LoggerInstance.append_record(task.name(), "pass", "restful/" + task.name())
		else:
			LoggerInstance.append_record(task.name(), "fail", "restful/" + task.name())

if __name__ == '__main__':
    unittest.main()	