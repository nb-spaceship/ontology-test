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
from parametrizedtestcase import ParametrizedTestCase

logger = LoggerInstance
filterfile = ""
rpc = RPC()
cli = CLI()

def call_contract(task):
	try:
		#step 1: signed tx
		logger.print("[-------------------------------]")
		logger.print("[ RUN      ] "+ "contract" + "/" + task.name())
		(result, response) = cli.run(task.name(), task.data())
		task.data()["RESPONSE"] = response
		logger.print("[ 1. SIGNED TX ] " + json.dumps(task.data(), indent = 4))

		#step 2: call contract
		signed_tx = None
		if not response is None and "result" in response and not response["result"] is None and "signed_tx" in response["result"]:
			signed_tx = response["result"]["signed_tx"]

		if signed_tx == None or signed_tx == '':
			raise Error("no signed tx")

		sendrawtxtask = Task("tasks/rpc/sendrawtransaction")
		sendrawtxtask.data()["REQUEST"]["params"] = [signed_tx, 1]
		(result, response) = rpc.run(sendrawtxtask.name(), sendrawtxtask.data())

		sendrawtxtask.data()["RESPONSE"] = response

		if not response is None and ("result" in response and "Result" in response["result"]):
			response["result"]["Result String"] = HexToByte(response["result"]["Result"]).decode('iso-8859-1')
		
		logger.print("[ 2. CALL CONTRACT ] " + json.dumps(sendrawtxtask.data(), indent = 4))

		if response is None or "error" not in response or str(response["error"]) != 0:
			raise Error("call contract error")

		logger.print("[ OK       ] ")
		logger.append_record(task.name(), "pass", "contract/" + task.name())
		return (result, response)

	except Error as err:
		logger.print("[ Failed   ] " + err.msg)
		logger.append_record(task.name(), "fail", "contract/" + task.name())
		return (False, None)

class TestContract(ParametrizedTestCase):
	def setUpClass():
		pass

	def setUp(self):
		print("TestMutiContract")
		pass

	def start(self, task):
		logger.open("contract/" + task.name())

	def finish(self, task):
		logger.close()

	def test_neo(self):
		task = self.param
		self.start(task)
		call_contract(task)
		self.finish(task)
		pass

if __name__ == '__main__':
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
