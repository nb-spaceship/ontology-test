# -*- coding:utf-8 -*-
import unittest
import urllib
import urllib.request
import json
import os

from utils.config import Config
from utils.baseapi import BaseApi
from utils.taskdata import TaskData

class TestCLIRPC(unittest.TestCase, BaseApi):
	def setUp(self):
		self.TYPE = "clirpc"

	def test_clirpc(self):
		request = self.load_cfg("tasks/test_clirpc")
		reponse = self.connnetweb(request)
		print("request: " + json.dumps(request))
		print("reponse: " + json.dumps(reponse))

if __name__ == '__main__':
    unittest.main()	