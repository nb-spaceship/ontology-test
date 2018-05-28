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

rpc = RPC()
cli = CLI()

@ddt.ddt
class TestContract(unittest.TestCase):
	def setUpClass():
		pass

	def setUp(self):
		pass

	@ddt.data(*TaskData("contract").tasks())
	def test_main(self, task):
		#step 1: signed tx
		LoggerInstance.open("contract/" + task.name())
		(result, response) = cli.run(task.name(), task.data(), LoggerInstance)
		signed_tx = response["result"]["signed_tx"]

		#step 2: call contract
		sendrawtxtask = Task("tasks/rpc/sendrawtransaction")
		sendrawtxtask.data()["REQUEST"]["params"] = [signed_tx, 1]
		(result, response) = rpc.run(sendrawtxtask.name(), sendrawtxtask.data(), LoggerInstance)

		LoggerInstance.close()
		if result:
			LoggerInstance.append_record(task.name(), "pass", "rpc/" + task.name())
		else:
			LoggerInstance.append_record(task.name(), "fail", "rpc/" + task.name())


if __name__ == '__main__':
    unittest.main()	