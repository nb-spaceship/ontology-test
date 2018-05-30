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
from utils.cli import CLI
from utils.restful import Restful
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

from common_api import call_contract

logger = LoggerInstance
rpc = RPC()
cli = CLI()

####################################################
#test cases
class TestContract(ParametrizedTestCase):
	def start(self, task):
		logger.open(task.log_path())

	def finish(self, task, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task.name(), "pass", task.log_path())
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task.name(), "fail", task.log_path())
		logger.close()

	def test_neo(self):
		task = self.param
		self.start(task)
		(result, response) = call_contract(task)
		self.finish(task, result, response)

####################################################
if __name__ == '__main__':
	filterfile = ""
	opts, args = getopt.getopt(sys.argv[1:], "n:", ["name="])
	for op, value in opts:
		if op in ("-n", "--name"):
			filterfile = value

	suite = unittest.TestSuite()    
	if filterfile == '':
		for task in TaskData('contract/neo').tasks():
			suite.addTest(TestContract("test_neo", param = task))    
	else:
		suite.addTest(TestContract("test_neo", param = Task(filterfile)))
	unittest.TextTestRunner(verbosity=2).run(suite)
