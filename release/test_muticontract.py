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
from test_contract import call_contract

logger = LoggerInstance
rpc = RPC()
cli = CLI()

class TestMutiContract(unittest.TestCase):
	def setUpClass():
		pass

	def setUp(self):
		print("TestMutiContract")
		pass

	def test_main(self):
		task = Task("tasks/contract/contract_demo")
		call_contract(task)

if __name__ == '__main__':
    unittest.main()	