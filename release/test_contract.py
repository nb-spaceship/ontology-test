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
from utils.cli import CLI
from utils.restful import Restful
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *

logger = LoggerInstance
rpc = RPC()
cli = CLI()

def call_contract(task):
	#step 1: signed tx
	logger.print("[-------------------------------]")
	logger.print("[ RUN      ] "+ "contract" + "/" + task.name())
	(result, response) = cli.run(task.name(), task.data())
	task.data()["RESPONSE"] = response
	logger.print("[ 1. SIGNED TX ] " + json.dumps(task.data(), indent = 4))

	#step 2: call contract
	signed_tx = response["result"]["signed_tx"]
	sendrawtxtask = Task("tasks/rpc/sendrawtransaction")
	sendrawtxtask.data()["REQUEST"]["params"] = [signed_tx, 1]
	(result, response) = rpc.run(sendrawtxtask.name(), sendrawtxtask.data())

	sendrawtxtask.data()["RESPONSE"] = response
	if "result" in response and "Result" in response["result"]:
		response["result"]["Result String"] = str(HexToByte(response["result"]["Result"]).decode('utf-8'))

	logger.print("[ 2. CALL CONTRACT ] " + json.dumps(sendrawtxtask.data(), indent = 4))
	if result:
		logger.print("[ OK       ] ")
		logger.append_record(task.name(), "pass", "contract/" + task.name())
	else:
		logger.print("[ Failed   ] ")
		logger.append_record(task.name(), "fail", "contract/" + task.name())

	return (result, response)

@ddt.ddt
class TestContract(unittest.TestCase):
	def setUpClass():
		pass

	def setUp(self):
		print("TestMutiContract")
		pass

	def start(self, task):
		logger.open("contract/" + task.name())

	def finish(self, task):
		logger.close()

	@ddt.data(*TaskData("contract").tasks())
	def test_main(self, task):
		self.start(task)
		call_contract(task)
		self.finish(task)

if __name__ == '__main__':
    unittest.main()	