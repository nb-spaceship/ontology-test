# -*- coding: utf-8 -*-
from websocket import create_connection
import websocket

import requests
import threading
import json
import os
import sys
import time
from utils.config import Config
from utils.baseapi import BaseApi
from utils.taskdata import *

class WS(BaseApi):
	LONG_LIVE_WS = None
	def __init__(self):
		self.TYPE = "websocket"
		self.LONG_LIVE_WS = None
		pass

	def con(self, ip, request):
		try:
			url = ""
			if ip:
				url = "ws://" + ip + ":20335"
			else:
				url = Config.WS_URL

			ws = create_connection(url)
			ws.send(json.dumps(request))
			response = ws.recv()
			ws.close()
			return json.loads(response)
		except Exception as e:
			return json.loads("{\"Desc\": \"Connection Error\", \"Error\": \"Connection Error\"}")	

	#special test case
	def ws_thread(self, message_cb = None):
		def on_message(ws, message):
			print("message: " + message)
			if message_cb:
				message_cb(message)

		def on_error(ws, error):
			print(error)

		def on_close(ws):
			print("### closed ###")

		def on_open(ws):
			print("### open ###")

		WS.LONG_LIVE_WS = websocket.WebSocketApp(Config.WS_URL,
							on_message = on_message,
							on_error = on_error,
							on_close = on_close,
							on_open = on_open)
		WS.LONG_LIVE_WS.run_forever()

	def ws_heartbeat_thread(self, heartbeat_gap = 5):
		while True:
			time.sleep(heartbeat_gap)
			WS.LONG_LIVE_WS.send(json.dumps(Task("tasks/ws/heartbeat.json").data()["REQUEST"]))

	def long_live_connnet(self, heartbeat = True, heartbeat_gap = 5, message_cb = None):
		t1 = threading.Thread(target=self.ws_thread, args=(message_cb,))
		t1.start()
		if heartbeat:
			t2 = threading.Thread(target=self.ws_heartbeat_thread, args=(heartbeat_gap,))
			t2.start()

		while True:
			try:
				command = sys.stdin.readline().strip('\n')
				if ".json" not in command:
					command = command + ".json"
				
				WS.LONG_LIVE_WS.send(json.dumps(Task("tasks/ws/" + command).data()["REQUEST"]))
				#ws.send(json.dumps(self.load_cfg(request)))
			except Exception as e:
				print(e)

if __name__ == "__main__":
	ws = WS()
	ws.long_live_connnet()