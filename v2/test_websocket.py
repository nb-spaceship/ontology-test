# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import websocket

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
		def on_message(ws, message):
			print(message)

		def on_error(ws, error):
			print(error)

		def on_close(ws):
			print("### closed ###")

		def on_open(ws):
			print("### open ###")

		ws = websocket.WebSocketApp(Config.WS_URL,
									on_message = on_message,
									on_error = on_error,
									on_close = on_close)
		ws.on_open = on_open
		ws.run_forever()


if __name__ == '__main__':
    unittest.main()	