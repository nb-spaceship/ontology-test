# -*- coding: utf-8 -*-
from websocket import create_connection

import requests
import json
import os
from config import Config
from BaseApi import BaseApi


class WSApi(BaseApi):
	def __init__(self):
		BaseApi.TYPE = "WebSocket"
		BaseApi.CONFIG_PATH = "websocket"
		pass

	def connnet(self, request):
		ws = create_connection(Config.WS_URL)
		ws.send(json.dumps(request))
		response = ws.recv()
		ws.close()
		return json.loads(response)

	#special test case
	def run_forever(self):
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