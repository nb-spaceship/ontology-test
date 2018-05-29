# -*- coding: utf-8 -*-

import requests
import json
import os
from utils.config import Config
from utils.baseapi import BaseApi

class CLI(BaseApi):
	def __init__(self):
		self.TYPE = "clirpc"

	def con(self, ip, request):
		try:
			url = ""
			if ip:
				url = "http://" + ip + ":20336/jsonrpc"
			else:
				url = Config.CLIRPC_URL

			response = requests.post(url, data=json.dumps(request), headers=Config.RPC_HEADERS)
			return response.json()
		except Exception as e:
			return json.loads("{\"Desc\": \"Connection Error\", \"Error\": \"Connection Error\"}")