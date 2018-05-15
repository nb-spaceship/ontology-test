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
