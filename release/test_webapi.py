# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

from utils.config import Config
from utils.baseapi import BaseApi
from utils.rpc import RPC
from utils.websocket import WS
from utils.restful import Restful
from utils.taskdata import TaskData
from utils.logger import LoggerInstance
from utils.parametrizedtestcase import ParametrizedTestCase

rpc = RPC()
ws = WS()
restful = Restful()
logger = LoggerInstance

class TestWebAPI(ParametrizedTestCase):
	def setUpClass():
		pass

	def setUp(self):
		pass

	def test_rpc(self):
		task = self.param
		logger.open(task.log_path())
		(result, response) = rpc.run(task.name(), task.data(), logger)
		logger.close()
		if result:
			logger.append_record(task.name(), "pass", task.log_path())
		else:
			logger.append_record(task.name(), "fail", task.log_path())

	def test_ws(self):
		task = self.param
		logger.open(task.log_path())
		(result, response) = ws.run(task.name(), task.data(), logger)
		logger.close()
		if result:
			logger.append_record(task.name(), "pass", task.log_path())
		else:
			logger.append_record(task.name(), "fail", task.log_path())

	def test_restful(self):
		task = self.param
		logger.open(task.log_path())
		(result, response) = restful.run(task.name(), task.data(), logger)
		logger.close()
		if result:
			logger.append_record(task.name(), "pass", task.log_path())
		else:
			logger.append_record(task.name(), "fail", task.log_path())

####################################################
if __name__ == '__main__':
	filterfile = ""
	opts, args = getopt.getopt(sys.argv[1:], "n:", ["name="])
	for op, value in opts:
		if op in ("-n", "--name"):
			filterfile = value

	suite = unittest.TestSuite()    
	if filterfile == '':
		for task in TaskData('rpc').tasks():
			suite.addTest(TestWebAPI("test_rpc", param = task))
		for task in TaskData('restful').tasks():
			suite.addTest(TestWebAPI("test_restful", param = task))
		for task in TaskData('ws').tasks():
			suite.addTest(TestWebAPI("test_ws", param = task))

	unittest.TextTestRunner(verbosity=2).run(suite)