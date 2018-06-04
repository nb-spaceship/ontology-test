# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import websocket
from websocket import create_connection

from utils.config import Config
from utils.baseapi import BaseApi
from utils.taskdata import TaskData

datas = TaskData("tasks/websocket")
 
@ddt.ddt
class TestWebSocket(unittest.TestCase, BaseApi):
	def setUp(self):
		self.TYPE = "ws"

	@ddt.data(*datas.next())
	def test_ws(self, api_file):
		self.runsingle(api_file)

	def test_heartbeat(self):
		ws = create_connection(Config.WS_URL)
		ws.send(json.dumps(self.load_cfg("tasks/websocket/heartbeat.json")))
		ws.send(json.dumps(self.load_cfg("tasks/websocket/subscribe.json")))

		while True:
			response = ws.recv()
			print("response: " + json.dumps(json.loads(response)))

if __name__ == '__main__':
    unittest.main()	