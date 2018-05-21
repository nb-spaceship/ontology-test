# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os

from utils.config import Config
from utils.baseapi import BaseApi
from utils.taskdata import TaskData

datas = TaskData("tasks/rpc")

@ddt.ddt
class TestRPC(unittest.TestCase, BaseApi):
	def setUp(self):
		self.TYPE = "rpc"

	@ddt.data(*datas.next())
	def test_rpc(self, api_file):
		self.runsingle(api_file)

if __name__ == '__main__':
    unittest.main()	