# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *

logger = LoggerInstance

class TestMutiContract(unittest.TestCase):
	def setUpClass():
		pass

	def setUp(self):
		print("TestMutiContract")
		pass

	def start(self, task):
		logger.open("contract/" + task.name())

	def finish(self, task):
		logger.close()

	def test_main(self):
		task = Task("tasks/contract/contract_demo")
		self.start(task)
		self.finish(task)

if __name__ == '__main__':
    unittest.main()	