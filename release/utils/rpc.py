# -*- coding: utf-8 -*-

import requests
import json
import os
from utils.config import Config
from utils.baseapi import BaseApi

class RPC(BaseApi):
	def __init__(self):
		self.TYPE = "rpc"

	def con(self, ip, request):
		try:
			con_url = ""
			if ip:
				con_url = "http://" + ip + ":20336/jsonrpc"
			else:
				con_url = Config.RPC_URL
			response = requests.post(con_url, data=json.dumps(request), headers=Config.RPC_HEADERS)
			return response.json()
		except Exception as e:
			return json.loads("{\"Desc\": \"Connection Error\", \"Error\": \"Connection Error\"}")
