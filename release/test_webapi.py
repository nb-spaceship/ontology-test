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
		pass

	@ddt.data(*TaskData("rpc").tasks())
	def test_rpc(self, task):
		logpath = "rpc/" + task.name()
		LoggerInstance.open(logpath)
		(result, response) = rpc.run(task.name(), task.data(), LoggerInstance)
		LoggerInstance.close()
		if result:
			LoggerInstance.append_record(task.name(), "pass", logpath)
		else:
			LoggerInstance.append_record(task.name(), "fail", logpath)

	@ddt.data(*TaskData("ws").tasks())
	def test_ws(self, task):
		logpath = "ws/" + task.name()
		LoggerInstance.open(logpath)
		(result, response) = ws.run(task.name(), task.data(), LoggerInstance)
		LoggerInstance.close()
		if result:
			LoggerInstance.append_record(task.name(), "pass", logpath)
		else:
			LoggerInstance.append_record(task.name(), "fail", logpath)

	@ddt.data(*TaskData("restful").tasks())
	def test_restful(self, task):
		logpath = "restful/" + task.name()
		LoggerInstance.open(logpath)
		(result, response) = restful.run(task.name(), task.data(), LoggerInstance)
		LoggerInstance.close()
		if result:
			LoggerInstance.append_record(task.name(), "pass", logpath)
		else:
			LoggerInstance.append_record(task.name(), "fail", logpath)

if __name__ == '__main__':
    unittest.main()	